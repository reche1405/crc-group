from flask import Blueprint, request, session, current_app, redirect, url_for, flash, render_template
from flask_login import current_user, login_user
from promo.admin.forms.login import LoginForm
from promo.models.user import User
from promo.extensions.login_manager import login_manager


main = Blueprint("main", __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))


@main.route('/login', methods=['GET', 'POST'])
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
    pass

@main.route('/contact')
def contact():
    pass

@main.route('/about')
def about():
    pass

@main.route('/services')
def service_list():
    pass

@main.route('/services/<string:slug>')
def service_detail(slug):
    pass

@main.route('/projects')
def project_list():
    pass


@main.route('/projects/<string:slug>')
def project_detail(slug):
    pass

@main.route('/locations')
def location_list():
    pass


@main.route('/locations/<string:slug>')
def location_detail(slug):
    pass