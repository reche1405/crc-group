from promo.models import db
from promo.models.base_model import BaseModel

class Review(BaseModel):
    __tablename__ = 'reviews'
    text = db.Column(db.Text, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id', ondelete="CASCADE"), unique=True, nullable=True)
    project = db.relationship('Project', backref=db.backref('review', uselist=False, lazy=True))
    rating = db.Column(db.Integer, default=5)