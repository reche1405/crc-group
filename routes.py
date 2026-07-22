import math, datetime
from flask import Blueprint, Response, request, session, current_app, redirect, url_for, flash, render_template, send_from_directory, abort
from flask_login import current_user, login_user

from flask_mailman import EmailMessage
from werkzeug.exceptions import NotFound, BadRequest
from promo.admin.forms.login import LoginForm
from promo.models.user import User
from promo.models.page import Page, Section
from promo.models.list import List, ListItem
from promo.models.area import Area, Location

from promo.models.article import BlogCategory, Article
from promo.models.service import Category, Service
from promo.models.project import Project
from promo.models.review import Review
from promo.models.policy import Policy

from promo.models.media import Media
from promo.extensions.login_manager import login_manager
from promo.extensions.caching import cache
from promo.forms.contact import ContactForm

main = Blueprint("main", __name__)


@main.context_processor
def get_footer():
    cached_links = cache.get('global_site_links')
    
    if cached_links is not None:
        return cached_links
    
    extra_context = {
        'current_year' : datetime.datetime.now().year
    }
    cache.set('global_site_links', extra_context, timeout=86400 )
    return extra_context


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
    projects_data = Project.to_home_json()
    project_count = len(projects_data['items'])
    context = {
        'page' : page,
        'services' : services,
        'projects_data' : projects_data,
        'project_count' : project_count
        
    }
    return render_template('pages/index.html', **context)

@main.route('/contact/', methods=['GET', 'POST'])
def contact():

    form = ContactForm(request.form, meta={'csrf_context': session})

    page = page = Page.get_for_tag('contact')
    context = {
        'page' :page,
        'form' : form
    }
    if request.method == "POST":
        print(form.data)
        if form.validate():
            client_email = form.email.data
            client_name = form.name.data
            client_tel = form.number.data
            message_body = form.message.data
            print(f"MAIL PORT:  {current_app.config['MAIL_PORT']}")
            print(f"MAIL USE SSL:  {current_app.config['MAIL_USE_SSL']}")
            print(f"MAIL USE TLS:   {current_app.config['MAIL_USE_TLS']}")
            #TEMP: Print the form data
            print(f"New contact query from:\n{client_name}\nTel:\n{client_tel}\nResponse Email:\n{client_email}\n\nMessage\n\n{message_body}")
            msg = EmailMessage(
                from_email=current_app.config['MAIL_USERNAME'],
                subject="New Website Contact Query",
                body=f"New contact query from:\n{client_name}\nTel:\n{client_tel}\nResponse Email:\n{client_email}\n\nMessage\n\n{message_body}",
                to=[current_app.config['INBOUND_MAIL']],

                
            )
            try:
                
                msg.send(fail_silently=False)

                print("Message sent successfully, we will respond within 2 business days..")
                flash("Message sent successfully, we will respond within 2 business days..", "success")
                return redirect(url_for('main.home'))
            except Exception as e:
                print(f"Email failed to send: {e}")
                flash(f"Email failed  to send. {e}", "error")
               
        else: 
            print("Error parsing form data!!!!")
            for field_name, error_messages in form.errors.items():
                for err in error_messages:
                    print(f"Field [{field_name}]: {err}")
                    flash(f"Field [{field_name}]: {err}")
                        

            return redirect(url_for('main.contact'))       
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
    form = ContactForm(meta={'csrf_context': session})
    if not service:
        #TODO: Add a flash message 
        #TODO: Turn this into a 404
        flash("Unable to locate service.")
        return abort(404)

        return redirect(url_for('main.service_list'))
    context = {
        'service' : service,
        'form' : form
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
    if not project:
        return abort(404)
    carousel = None
    context = {
        'project' : project
    }
    if project.gallery: 
        carousel = project.gallery.to_json()
        context['carousel'] = carousel
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
    if not article: return abort(404)
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


@main.route('/legal/')
def policy_list():
    page = Page.get_for_tag('policies')
    policies =Policy.get_all()
    context = {
        'page' : page,
        'policies' : policies
    }
    return render_template('pages/policty-list.html', **context)

@main.route("/legal/<slug>")
def policy_detail(slug):
    policy = Policy.get_by_slug(slug)
    if not policy: return abort(404)
    other_policies = Policy.query.filter(Policy.id != policy.id).all()

    context = {
        'policy' : policy,
        'other_policies' : other_policies
    }
    return render_template('pages/policy-detail.html', **context)


@main.errorhandler(404)
def error_not_found(e):
    return render_template('error/404.html')





@main.route("/sitemap.txt")
def sitemap():
    base_url = "https://theconservatoryroofconverters.co.uk"
    urls = [
        base_url,
        create_url(base_url, 'services/'),
        create_url(base_url, 'contact/'),
        create_url(base_url, 'projects/'),
        create_url(base_url, 'areas/'),
        create_url(base_url, 'blog/'),
        
    ]
    locations  = Location.get_all()
    policies = Policy.get_all()
    services = Service.get_all()
    projects = Project.get_all()
    articles = Article.get_all()
    for location in locations:
        urls.append(create_url(base_url, f"locations/{location.slug}/"))

    for policy in policies:
        urls.append(create_url(base_url, f"legal/{policy.slug}/"))

    for service in services:
        urls.append(create_url(base_url, f"services/{service.slug}/"))
        for location in locations:
            urls.append(create_url(base_url, f"services/{service.slug}/{location.slug}/"))

    for project in projects:
        urls.append(create_url(base_url, f'projects/{project.slug}/'))

    for article in articles:
        urls.append(create_url(base_url, f'blog/{article.slug}/'))

    sitemap_content = "\n".join(urls)
    return Response(sitemap_content, mimetype="text/plain")

def create_url(base, relative):
    return f"{base}/{relative}"



@main.route("/robots.txt")
def robots():
    content_str = """User-aagent: *
Disallow: /admin/
Disallow: /login/
Sitemap: https://therokgroup.co.uk/sitemap.txt
"""
    return Response(content_str, mimetype="text/plain")
