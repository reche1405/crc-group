import os, datetime
from promo.models.list import List, ListItem
from promo.models.service import Service
from promo.models.area import area, location

list_data = [
    {
        "tag" : "welcome-cards",
        "items" : [
            {
                "order" : 0, 
                "text" : "Quality Workmanship",
                "subtext" : "We take pride in our work at conservatory roof renovations",
                "svg" : ""
            },
            {
                "order" : 1, 
                "text" : "Finance Options",
                "subtext" : "Don't break the bank! We offer financing plans on all of our services.",
                "svg" : ""
            },
            {
                "order" : 2,
                "text" : "Free Quotes",
                "subtext" : "Totally free. No strings attached on site visits and quotations.",
                "svg" : ""
            }
        ]
    },
    
]