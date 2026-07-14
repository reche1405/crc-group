from promo.models import db
from promo.models.base_model import BaseModel, SluggedModel
from datetime import datetime
article_media = db.Table(
    'article_media',
    db.Column('article_id', db.Integer, db.ForeignKey('articles.id'), primary_key=True),
    db.Column('media_id', db.Integer, db.ForeignKey('media.id'), primary_key=True)
)

class BlogCategory(BaseModel):
    __tablename__ = 'blogcats'
    title = db.Column(db.String(255), nullable=False)

class Article(SluggedModel):
    __tablename__ = 'articles'
    url_prefix = 'blog'
    parent_route = db.Column(db.String(255), nullable=False, default='article_list')
    parent_title = db.Column(db.String(255), nullable=False, default='Our Blog')
    subtitle = db.Column(db.String(255), nullable=True)
    abstract = db.Column(db.Text, nullable=False)
    body_one = db.Column(db.Text, nullable=False)
    body_two = db.Column(db.Text, nullable=True)
    body_three = db.Column(db.Text, nullable=True)
    blog_form = db.Column(db.String(255), default="article-short" )
    author = db.Column(db.String(255), nullable=False)
    published = db.Column(db.Boolean, default=False)
    featured_media_id = db.Column(db.Integer,  db.ForeignKey('media.id'), nullable=True)
    featured_media = db.relationship('Media', backref=db.backref('featured_article_images', lazy=True))
    category_id = db.Column(db.Integer, db.ForeignKey('blogcats.id'), nullable=True)
    category = db.relationship('BlogCategory', backref=db.backref('articles', lazy=True))

    # nullable published date to allow scheduling future publications
    published_date = db.Column(db.Date, nullable=True)

    media_list = db.relationship(
        'Media', secondary=article_media,
        primaryjoin="Article.id == article_media.c.article_id",
        secondaryjoin="Media.id == article_media.c.media_id",
        backref=db.backref('articles')
    )
    
    def __repr__(self):
        return self.title
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    @classmethod
    def count(cls):
        return cls.query.count()
    
    @classmethod
    def get_page(cls, page, items_per_page):
        today = datetime.now().date()
        if page is None or page < 1:
            page = 1
        if items_per_page is None or items_per_page < 1:
            items_per_page = 10
        offset = (page - 1) * items_per_page
        return cls.query.order_by(cls.id).filter_by(published=True).filter(cls.published_date <= today).offset(offset).limit(items_per_page).all()
    
    @classmethod
    def get_by_slug(cls, slug):
        if not slug:
            return None
        return cls.query.filter_by(slug=slug).first()

    
