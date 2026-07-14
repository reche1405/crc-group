from datetime import datetime
import enum
from promo.models import db
from sqlalchemy.ext.orderinglist import ordering_list
from promo.models.base_model import BaseModel, SluggedModel



class ProjectTag(enum.Enum):
  
    CRC = 'Roof Conversion'
    GRM = 'Garden Room'
    INT = 'Interior Design'

class Project(SluggedModel):
    __tablename__ = 'projects'
    url_prefix = 'projects'
    
    parent_route = db.Column(db.String(255), nullable=False, default='project_list')
    parent_title = db.Column(db.String(255), nullable=False, default='Our Work')
    desc = db.Column(db.Text, nullable=True) 
    short_desc = db.Column(db.String(500), nullable=False)
    is_featured = db.Column(db.Boolean, nullable=False)  
    type = db.Column(db.String(100), nullable=True)
    tag = db.Column(db.Enum(ProjectTag), default=ProjectTag.CRC, nullable=False )
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=True)
    location = db.relationship('Location', backref=db.backref('projects', lazy=True))
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=True)
    service = db.relationship('Service',  backref=db.backref('projects', lazy=True))
    customer_name = db.Column(db.String(100), nullable=True)
    featured_media_id = db.Column(db.Integer,  db.ForeignKey('media.id'), nullable=True)
    featured_media = db.relationship('Media', backref=db.backref('featured_project_images', lazy=True))

    def __repr__(self):
        return self.title

    @classmethod
    def get_featured(cls):
        """Returns only projects marked as featured."""
        return cls.query.filter_by(is_featured=True).all()
    
    @classmethod
    def get_page(cls, page, items_per_page):
        if page is None or page < 1:
            page = 1
        if items_per_page is None or items_per_page < 1:
            items_per_page = 10
        offset = (page - 1) * items_per_page
        return cls.query.order_by(cls.id).offset(offset).limit(items_per_page).all()
    
    @classmethod
    def count(cls):
        return cls.query.count()
    
    def to_carousel_json(self):
        """Convert project media to carousel JSON format"""
        if not self.media: return

        return {
            'items': [media.to_carousel_dict() for media in self.media],
            'project_id': self.id,
            'project_title': self.title,
            'autoplay_interval': 4000  # or get from project settings
        }
    
    

class Orientation(enum.Enum):
    Portrait = "portrait"
    Landscape = 'landscape'
    def __str__(self):
        return self.value

class Gallery(BaseModel):
    __tablename__ = 'galleries'
    
    name = db.Column(db.String(100), default='Default Slideshow')
    orientation = db.Column(db.Enum(Orientation), default=Orientation.Portrait, nullable=False)
    
    # Foreign Key & Relationship to Project
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id', ondelete="CASCADE"), unique=True, nullable=True)
    project = db.relationship('Project', backref=db.backref('gallery', uselist=False, lazy=True))


    slides = db.relationship(
        'Slide', 
        order_by='Slide.sort_order', 
        collection_class=ordering_list('sort_order'),
        cascade="all, delete-orphan",
        backref='gallery'
    )

    def __repr__(self):
        return f"<Gallery {self.name} (Project ID: {self.project_id})>"
    
    def to_json(self):
        return {
            "items" : [slide.to_json() for slide in self.slides],
            'orientation' : self.orientation.value,
            'project_id': self.project_id,
            'project_title': self.name,
            'autoplay_interval': 4000  # or get from project settings
            }

class Slide(BaseModel):
    __tablename__ = 'slides'
    
    gallery_id = db.Column(db.Integer, db.ForeignKey('galleries.id', ondelete="CASCADE"), nullable=False)
    sort_order = db.Column(db.Integer, nullable=False, default=0) # Made non-nullable for ordering_list
    
    # Relationship to Media
    media_id = db.Column(db.Integer, db.ForeignKey('media.id'), nullable=False)
    # Changed backref to 'slides' (plural) to avoid naming collisions if Media is used elsewhere
    media = db.relationship('Media', backref=db.backref('slides', lazy=True))
    
    def __repr__(self):
        return f"<Slide id={self.id} gallery_id={self.gallery_id} order={self.sort_order}>"
    
    def to_json(self):
        return self.media.to_carousel_dict()

