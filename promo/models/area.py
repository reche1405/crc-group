from promo.models import db
from promo.models.base_model import BaseModel, SluggedModel

class Area(BaseModel):
    __tablename__ = 'areas'

    title = db.Column(db.String(255), nullable=False)
    short_desc = db.Column(db.String(500), nullable=False)
    featured_media_id = db.Column(db.Integer,  db.ForeignKey('media.id'), nullable=True)
    featured_media = db.relationship('Media', backref=db.backref('featured_area_images', lazy=True))
   
    @classmethod
    def get_home(cls):
        return cls.query.limit(4).all()

    def __repr__(self):
        return self.title
    

class Location(SluggedModel):
    __tablename__ = "locations"
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'), nullable=False)
    area = db.relationship('Area', backref=db.backref('locations', lazy=True))
    short_description = db.Column(db.String(512), nullable=True)
    long_description = db.Column(db.Text, nullable=True)
    slug = db.Column(db.String(255), nullable=True)
    def __repr__(self):
        return f'<Location {self.title}>'
    
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    

