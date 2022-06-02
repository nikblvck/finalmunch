from .db import db

class Post(db.Model):
  __tablename__ = 'posts'

  id = db.Column(db.Integer, primary_key=True)
  caption = db.Column(db.Text, nullable=True)
  category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
  updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())


  images = db.relationship('Image', backref='post', lazy=True)


  @property
  def post_summary(self):
    return self.caption[:100]

  def to_dict(self):
    return {
      'id': self.id,
      'caption': self.caption,
      'category_id': self.category_id,
      'user_id': self.user_id,
      'created_at': self.created_at,
      'updated_at': self.updated_at,
      'images': [image.image_summary for image in self.images]
    }

  def __repr__(self):
    return '<Post %r>' % self.id

  def __str__(self):
    return self.__repr__()
