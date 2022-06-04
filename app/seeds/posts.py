from app.models import db, Post, Image

#function to seed posts to the database


def seed_posts():
  #create a list of posts
  posts = [
    {
      'caption': 'Just a demo post',
      'user_id': 1,
      'category_id': 1,
      'created_at': new Date(),
      'updated_at': new Date()

    },
    {
      'caption': 'Another demo post',
      'user_id': 1,
      'category_id': 1,
      'created_at': new Date(),
      'updated_at': new Date()
    }
  ]
  #loop through the list of posts and add them to the database
  for post in posts:
    new_post = Post(
        caption=post['caption'],
        user_id=post['user_id'],
        category_id=post['category_id'],
        created_at=post['created_at'],
        updated_at=post['updated_at']
    )
    db.session.add(new_post)
  db.session.commit()

def undo_posts():
  db.session.execute('TRUNCATE posts RESTART IDENTITY CASCADE;')
  db.session.commit()
