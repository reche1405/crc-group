from promo.models import db
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from .base_model import BaseModel

class List(BaseModel):
    __tablename__ = "lisits"
    tag = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True )
    items = db.relationship('ListItem', backref='list', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return self.tag

    @classmethod
    def get_for_tag(cls, tag):
        try:
            return cls.query.filter_by(tag=tag).one()
        except NoResultFound:
            return None
        except MultipleResultsFound:
            return cls.query.filter_by(tag=tag).first()
        
    @classmethod
    def get_for_tags(cls, tags):
        tag_list = cls.query.filter(cls.tag.in_(tags)).all()
        if tag_list:
            return {x.tag: x for x in tag_list}
        return None

    @classmethod
    def get_home(cls):
        tags = ['why-rok', 'home-welcome']
        tag_list = cls.query.filter(cls.tag.in_(tags)).all()
        return {x.tag: x for x in tag_list}


class ListItem(BaseModel):
    __tablename__ = 'listitems'
    order = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(255), nullable=False)
    subtext = db.Column(db.Text, nullable=True)
    svg = db.Column(db.Text, nullable=True)
    list_id = db.Column(db.Integer, db.ForeignKey('lisits.id'), nullable=False)
