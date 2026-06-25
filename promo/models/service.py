
from promo.models import db
from .base_model import BaseModel, SluggedModel
from flask import current_app
class Category(BaseModel):
    __tablename__ = "categories"
    title = db.Column(db.String(255), unique=True, nullable=False )

    def __repr__(self):
        return self.title
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    def get_by_title(cls, title):
        
        cat = cls.query.filter_by(title=title).first()
        return cat
    

class Service(SluggedModel):
    __tablename__ = 'services'
    short_desc = db.Column(db.String(500), nullable=False)
    desc = db.Column(db.Text, nullable=False)
    svg = db.Column(db.Text, nullable=True)
    benefits_list_id = db.Column(db.Integer, db.ForeignKey('lisits.id'), nullable=True)
    benefits_list = db.relationship('List', backref=db.backref('service', uselist=False))
    featured_media_id = db.Column(db.Integer,  db.ForeignKey('media.id'), nullable=True)
    featured_media = db.relationship('Media', backref=db.backref('featured_service_images', lazy=True))

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), default=1)
    category = db.relationship('Category', backref=db.backref("services"), lazy=True)
    def __repr__(self):
        return self.title

    @classmethod
    def get_home(cls):
        return cls.query.limit(4).all()
   
    def get_absolute_url(self):
        return f"{current_app['BASE_URL']}/services/{self.slug}"
    

    



