
from promo.models import db
from .base_model import BaseModel, SluggedModel
from .section import BaseSection
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
    url_prefix = 'services'

    parent_route = db.Column(db.String(255), nullable=False, default='service_list')
    parent_title = db.Column(db.String(255), nullable=False, default='Services')
    short_desc = db.Column(db.String(500), nullable=False)
    desc = db.Column(db.Text, nullable=False)
    svg = db.Column(db.Text, nullable=True)
    benefits_list_id = db.Column(db.Integer, db.ForeignKey('lists.id'), nullable=True)
    benefits_list = db.relationship('List', foreign_keys=[benefits_list_id], backref=db.backref('service_full', uselist=False))

    intro_list_id = db.Column(db.Integer, db.ForeignKey('lists.id'), nullable=True)
    intro_list = db.relationship('List', foreign_keys=[intro_list_id], backref=db.backref('service_intro', uselist=False))
    
    featured_media_id = db.Column(db.Integer,  db.ForeignKey('media.id'), nullable=True)
    featured_media = db.relationship('Media', backref=db.backref('featured_service_images', lazy=True))
    is_featured = db.Column(db.Boolean, default=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), default=1)
    category = db.relationship('Category', backref=db.backref("services"), lazy=True)
    def __repr__(self):
        return self.title

    @classmethod
    def get_home(cls):
        return cls.query.filter_by(is_featured=True).limit(4)
    
    def section(self, tag):
        return next((s for s in self.sections if s.tag == tag), None)
   

class ServiceSection(BaseSection):
    __tablename__ = 'servicesections'
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    service = db.relationship('Service', backref='sections')
    order = db.Column(db.Integer, nullable=False, default=0)
    media_id = db.Column(db.Integer, db.ForeignKey('media.id'), nullable=True)
    media = db.relationship('Media', backref='service_sections')


    



