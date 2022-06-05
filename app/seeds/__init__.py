from flask.cli import AppGroup
from .users import seed_users, undo_users
from .categories import seed_categories, undo_categories
from .posts import seed_posts, undo_posts
from .has_categories import seed_has_categories, undo_has_categories
from .images import seed_images, undo_images
# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_categories()
    seed_posts()
    seed_has_categories()
    seed_images()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_categories()
    undo_posts()
    undo_has_categories()
    undo_images()
    # Add other undo functions here
