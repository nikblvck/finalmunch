from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import db, Post, Image, Comment, Like, Category, HasCategory
from app.s3_helpers import (
    upload_file_to_s3, allowed_file, get_unique_filename)
from app.forms import NewPostForm


post_routes = Blueprint('posts', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages

#Create a new post with image and caption
@post_routes.route("/new", methods=["POST"])
def new_post_with_images():
    form = NewPostForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        #Create the new post, add categories and upload images to S3
        post = Post(
            caption=form.caption.data,
            user_id=current_user.id
        )
        db.session.add(post)
        db.session.commit()
        #Add the categories to the post
        for category in form.categories.data.split(','):
            category = Category.query.filter(Category.name == category).first()
            if category:
                has_category = HasCategory(
                    post_id=post.id,
                    category_id=category.id
                )
                db.session.add(has_category)
        db.session.commit()
        #Upload images to S3
        for image in form.images.data.split(','):
            image = Image(
                post_id=post.id,
                image_url=upload_file_to_s3(image)
            )
            db.session.add(image)
        db.session.commit()
        return post.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

#Read all posts
@post_routes.route("/")
def read_all_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])
#Read a single post
@post_routes.route("/<int:post_id>", methods=["GET"])
def get_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        return jsonify({"error": "Post not found"}), 404
    return post.to_dict()

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
