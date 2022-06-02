from .db import db

class Comemnt(db.Model):
  __tablename__ = 'comments'

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
  content = db.Column(db.Text, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
  updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())


  def to_dict(self):
    return {
      'id': self.id,
      'user_id': self.user_id,
      'post_id': self.post_id,
      'content': self.content,
      'created_at': self.created_at,
      'updated_at': self.updated_at
    }
    
