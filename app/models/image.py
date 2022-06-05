from .db import db

class Image(db.Model):
  __tablename__ = 'images'

  id = db.Column(db.Integer, primary_key=True)
  post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
  url = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
  updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

  post = db.relationship('Post', back_populates='images')


  @property
  def image_summary(self):
    return { 'post_id': self.post_id, 'url': self.url }


  def to_dict(self):
    return {
      'id': self.id,
      'post_id': self.post_id,
      'url': self.url,
      'created_at': self.created_at,
      'updated_at': self.updated_at
    }
