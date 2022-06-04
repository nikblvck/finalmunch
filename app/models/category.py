from .db import db

class Category(db.Model):
  __tablename__ = 'categories'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)

  post = db.relationship('Post', back_populates='category', lazy=True)

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'posts': [post.to_dict() for post in self.posts],
      'post_count': len(self.posts)
    }
