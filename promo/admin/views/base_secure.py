import os, io
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import  redirect, url_for, request
from slugify import slugify

class BaseSecureView(ModelView):
    
    def is_accessible(self):
        # Only allow access if the user is authenticated
        # Pro tip: If your User model has an 'is_admin' field, check it here: 
        # return current_user.is_authenticated and current_user.is_admin
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # Redirect logged-out users straight to your custom login view.
        # request.url ensures the user is sent back here after typing their password.

        return redirect(url_for('main.login', next=request.url))
    
class SlugifyAdminView(BaseSecureView):
    form_excluded_columns = ['slug']

    def on_model_change(self, form, model, is_created):
        super().on_model_change(form, model, is_created)
        if model.title:
            model.slug = slugify(model.title)

