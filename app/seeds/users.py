from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():
    # Demo user is the first user added to the database
    #Create a list of users
    users = [
        {
            'first_name': 'Demo',
            'last_name': 'User',
            'username': 'demo',
            'email': 'demouser@munch.io',
            'password': 'munchies2022!',
            'is_admin': False
        },
        {
            'first_name': 'Admin',
            'last_name': 'User',
            'username': 'admin',
            'email': 'admin@munch.io',
            'password': 'goodvibes8jet',
            'is_admin': True
        },
        {
            'first_name': 'Rubeus',
            'last_name': 'Hagrid',
            'username': 'rhagrid',
            'email': 'hagrid@munch.io',
            'password': 'password',
            'is_admin': False
        }
    ]
    # Loop through the list of users and add them to the database
    for user in users:
        new_user = User(
            first_name=user['first_name'],
            last_name=user['last_name'],
            username=user['username'],
            email=user['email'],
            password=user['password'],
            is_admin=user['is_admin']
        )
        db.session.add(new_user)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
