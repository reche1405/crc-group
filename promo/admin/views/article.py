from .base_secure import SlugifyAdminView
class ArticleAdminView(SlugifyAdminView):
    column_exclude_list = ['body_one', 'body_two', 'body_three', 'abstract', 'subtitle', 'created_at', 'updated_at']
    form_excluded_columns = ['slug']