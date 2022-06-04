from app.models import db, HasCategory


def seed_has_categories():
  #List of Post Categories
  has_categories = [
    {
      'post_id': 1,
      'category_id': 1
    },
    {
      'post_id': 1,
      'category_id': 2
    },
    {
      'post_id': 1,
      'category_id': 3
    },
    {
      'post_id': 2,
      'category_id': 14
    },
    {
      'post_id':2,
      'category_id': 6
    },
    {
      'post_id': 3,
      'category_id': 14
    },
    {
      'post_id': 3,
      'category_id': 15
    },
    {
      'post_id':2,
      'category_id': 7
    }
  ]

  for has_category in has_categories:
    new_has_category = HasCategory(**has_category)
    db.session.add(new_has_category)
  db.session.commit()


def undo_has_categories():
  db.session.execute('TRUNCATE has_categories RESTART IDENTITY CASCADE;')
  db.session.commit()
  
