from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import Post, Image, Comment, Like, Category, HasCategory
from app.s3_helpers import (
    upload_file_to_s3, allowed_file, get_unique_filename)

post_routes = Blueprint('posts', __name__)




#Create a new post with image and caption
@post_routes.route("/new", methods=["POST"])
def new_post_with_images():
    caption = request.form.get("caption")
    categories = request.form.get("categories")
    images = request.form.get("images")
    user_id = request.form.get("user_id")

    new_post = Post(caption=caption, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()

    # Add categories
    categories = categories.split(",")
    for category in categories:
        new_category = Category.query.filter_by(name=category).first()
        if new_category is None:
            new_category = Category(name=category)
            db.session.add(new_category)
            db.session.commit()
        new_has_category = HasCategory(
            post_id=new_post.id, category_id=new_category.id)
        db.session.add(new_has_category)
        db.session.commit()

 #Takes array of image urls and uploads them to S3
    images = request.files["images"]
    for image in images:
        if not allowed_file(image.filename):
            return jsonify({"error": "Invalid file type"}), 400
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image, "images")
        if "url" not in upload:
            return upload, 400
        new_image = Image(image_url=upload["url"], post_id=new_post.id)
        db.session.add(new_image)
        db.session.commit()

    return jsonify(new_post.to_dict())

#Read all posts
@post_routes.route("/")
def read_all_posts():
    posts = Post.query.all()
    return {'posts': [post.to_dict() for post in posts]}

#Read a single post
@post_routes.route("/<int:post_id>", methods=["GET"])
def get_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        return jsonify({"error": "Post not found"}), 404
    return jsonify(post.to_dict())

#Update a post
@post_routes.route("/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    post = Post.query.get(post_id)
    if post is None:
        return jsonify({"error": "Post not found"}), 404
    caption = request.form.get("caption")
    categories = request.form.get("categories")
    images = request.form.get("images")
    user_id = request.form.get("user_id")

    post.caption = caption
    post.user_id = user_id
    db.session.commit()

    # Add categories
    categories = categories.split(",")
    for category in categories:
        new_category = Category.query.filter_by(name=category).first()
        if new_category is None:
            new_category = Category(name=category)
            db.session.add(new_category)
            db.session.commit()
        new_has_category = HasCategory(
            post_id=post.id, category_id=new_category.id)
        db.session.add(new_has_category)
        db.session.commit()

    #Takes array of image urls and uploads them to S3
    images = request.files["images"]
    for image in images:
        if not allowed_file(image.filename):
            return jsonify({"error": "Invalid file type"}), 400
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image, "images")
        if "url" not in upload:
            return upload, 400
        new_image = Image(image_url=upload["url"], post_id=post.id)
        db.session.add(new_image)
        db.session.commit()

    return jsonify(post.to_dict())

#Delete a post
@post_routes.route("/<int:post_id>", methods=["DELETE"])
@login_required
def delete_one_post(post_id):
    post = Post.query.get(post_id)
    if post is None:
        return jsonify({"error": "Post not found"}), 404
    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted"})
