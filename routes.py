import math
from flask import Blueprint, request, session, current_app, redirect, url_for, flash, render_template, send_from_directory, abort
from flask_login import current_user, login_user
from promo.admin.forms.login import LoginForm
from promo.models.user import User
from promo.models.page import Page, Section
from promo.models.list import List, ListItem

from promo.models.article import BlogCategory, Article
from promo.models.service import Category, Service
from promo.models.project import Project
from promo.models.review import Review

from promo.models.media import Media
from promo.extensions.login_manager import login_manager


main = Blueprint("main", __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))


@main.route('/login/', methods=['GET', 'POST'])
def login():
    # 1. If they are already logged in, send them straight to the admin panel
    if current_user.is_authenticated and current_user.is_admin:
        return redirect(url_for('admin.index'))

    form = LoginForm(request.form, meta={'csrf_context': session})

    # 2. Handle form submission
    if form.validate():
        # Find user by username
        user : User = User.query.filter_by(username=form.username.data).first()
        
        # Verify user exists and the password hash matches
        if user and user.verify_password(form.password.data):
            # Log the user in with Flask-Login
            login_user(user)
            print(f"Login function executed. Is user authed? {current_user.is_authenticated}")
            # Handle the 'next' query parameter securely (from Flask-Admin/Flask-Login intercepts)
            next_page = request.args.get('next')
            
            # Simple security check to make sure the next page stays on your domain
            if not next_page:
                next_page = url_for('admin.index')
                
            flash('Logged in successfully!', 'success')
            return redirect(next_page)
        
        # Generic error message so malicious entities don't know if username or password was wrong
        flash('Invalid username or password.', 'danger')
        print(f"Login function not successful. Is user authed? {current_user.is_authenticated}")
        
    return render_template('admin/login.html', form=form)


@main.route('/')
def home():

    page = Page.get_for_tag('home')
    for section in page.sections:
        for _list in section.lists:
            print(len(_list.items))
    services = Service.get_home()
    context = {
        'page' : page,
        'services' : services
        
    }
    return render_template('pages/index.html', **context)

@main.route('/contact/')
def contact():
    page = {
        'tag' : 'contact',
        'body_title' : 'Contact Us',
        'title' : 'Contact CRC Group',
        'body_intro' : 'We are The Conservatory Roof Convrersion Group. And our specialism is in the name. We offer premium external space installations and conversions.'
    }
    context = {
        'page' :page,
    }
    return render_template('pages/contact.html', **context)

@main.route('/about/')
def about():

    page = Page.get_for_tag('about')
    reviews = Review.get_all()
    context = {
        'page' :page,
        'reviews' : reviews

    }
    return render_template('pages/about.html', **context)

@main.route('/services/')
def service_list():
    page = Page.get_for_tag('services')

    
    services = Service.get_home()
    context = {
        'page' : page,
        'services' : services
    }
    return render_template('pages/service-list.html', **context)

      

@main.route('/services/<string:slug>/')
def service_detail(slug):
    service = Service.get_by_slug(slug)

    if not service:
        #TODO: Add a flash message 
        #TODO: Turn this into a 404

        return redirect(url_for('main.service_list'))
    context = {
        'service' : service
    }
    return render_template('pages/service-detail.html', **context)
    

@main.route('/projects/')
def project_list():
    page = Page.get_for_tag('projects')
    projects = Project.get_featured()
    context = {
        'page' : page,
        'projects' : projects
    } 
    return render_template('pages/project-list.html', **context)


@main.route('/projects/<string:slug>/')
def project_detail(slug):
    project = Project.get_by_slug(slug)
    context = {
        'project' : project
    }
    return render_template('pages/project-detail.html', **context)

@main.route('/locations/')
def location_list():
    pass


@main.route('/locations/<string:slug>/')
def location_detail(slug):
    pass

@main.route('/blog/')
def article_list():
    page_no = request.args.get('page')
    page_no = 1 if page_no is  None else int(page_no)
    per_page = 6


    article_count = max(1,Article.count())

    _page_count = article_count / per_page
    if _page_count < 1:
        _page_count = 1
    elif _page_count % 1 != 0:
        _page_count = math.floor(_page_count + 1)
    else: 
        _page_count = int(_page_count) 
    page_count = _page_count
    print(f"Page Count: {page_count}")
    has_prev = True if page_no > 1 else False
    prev_page_no = page_no - 1 if page_no > 1 else None

    has_next = True if page_no + 1 <= page_count else False
    next_page_no = page_no + 1 if page_no + 1 <= page_count else None
    print(f"Page Number: {page_no}\nHas Next: {has_next}\n Next Page: {next_page_no}")
    context = {
        'articles' : Article.get_page(page=page_no, items_per_page=per_page),
        'page_no' : page_no,
        'page_count' : page_count,
        'has_prev' : has_prev,
        'prev_page_no' : prev_page_no,
        'has_next' : has_next,
        'next_page_no' : next_page_no,
        'page' : Page.get_for_tag('blog'),
        'categories' : BlogCategory.get_all()
        

    }
    return render_template("pages/article-list.html", **context)

@main.route('/blog/<string:slug>/')
def article_detail(slug):
    article = Article.get_by_slug(slug)
    context = {
        'article': article
    }
    return render_template('pages/article-detail.html', **context)


@main.route("/media/<string:rel_path>")
def serve_media(rel_path):
    media_item = Media.query.filter_by(relative_path=rel_path).first()
    if not media_item:
        return abort(404)
    path = current_app.config['UPLOAD_PATH']
    
    # 3. Stream the file securely
    try:
        return send_from_directory(path, rel_path)
    except FileNotFoundError:
        return abort(404)


