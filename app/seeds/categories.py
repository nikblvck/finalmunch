from app.models import db, Category

#Add categories to the database
def seed_categories():
  #Create a list of categories
  categories = [
    {
      'name': 'Soul Food'
    },
    {
      'name': 'Vegan'
    },
    {
      'name': 'Vegetarian'
    },
    {
      'name': 'Breakfast'
    },
    {
      'name': 'Lunch'
    },
    {
      'name': 'Barbecue'
    },
    {
      'name': 'Finger Food'
    },
    {
      'name': 'Dessert'
    },
    {
      'name': 'Soup'
    },
    {
      'name': 'Salad'
    },
    {
      'name': 'Japanese'
    },
    {
      'name': 'Mexican'
    },
    {
      'name': 'Italian'
    },
    {
      'name': 'Chinese'
    },
    {
      'name': 'Thai'
    },
    {
      'name': 'Indian'
    },
    {
      'name': 'American'
    },
    {
      'name': 'French'
    },
    {
      'name': 'German'
    },
    {
      'name': 'Greek'
    },
    {
      'name': 'Spanish'
    },
    {
      'name':'Nigerian'
    },
    {
      'name':'African'
    },
    {
      'name':'Caribbean'
    },
    {
      'name':'Mediterranean'
    },
    {
      'name': 'From Scratch'
    }
  ]

  #Loop through the list of categories and add them to the database
  for category in categories:
    new_category = Category(
      name=category['name']
    )
    db.session.add(new_category)
  db.session.commit()

#Uses a raw SQL query to TRUNCATE the categories table.
def undo_categories():
  db.session.execute('TRUNCATE categories RESTART IDENTITY CASCADE;')
  db.session.commit()
