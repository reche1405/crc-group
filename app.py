from flask import Flask
import os
from dotenv import load_dotenv

from promo.admin.commands import create_admin
from promo.models import db, migrate
from promo.extensions import mail, admin, login_manager, cache

load_dotenv()
def create_app():
    from promo.admin.views import BaseSecureView, SecuredAdminIndexView, ProjectAdminView, MediaAdminView, ArticleAdminView, SlugifyAdminView
    from routes import main

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))
    # 
    app = Flask(__name__,
         template_folder=os.path.join(BASE_DIR, 'promo', 'templates'),
        static_folder=os.path.join(BASE_DIR, 'promo', 'static'),
        static_url_path='/static'
                )
    app.cli.add_command(create_admin)


    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    app.config['RECAPTCHA_PUBLIC_KEY'] = os.environ.get('RECAPTCHA_PUBLIC_KEY')
    app.config['RECAPTCHA_PRIVATE_KEY'] = os.environ.get('RECAPTCHA_SECRET_KEY')

    app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
    app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT'))
    app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS') in ['True', 'true', '1', 1]
    app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL') in ['True', 'true', '1', 1]
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', 'contact@nmemusic.co.uk')
    app.config['INBOUND_MAIL'] = os.environ.get('INBOUND_MAIL')
    app.config['MAIL_DEBUG'] = True
    app_env = os.environ.get('FLASK_ENV')
    if app_env is None:
        app_env = 'production'

   
    app.config['CACHE_TYPE'] = os.environ.get('CACHE_TYPE', 'SimpleCache')
    app.config['CACHE_DEFAULT_TIMEOUT'] = int(os.environ.get('CACHE_DEFAULT_TIMEOUT', '300'))
    app.config['FLASK_ENV'] = app_env
    mail.init_app(app)
    admin.init_app(app, index_view=SecuredAdminIndexView())
    login_manager.init_app(app)
    cache.init_app(app)


    UPLOAD_PATH = os.path.join(BASE_DIR, 'promo', 'media')

    app.config['UPLOAD_PATH'] = UPLOAD_PATH
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'project.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)
    migrate.init_app(app, db, command="migrations")
    with app.app_context():
        from promo.models.media import Media
        from promo.models.user import User
        from promo.models.project import Project, Gallery, Slide
        from promo.models.service import Service, Category, ServiceSection
        from promo.models.article import Article, BlogCategory
        from promo.models.page import HeroHeight, Page,Section
        from promo.models.list import List, ListItem
        from promo.models.area import Area, Location
        from promo.models.review import Review



        db.create_all()

        admin.add_view(MediaAdminView(Media, db, category='Static'))
        admin.add_view(BaseSecureView(User, db, category='Auth'))
        admin.add_view(ProjectAdminView(Project, db, category='Projects'))
        admin.add_view(BaseSecureView(Gallery, db, category='Projects'))
        admin.add_view(BaseSecureView(Slide, db, category='Projects'))
        admin.add_view(BaseSecureView(Review, db, category='Projects'))
        admin.add_view(BaseSecureView(Category, db, category='Services' ))
        admin.add_view(SlugifyAdminView(Service, db, category='Services'))
        admin.add_view(BaseSecureView(ServiceSection, db, category='Services'))
        admin.add_view(BaseSecureView(Page, db, category='Static'))
        admin.add_view(BaseSecureView(Section, db, category='Static'))
        admin.add_view(BaseSecureView(List, db, category='Static'))
        admin.add_view(BaseSecureView(ListItem, db, category='Static'))
        admin.add_view(SlugifyAdminView(Article, db, category='Blog'))
        admin.add_view(BaseSecureView(BlogCategory, db, category='Blog'))
        admin.add_view(SlugifyAdminView(Location, db, category='Static'))
        admin.add_view(BaseSecureView(Area, db, category='Static'))



    app.register_blueprint(main)
    return app

if __name__ == '__main__':
    # Setting debug=True activates the auto-reloader
    app = create_app()
    app.run(debug=app.config['FLASK_ENV'] == 'development')