from promo.models import db
from promo.models.base_model import BaseModel

class BaseSection(BaseModel):
    __abstract__ = True

    title = db.Column(db.String(200), nullable=True)
    subtitle = db.Column(db.String(200), nullable=True)
    text = db.Column(db.Text, nullable=True)
    cta_link = db.Column(db.String(255), nullable=True)
    tag = db.Column(db.String(100), nullable=False)
    

    def list_for(self, tag):
        return next((l for l in self.lists if l.tag == tag), None)

    
