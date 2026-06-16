from promo.models import db
import datetime
class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column('last_updated', db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)


    @classmethod
    def get_all(cls):
        return cls.query.all()
    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def count(cls):
        return cls.query.count()
    
class SluggedModel(BaseModel):
    __abstract__ = True
    title = db.Column(db.String(255), nullable=False, unique=True)  

    slug = db.Column(db.String(255), nullable=True)

    @classmethod
    def get_by_slug(cls, slug):
        return cls.query.filter_by(slug=slug).first()
    

