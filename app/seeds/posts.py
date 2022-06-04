from app.models import db, Post, Image

#function to seed posts to the database


def seed_posts():
  #create a list of posts
  posts = [
    {
      'caption': 'This is a test post',
      'category_id': 1,
      'user_id': 1
    },
    {
      'caption': 'This is another test post',
      'category_id': 2,
      'user_id': 1
    },
    {
      'caption': 'This is the third and probably final...for now...test post',
      'category_id': 3,
      'user_id': 1
    }
  ]
  #loop through the list of posts and add them to the database
  for post in posts:
    new_post = Post(**post)
    db.session.add(new_post)
  db.session.commit()


def undo_posts():
  db.session.execute('TRUNCATE posts RESTART IDENTITY CASCADE;')
  db.session.commit()
