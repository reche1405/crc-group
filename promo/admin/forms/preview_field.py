
from .preview_widget import ImagePreviewWidget
from flask_admin.form import FileUploadField

class PreviewFileUploadField(FileUploadField):
    widget = ImagePreviewWidget()