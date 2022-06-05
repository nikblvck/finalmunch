from app.models import db, Image

#Function to seed post images to database
def seed_images():
  #Create a list of images
  images = [
    {
      'post_id': 1,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1646853754/munch/Soup_TomatoGrilledCheese.jpg'
    },
    {
      'post_id': 1,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1646853659/munch/Soup_SoupSammieBrew.jpg'
    },
    {
      'post_id': 1,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1646853848/munch/Soup_WaffleGC.jpg'
    },
    {
      'post_id': 1,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1646853933/munch/Sandwich_Ribeye.jpg'
    },
    {
      'post_id': 1,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1646853880/munch/Sandwich_ItalianWToppenade.jpg'
    },
    {
      'post_id': 2,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1646023123/munch/Dessert_IceCreamCake.png'
    },
    {
      'post_id': 2,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1646023062/munch/Dessert_CreamFilledCrepeChoc.jpg'
    },
    {
      'post_id': 2,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1646022996/munch/Dessert_Nutrageous.jpg'
    },
    {
      'post_id': 2,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1646023191/munch/Dessert_IceCreamCookieCake.jpg'
    },
    {
      'post_id': 3,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1646583309/munch/Indian_Honey%20Chili%20Potatoes.jpg'
    },
    {
      'post_id': 3,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1646849899/munch/Breakfast_SteakNEggsTots.jpg'
    },
    {
      'post_id': 3,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1646849934/munch/Breakfast_CampfireStyle.jpg'
    },
    {
      'post_id': 3,
      'url': 'https://res.cloudinary.com/bigtechnik/image/upload/v1646853461/munch/Seafood_RisottoScallopsJumboPrawn.png'
    }
  ]

#Loop through the images list and add each image to the database

  for image in images:
    new_image = Image(
      post_id=image['post_id'],
      url=image['url']
    )
    db.session.add(new_image)
  db.session.commit()

def undo_images():
  db.session.execute('TRUNCATE images RESTART IDENTITY CASCADE;')
  db.session.commit()
