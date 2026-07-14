import os, datetime
from promo.models import db
from promo.models.list import List, ListItem
from promo.models.service import Category, Service, ServiceSection
from promo .models.project import ProjectTag, Project
from promo.models.review import Review
from promo.models.page import Page, Section
from promo.models.article import BlogCategory, Article
from app import create_app
category_data = [
    {"title" : "Commercial"},
    {"title" : "Residential"},
    {"title" : "Commercial & Residential"},
]
page_data = [
    {
        'tag': 'home',
        'title': 'Welcome | CRC Group',
        'description': (
            "CRC Group specialises in premium conservatory roof conversions and "
            "external space transformations. We help homeowners create comfortable, "
            "energy‑efficient living spaces that can be enjoyed all year round."
        ),
        'keywords': (
            "conservatory roof conversion, conservatory insulation, warm roof systems, "
            "home extensions, CRC Group, conservatory upgrades, external space renovation"
        ),
        'body_title': 'Welcome to CRC Group',
        'body_intro': (
            "We are The Conservatory Roof Conversion Group. Our specialism is in the name. "
            "We offer premium external space installations and conversions, helping you "
            "transform your conservatory into a comfortable, usable room throughout the year."
        )
    
    },
    
    {
        'tag': 'about',
        'title': 'About Us | CRC Group',
        'description': (
            "Learn about CRC Group, a specialist provider of premium conservatory roof "
            "conversions and external space transformations. Our team is committed to "
            "craftsmanship, energy efficiency, and long‑lasting home improvements."
        ),
        'keywords': (
            "about CRC Group, conservatory specialists, roof conversion experts, "
            "home improvement company, warm roof installers"
        ),
        'body_title': 'About CRC Group',
        'body_intro': (
            "CRC Group was founded with a simple mission: to transform conservatories into "
            "comfortable, energy‑efficient living spaces. Our team brings years of experience, "
            "precision workmanship, and a commitment to delivering exceptional results."
        )
    },

    {
        'tag': 'services',
        'title': 'Our Services | CRC Group',
        'description': (
            "Explore CRC Group’s range of premium services including conservatory roof "
            "conversions, insulated warm roofs, and external space transformations."
        ),
        'keywords': (
            "CRC Group services, conservatory roof conversion services, warm roof installation, "
            "external space renovation, conservatory upgrades"
        ),
        'body_title': 'Our Services',
        'body_intro': (
            "We offer a comprehensive range of premium home improvement services designed to "
            "enhance comfort, efficiency, and the overall quality of your living space."
        )
    },
    
    {
        'tag': 'projects',
        'title': 'Our Projects | CRC Group',
        'description': (
            "View completed conservatory roof conversions and home improvement projects by "
            "CRC Group. See real transformations and the quality of our craftsmanship."
        ),
        'keywords': (
            "CRC Group projects, conservatory roof conversion examples, home renovation gallery, "
            "before and after conservatory upgrades"
        ),
        'body_title': 'Our Projects',
        'body_intro': (
            "Take a look at some of the transformations we've delivered for homeowners across "
            "the region. Each project showcases our attention to detail, craftsmanship, and "
            "commitment to creating comfortable, energy‑efficient spaces."
        )
    },

     {
        'tag': 'blog',
        'title': 'Blog & Insights | CRC Group',
        'description': (
            "Explore articles, guides, and insights from CRC Group on conservatory roof "
            "conversions, insulation, home improvement trends, and energy‑efficient living."
        ),
        'keywords': (
            "CRC Group blog, conservatory roof guides, home improvement tips, "
            "warm roof articles, energy efficiency advice"
        ),
        'body_title': 'CRC Group Blog',
        'body_intro': (
            "Discover insights, tips, and expert guidance on conservatory conversions, "
            "insulation solutions, and creating comfortable living spaces all year round."
        )
    },
    

    {
        'tag': 'contact',
        'title': 'Contact Us | CRC Group',
        'description': (
            "Get in touch with CRC Group for enquiries, quotes, or advice on conservatory "
            "roof conversions and external space improvements. We're here to help."
        ),
        'keywords': (
            "contact CRC Group, conservatory roof quote, home improvement enquiries, "
            "speak to CRC Group, conservatory conversion advice"
        ),
        'body_title': 'Contact Us',
        'body_intro': (
            "Whether you're looking for a quote, have questions about our services, or want "
            "expert guidance on your conservatory transformation, our team is ready to help."
        )
    },
    
   
  
]

section_data = [
    {
        'page_id': 1, 
        'title': '',
        'subtitle': '',
        'text': "",
        'tag' : 'welcome-section'
    },
    {
        'page_id': 1, 
        'title': 'Expert Exterior Space Development',
        'subtitle': 'ABOUT CRC GROUP',
        'text': "We provide thermal regulation for your outside spaces so that you can enjoy them year round. Keep optimal lighting and temprature, while maximising value on your property.",
        'tag' : 'home-about'
    }, 
    {
        'page_id' : 1, 
        'title' : "Our Project Excellence",
        'subtitle' : "OUR FEATURED WORKS",
        'tag' : 'home-featured-projects'
    },
    {
        'page_id' : 1, 
        'title' : 'We Convert Conservatories of All Shapes & Sizes!',
        'subtitle' : 'COMPATIBLE VARIATIONS',
        'tag' : 'home-compatible',
    },
    {
        'page_id' : 2, 
        'title' : 'The People Behind the Company',
        'subtitle' : 'ABOUT CRC',
        'text' : "Construction is the process of planning, designing, and building infrastructure such as residential homes, commercial buildings, roads, bridges, and industrial facilities. It involves the coordination of skilled labor.",
        'tag' : 'about-the-company'
    },
    {
        'page_id' : 2,
        'title': 'What Our Clients Have To Say',
        'subtitle': 'OUR CLIENT REVIEWS',
        'text' : "Don't listen to us, here's some feedback from our happy customers...",
        'tag' : 'about-reviews'
    },
    {
        'page_id' : 3,
        'title': 'Your Trusted Extensions Partner.',
        'subtitle': 'WHY CHOOSE US',
        'text' : "We beleive that every build is unique, and our approach keeps that in mind.",
        'tag': 'services-why-us', 
    },
    {
        'page_id' : 3,
        'title': 'Our Construction Work Process',
        'subtitle': 'OUR PROCESS',
        'text' : "From brief to handover, we have a four point process that adhere to.",
        'tag': 'services-process', 
    },
    {
        'page_id' : 6,
        'title': "Let's Talk!",
        'subtitle': 'START YOUR JOUNEY',
        'text' : "",
        'tag': 'contact-talk', 
    },
    {
        'page_id' : 2,
        'title': 'What Sets us Apart from Other Solutions?',
        'subtitle': 'COMPARISON CHART',
        'text' : "See why customers nationwide are choosing conservatory roof converters over alternative solutions.",
        'tag' : 'about-compare'
    },

]

service_data = [
    {
        'title' : 'Conservatory Roofs',
        'short_desc' : "We utilise modern state of the art tiling solutions to maximise your conservatories light and tempature stabilisation, Allowing comfort all-year round.",
        'slug': 'conservatory-roofs',
        'desc': "If you love the natural light of your conservatory but find it practically unusable—becoming a greenhouse in the peak of summer and a freezing icebox throughout the winter—you are not alone. Traditional glass or polycarbonate roofs simply cannot handle the extreme seasonal shifts of the UK climate.\n"
        "Our premium conservatory roof conversion service completely resolves this issue. By replacing your outdated roof with advanced Eurocell Equinox tiled roofing technology, we transform your conservatory from an underutilised seasonal room into a seamless, high-performance extension of your home.\n",
        "category_id" : 3,
        "is_featured" : True
    },
    {
        'title' : 'Garden Rooms',
        'short_desc' : "We convert open spaces into fully functioning exterior buildings, with functioning electricity and gas, and a regulated temprature all yar round.",
        'slug': 'garden-rooms',
        'desc': "If you love the natural light of your conservatory but find it practically unusable—becoming a greenhouse in the peak of summer and a freezing icebox throughout the winter—you are not alone. Traditional glass or polycarbonate roofs simply cannot handle the extreme seasonal shifts of the UK climate.\n"
        "Our premium conservatory roof conversion service completely resolves this issue. By replacing your outdated roof with advanced Eurocell Equinox tiled roofing technology, we transform your conservatory from an underutilised seasonal room into a seamless, high-performance extension of your home.\n",
        "category_id" : 3,
        "is_featured" : True
    },
    {
        'title' : 'Interior Design',
        'short_desc' : "Feel as good on the inside as you do on the out! Interior redesigns to match your premium new exterior spaces. From Painting & Decorating to Furnishing.",
        'slug': 'interior-design',
        'desc': "If you love the natural light of your conservatory but find it practically unusable—becoming a greenhouse in the peak of summer and a freezing icebox throughout the winter—you are not alone. Traditional glass or polycarbonate roofs simply cannot handle the extreme seasonal shifts of the UK climate."
        "Our premium conservatory roof conversion service completely resolves this issue. By replacing your outdated roof with advanced Eurocell Equinox tiled roofing technology, we transform your conservatory from an underutilised seasonal room into a seamless, high-performance extension of your home.",
        "category_id" : 3,
        "is_featured" : True
    },
]

service_intro_lists = [
    {
        # Conservatory Roofs
        'service_id': 1,
        'items' : [
            {
                'order' : 0,
                'text': 'Tailored Roof Designs'
            },
            {
                'order' : 1,
                'text': 'Full Weather Protection'
            }
        ]
    },
    {
        # Garden Rooms
        'service_id': 2,
        'items' : [
            {
                'order' : 0,
                'text': 'Gas And Electric Intstalled'
            },
            {
                'order' : 1,
                'text': 'Totally Customisable'
            }
        ]
    },
    {
        # Interior Design
        'service_id': 3,
        'items' : [
            {
                'order' : 0,
                'text': 'Flexible Design Team'
            },
            {
                'order' : 1,
                'text': 'Free Consultation'
            }
        ]
    }
]

service_section_data = [
    {
        'service_id': 1, 
        'tag': 'conservatory-roofs-faq',
        'title': 'FAQ',
        'list': {
            'tag': 'conservatory-roofs-faq-questions',
            'items': [
                {
                    'order' : 0,
                    'text': 'How long does installation take?',
                    'subtext': "We are entirely flexible around your schedule.\n"
                    "We can have have construction complete in as little as two working days!\n" 
                    "So that you can minimise the headache of installation."
                },
                {
                    'order' : 1,
                    'text': 'What is the price for a quotation?', 
                    'subtext': "We offer <b>FREE</b>, no strings attached quotes on all new projects.\n"

                    "Don't get locked in with cowboy traders that will lock you in to a contract. Contact a name you can trust!"
                },
                {
                    'order' : 2,
                    'text': 'Do I have to pay upfront?',
                    'subtext': 'Avoid financial burden! We offer a variety of affordable payment plans on our services.\n'
                    "Pick the plan that suites you, including upfront, short term payment plans and long term payment plans,\n"
                    "<span class='smaller-text mt-3'>Short Term: 3 - 6 Months | Long Term: 12 - 48 Months</span>"
                }
            ]
        
        },
    },
    {
        'service_id': 1, 
        'tag': 'conservatory-roofs-how',
        'title': 'How It Works',
        'list' : {
            'tag': 'conservatory-roofs-render',
            'items' : [
                {
                    'order' : 0,
                    'text': 'CHOICE OF TILES',
                    'subtext': 'AND COLOURS',
                    'svg' : '20,50'
                },
                {
                    'order' : 1,
                    'text': 'FULL GLAZING PANEL &amp; ROOF WINDOW OPTIONS',
                    'subtext': 'NOW AVAILABLE',
                    'svg' : '90,45'
                },
                {
                    'order' : 2,
                    'text': '0.15*',
                    'subtext': 'U-VALUE',
                    'svg' : '155,5'
                },
                {
                    'order' : 2,
                    'text': 'FULLY VENTILATED',
                    'subtext': 'ROOF SYSTEM',
                    'svg' : '205,95'
                },

            ]
            
        }
    },
    {
        'service_id': 2, 
        'tag': 'garden-rooms-faq',
        'title': 'FAQ',
        'list': {
            'tag': 'garden-rooms-faq-questions',
            'items': [
                {
                    'order' : 0,
                    'text': 'How long does installation take?',
                    'subtext': "We are entirely flexible around your schedule.\n"
                    "We can have have construction complete in as little as two working days!\n" 
                    "So that you can minimise the headache of installation."
                },
                {
                    'order' : 1,
                    'text': 'What is the price for a quotation?', 
                    'subtext': "We offer <b>FREE</b>, no strings attached quotes on all new projects.\n"

                    "Don't get locked in with cowboy traders that will lock you in to a contract. Contact a name you can trust!"
                },
                {
                    'order' : 2,
                    'text': 'Do I have to pay upfront?',
                    'subtext': 'Avoid financial burden! We offer a variety of affordable payment plans on our services.\n'
                    "Pick the plan that suites you, including upfront, short term payment plans and long term payment plans,\n"
                    "<span class='smaller-text mt-3'>Short Term: 3 - 6 Months | Long Term: 12 - 48 Months</span>"
                }
            ]
        
        },
    },
    {
        'service_id': 3, 
        'tag': 'interior-design-faq',
        'title': 'FAQ',
        'list': {
            'tag': 'interior-design-faq-questions',
            'items': [
                {
                    'order' : 0,
                    'text': 'How long does installation take?',
                    'subtext': "We are entirely flexible around your schedule.\n"
                    "We can have have construction complete in as little as two working days!\n" 
                    "So that you can minimise the headache of installation."
                },
                {
                    'order' : 1,
                    'text': 'What is the price for a quotation?', 
                    'subtext': "We offer <b>FREE</b>, no strings attached quotes on all new projects.\n"

                    "Don't get locked in with cowboy traders that will lock you in to a contract. Contact a name you can trust!"
                },
                {
                    'order' : 2,
                    'text': 'Do I have to pay upfront?',
                    'subtext': 'Avoid financial burden! We offer a variety of affordable payment plans on our services.\n'
                    "Pick the plan that suites you, including upfront, short term payment plans and long term payment plans,\n"
                    "<span class='smaller-text mt-3'>Short Term: 3 - 6 Months | Long Term: 12 - 48 Months</span>"
                }
            ]
        
        },
    },
]

project_data = [
    {
        'title': "St Anthony's Conversion",
        'slug': 'st-anthonys-conversion',
        'customer_name': 'Joan Phoenix',
        'short_desc' : "Lorem Ipsum Dolar Amet some other stuff that goes in here.!",
        'service_id' : 1,
        'is_featured' : True,

    },
    {
        'title': "Stones Cross Garden Room",
        'slug': 'stones-cross-garden-room',
        'customer_name': 'Andy Belton',
        'short_desc' : "Lorem Ipsum Dolar Amet some other stuff that goes in here.!",
        'service_id' : 2,
        'is_featured' : True,
        
    },
    {
        'title': "Rother Redesign",
        'slug': 'rother-redesign',
        'customer_name': 'Pete & Wendy Jones',
        'short_desc' : "Lorem Ipsum Dolar Amet some other stuff that goes in here.!",
        'service_id' : 3,
        'is_featured' : True,
        
    },
]
review_data = [
    {
        'project_id' : 1,
        'text': "Couldn't be happier with my conservatory. CRC Group were professional, respectable, and efficient throughout the process.",
        'rating' : 5
    },
    {
        'project_id' : 2,
        'text': "We decided to go for a full garden room instead of a summer house. There's truly no looking back! Feels like we've added another room to the house.",
        'rating' : 5
    },
    {
        'project_id': 3, 
        'text' : 'Pleasantly suprised with the finish. The rendering and lighting fixtures really bring the room together.',
        'rating' : 5
    }
]

list_data = [
    {
        "tag" : "welcome-cards",
        "section_id" : 1,
        "items" : [
            {
            "order" : 0, 
            "text" : "Quality Workmanship",
            "subtext" : "We take pride in our work at conservatory roof renovations",
            "svg" : f'''
                
            <svg width="50px" height="50px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path opacity="0.5" d="M12.0006 16C6.2407 16 5.22032 10.2595 5.03956 5.70647C4.98928 4.43998 4.96414 3.80673 5.43985 3.22083C5.91557 2.63494 6.48494 2.53887 7.62367 2.34674C8.74773 2.15709 10.2171 2 12.0006 2C13.7842 2 15.2536 2.15709 16.3776 2.34674C17.5163 2.53887 18.0857 2.63494 18.5614 3.22083C19.0371 3.80673 19.012 4.43998 18.9617 5.70647C18.781 10.2595 17.7606 16 12.0006 16Z" fill="#bbbbbb"/>
                <path d="M17.6404 12.422L20.4569 10.8572C21.2093 10.4392 21.5855 10.2302 21.7927 9.87809C21.9999 9.52598 21.9999 9.09561 21.9999 8.23487L21.9999 8.16234C22 7.11873 22 6.59692 21.7168 6.20408C21.4337 5.81124 20.9387 5.64623 19.9486 5.31621L19 5L18.9831 5.08464C18.9784 5.27391 18.9702 5.48006 18.9612 5.70645C18.8729 7.93085 18.5842 10.4387 17.6404 12.422Z" fill="#bbbbbb"/>
                <path d="M5.03907 5.70647C5.12739 7.93096 5.41612 10.4389 6.36008 12.4223L3.54305 10.8572C2.79063 10.4392 2.41442 10.2302 2.20723 9.87809C2.00004 9.52598 2.00003 9.09561 2 8.23487L2 8.16234C1.99997 7.11874 1.99996 6.59692 2.2831 6.20408C2.56624 5.81124 3.06126 5.64623 4.05132 5.31621L4.99994 5L5.01728 5.08671C5.02196 5.27541 5.03011 5.4809 5.03907 5.70647Z" fill="#bbbbbb"/>
                <path fill-rule="evenodd" clip-rule="evenodd" d="M5.25 22C5.25 21.5858 5.58579 21.25 6 21.25H18C18.4142 21.25 18.75 21.5858 18.75 22C18.75 22.4142 18.4142 22.75 18 22.75H6C5.58579 22.75 5.25 22.4142 5.25 22Z" fill="#ffd82d"/>
                <path opacity="0.5" d="M15.4582 21.25H8.54297L8.83979 19.5002C8.93327 19.0327 9.34368 18.6963 9.82037 18.6963H14.1808C14.6574 18.6963 15.0679 19.0327 15.1613 19.5002L15.4582 21.25Z" fill="#ffd82d"/>
                <path d="M12.0002 16.0002C11.7406 16.0002 11.4907 15.9885 11.25 15.9658V18.6963H12.75V15.9658C12.5094 15.9885 12.2596 16.0002 12.0002 16.0002Z" fill="#ffd82d"/>
                <path d="M11.1459 6.02251C11.5259 5.34084 11.7159 5 12 5C12.2841 5 12.4741 5.34084 12.8541 6.02251L12.9524 6.19887C13.0603 6.39258 13.1143 6.48944 13.1985 6.55334C13.2827 6.61725 13.3875 6.64097 13.5972 6.68841L13.7881 6.73161C14.526 6.89857 14.895 6.98205 14.9828 7.26432C15.0706 7.54659 14.819 7.84072 14.316 8.42898L14.1858 8.58117C14.0429 8.74833 13.9714 8.83191 13.9392 8.93531C13.9071 9.03872 13.9179 9.15023 13.9395 9.37327L13.9592 9.57632C14.0352 10.3612 14.0733 10.7536 13.8435 10.9281C13.6136 11.1025 13.2682 10.9435 12.5773 10.6254L12.3986 10.5431C12.2022 10.4527 12.1041 10.4075 12 10.4075C11.8959 10.4075 11.7978 10.4527 11.6014 10.5431L11.4227 10.6254C10.7318 10.9435 10.3864 11.1025 10.1565 10.9281C9.92674 10.7536 9.96476 10.3612 10.0408 9.57632L10.0605 9.37327C10.0821 9.15023 10.0929 9.03872 10.0608 8.93531C10.0286 8.83191 9.95713 8.74833 9.81418 8.58117L9.68403 8.42898C9.18097 7.84072 8.92945 7.54659 9.01723 7.26432C9.10501 6.98205 9.47396 6.89857 10.2119 6.73161L10.4028 6.68841C10.6125 6.64097 10.7173 6.61725 10.8015 6.55334C10.8857 6.48944 10.9397 6.39258 11.0476 6.19887L11.1459 6.02251Z" fill="#ffd82d"/>
            </svg>
'''
        },
        {
            "order" : 1, 
            "text" : "Finance Options",
            "subtext" : "Don't break the bank! We offer financing plans on all of our services.",
            "svg" : '''
                <svg width="50px" height="50px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path opacity="0.5" d="M7.24502 2H16.755C17.9139 2 18.4933 2 18.9606 2.16261C19.8468 2.47096 20.5425 3.18719 20.842 4.09946C21 4.58055 21 5.17705 21 6.37006V20.3742C21 21.2324 20.015 21.6878 19.3919 21.1176C19.0258 20.7826 18.4742 20.7826 18.1081 21.1176L17.625 21.5597C16.9834 22.1468 16.0166 22.1468 15.375 21.5597C14.7334 20.9726 13.7666 20.9726 13.125 21.5597C12.4834 22.1468 11.5166 22.1468 10.875 21.5597C10.2334 20.9726 9.26659 20.9726 8.625 21.5597C7.98341 22.1468 7.01659 22.1468 6.375 21.5597L5.8919 21.1176C5.52583 20.7826 4.97417 20.7826 4.6081 21.1176C3.985 21.6878 3 21.2324 3 20.3742V6.37006C3 5.17705 3 4.58055 3.15795 4.09946C3.45748 3.18719 4.15322 2.47096 5.03939 2.16261C5.50671 2 6.08614 2 7.24502 2Z" fill="#cccccc"/>
                    <path d="M15.0595 8.49952C15.3353 8.19054 15.3085 7.71643 14.9995 7.44055C14.6905 7.16468 14.2164 7.19152 13.9405 7.5005L10.9286 10.8739L10.0595 9.9005C9.78358 9.59152 9.30947 9.56468 9.00049 9.84055C8.69151 10.1164 8.66467 10.5905 8.94055 10.8995L10.3691 12.4995C10.5114 12.6589 10.7149 12.75 10.9286 12.75C11.1422 12.75 11.3457 12.6589 11.488 12.4995L15.0595 8.49952Z" fill="#ffd82d"/>
                    <path d="M7.5 14.75C7.08579 14.75 6.75 15.0858 6.75 15.5C6.75 15.9142 7.08579 16.25 7.5 16.25H16.5C16.9142 16.25 17.25 15.9142 17.25 15.5C17.25 15.0858 16.9142 14.75 16.5 14.75H7.5Z" fill="#eeeeee"/>
                </svg>
            '''
            
        },
        {
            "order" : 2,
            "text" : "Free Quotes",
            "subtext" : "Totally free. No strings attached on site visits and quotations.",
            "svg" : '''
                <svg width="50px" height="50px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M21.5315 11.5857L20.75 10.9605V21.25H22C22.4142 21.25 22.75 21.5858 22.75 22C22.75 22.4143 22.4142 22.75 22 22.75H2.00003C1.58581 22.75 1.25003 22.4143 1.25003 22C1.25003 21.5858 1.58581 21.25 2.00003 21.25H3.25003V10.9605L2.46855 11.5857C2.1451 11.8445 1.67313 11.792 1.41438 11.4686C1.15562 11.1451 1.20806 10.6731 1.53151 10.4144L9.65742 3.91366C11.027 2.818 12.9731 2.818 14.3426 3.91366L22.4685 10.4144C22.792 10.6731 22.8444 11.1451 22.5857 11.4686C22.3269 11.792 21.855 11.8445 21.5315 11.5857ZM12 6.75004C10.4812 6.75004 9.25003 7.98126 9.25003 9.50004C9.25003 11.0188 10.4812 12.25 12 12.25C13.5188 12.25 14.75 11.0188 14.75 9.50004C14.75 7.98126 13.5188 6.75004 12 6.75004ZM13.7459 13.3116C13.2871 13.25 12.7143 13.25 12.0494 13.25H11.9507C11.2858 13.25 10.7129 13.25 10.2542 13.3116C9.76255 13.3777 9.29128 13.5268 8.90904 13.9091C8.52679 14.2913 8.37773 14.7626 8.31163 15.2542C8.24996 15.7129 8.24999 16.2858 8.25003 16.9507L8.25003 21.25H9.75003H14.25H15.75L15.75 16.9507L15.75 16.8271C15.7498 16.2146 15.7462 15.6843 15.6884 15.2542C15.6223 14.7626 15.4733 14.2913 15.091 13.9091C14.7088 13.5268 14.2375 13.3777 13.7459 13.3116Z" fill="#666666"/>
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M10.75 9.5C10.75 8.80964 11.3096 8.25 12 8.25C12.6904 8.25 13.25 8.80964 13.25 9.5C13.25 10.1904 12.6904 10.75 12 10.75C11.3096 10.75 10.75 10.1904 10.75 9.5Z" fill="#ffd82d"/>
                    <g opacity="0.5">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M10.75 9.5C10.75 8.80964 11.3096 8.25 12 8.25C12.6904 8.25 13.25 8.80964 13.25 9.5C13.25 10.1904 12.6904 10.75 12 10.75C11.3096 10.75 10.75 10.1904 10.75 9.5Z" fill="#ffd82d"/>
                    </g>
                    <path  d="M12.0494 13.25C12.7142 13.25 13.2871 13.2499 13.7458 13.3116C14.2375 13.3777 14.7087 13.5268 15.091 13.909C15.4732 14.2913 15.6223 14.7625 15.6884 15.2542C15.7462 15.6842 15.7498 16.2146 15.75 16.827L15.75 21.25H8.25L8.25 16.9506C8.24997 16.2858 8.24993 15.7129 8.31161 15.2542C8.37771 14.7625 8.52677 14.2913 8.90901 13.909C9.29126 13.5268 9.76252 13.3777 10.2542 13.3116C10.7129 13.2499 11.2858 13.25 11.9506 13.25H12.0494Z" fill="#444444"/>
                    <path opacity="0.5" d="M16 3H18.5C18.7761 3 19 3.22386 19 3.5L19 7.63955L15.5 4.83955V3.5C15.5 3.22386 15.7239 3 16 3Z" fill="#1C274C"/>
                </svg>
            '''
        }

        ]
    },
    
    {
        'tag' : 'home-mission',
        'section_id' : 2,
        'title': 'Mission',
        'description': 'Our mission is to ensure that every customer is satisfied that they are making the most of their external spaces.',
        'items': [
            {
                "text": "Project Pride",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "98% Happy Customers",
                "order" : 1, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',         
            },
            
        ]
    },

    {
        'tag' : 'home-vision',
        'section_id' : 2,
        'title': 'Vision',
        'description': 'Our vision is to be the most trusted impactful extension specialists in the south east, known for transforming external spaces.',
        'items': [
            {
                "text": "South East Coverage",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "24/7 Contact Support",
                "order" : 1, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',         
            },
            
        ]
    },

    {
        'tag' : 'home-values',
        'section_id' : 2,
        'title': 'Values',
        'description': 'At CRC, we have three core values. We value commitment, pride in our work, and economic efficiency in our trade.',
        'items': [
            {
                "text": "Free Quotes",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "Payment Plans Available",
                "order" : 1, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',         
            },
            
        ]
    },

    {
        "tag" : "con-shapes",
        "section_id" : 4,
        "items" : [
        {
            "text": "Victorian",
            "order":0,
            "subtext": "A classic design featuring a faceted, curved bay front, a steep roof, and ornate ridge details that deliver traditional British elegance.",
            "svg" : '''
                              
                <svg width="243.88751" height="184.9209" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1"><linearGradient id="linearGradient70"><stop style="stop-color:#6dabcf;stop-opacity:1;" offset="0" id="stop67" /><stop style="stop-color:#5fb0e6;stop-opacity:0.50588232;" offset="0.45308921" id="stop68" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop70" /></linearGradient><pattern xlink:href="#Strips1_5" preserveAspectRatio="xMidYMid" id="pattern67" patternTransform="matrix(0,0.1,-0.1,0,0,0)" x="0" y="0" /><pattern patternUnits="userSpaceOnUse" width="6" height="1" patternTransform="translate(0,0) scale(2,2)" preserveAspectRatio="xMidYMid" id="Strips1_5" style="fill:#000000">&#10;      <rect style="stroke:none" x="0" y="-0.5" width="1" height="2" id="rect164" />&#10;    </pattern><linearGradient id="linearGradient64"><stop style="stop-color:#a3c9e1;stop-opacity:1;" offset="0" id="stop61" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop62" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop63" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop64" /></linearGradient><linearGradient id="linearGradient60"><stop style="stop-color:#8cbed9;stop-opacity:1;" offset="0" id="stop57" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop58" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop59" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop60" /></linearGradient><pattern xlink:href="#pattern13" preserveAspectRatio="xMidYMid" id="pattern14" patternTransform="matrix(-0.01995129,0.00139513,-0.00139513,-0.01995129,0,0)" x="0" y="0" /><pattern xlink:href="#Bricks" id="pattern13" patternTransform="matrix(0.01995129,0.00139513,-0.00139513,0.01995129,0.42094947,-11.739813)" x="0" y="0" preserveAspectRatio="xMidYMid" /><pattern xlink:href="#Bricks" id="pattern10" patternTransform="scale(0.02)" x="0" y="0" preserveAspectRatio="none" /><pattern patternUnits="userSpaceOnUse" width="100" height="100" id="Bricks" style="fill:#935219" patternTransform="scale(0.25,0.25)"><g id="g13367"><rect style="fill:none;stroke:none;stroke-width:0" id="rect13349" width="100" height="100" x="0" y="0" /><rect style="fill-opacity:1;stroke-width:0" id="rect13351" width="40" height="40" x="0" y="60" /><rect style="fill-opacity:1;stroke-width:0" id="rect13353" width="90" height="40" x="0" y="10" /><rect style="fill-opacity:1;stroke-width:0" id="rect13355" width="50" height="40" x="50" y="60" /></g></pattern><linearGradient xlink:href="#linearGradient60" id="linearGradient11" x1="167.06261" y1="27.089109" x2="173.57579" y2="31.392151" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient64" id="linearGradient14" gradientUnits="userSpaceOnUse" x1="167.06261" y1="27.089109" x2="173.57579" y2="31.392151" gradientTransform="translate(10.555822,-0.10841814)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient54" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="145.01958" y1="24.0648" x2="148.92474" y2="19.325005" /><linearGradient xlink:href="#linearGradient70" id="linearGradient55" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="152.00311" y1="23.510586" x2="157.09706" y2="17.924889" /><linearGradient xlink:href="#linearGradient70" id="linearGradient56" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="139.66898" y1="34.298935" x2="148.91502" y2="24.094034" /><linearGradient xlink:href="#linearGradient70" id="linearGradient57" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="150.92365" y1="34.486496" x2="160.32947" y2="26.142387" /><linearGradient xlink:href="#linearGradient70" id="linearGradient72" x1="155.09953" y1="28.766298" x2="160.79262" y2="28.766298" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient73" x1="149.03021" y1="28.757526" x2="154.17104" y2="28.757526" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient74" x1="149.03001" y1="20.392658" x2="154.17073" y2="20.392658" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient75" x1="155.09943" y1="19.961107" x2="160.79259" y2="19.961107" gradientUnits="userSpaceOnUse" /></defs><g id="layer2" transform="translate(-142.39713,-1.5863839)"><path style="fill:#968334;fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 198.60245,45.193143 -0.0661,-9.98802 -13.95677,1.124479 v 11.112499 z" id="path76" /><path id="path77" style="fill:#968334;fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 184.58344,43.618976 0.0583,3.696537 h -23.0349 l 0.0187,-5.481645 z" /><path style="fill:#968334;fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 147.79386,45.112527 0.0661,-9.98802 13.95677,1.124479 v 11.112499 z" id="path78" /><path id="path75" style="fill:#42403e;fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 200.79629,15.944435 -16.06221,-1.343101 h -23.66934 l -14.5044,1.343101 27.11797,-10.9746084 z" /><path style="fill:url(#pattern14);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 198.60245,45.193143 -0.0661,-9.98802 -13.95677,1.124479 v 11.112499 z" id="path13" /><path id="rect30" style="fill:url(#pattern10);fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 184.58344,43.618976 0.0583,3.696537 h -23.0349 l 0.0187,-5.481645 z" /><path id="path25" style="fill:url(#pattern67);fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 200.79629,15.944435 -16.06221,-1.343101 h -23.66934 l -14.5044,1.343101 27.11797,-10.9746084 z" /><path id="rect25" style="fill:#302c2a;fill-opacity:1;stroke:none;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 146.64253,15.977569 14.73106,-1.226469 h 23.3848 l 15.81024,1.226469 v 1.546345 l -15.86856,-1.226469 h -23.38479 l -14.67275,1.226469 z" /><rect style="fill:#e5e5e5;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26" width="22.803343" height="27.902233" x="161.83841" y="16.331261" /><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect2" width="10.649479" height="26.127604" x="162.71873" y="16.999477" /><rect style="opacity:0.579137;fill:url(#linearGradient11);fill-opacity:1;stroke:#787666;stroke-width:0.0915985;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27" width="7.9183006" height="23.873291" x="164.11497" y="18.145884" /><path style="fill:url(#pattern13);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 147.79386,45.112527 0.0661,-9.98802 13.95677,1.124479 v 11.112499 z" id="path11" /><rect style="fill:#f6f6f6;fill-opacity:1;stroke:#414141;stroke-width:0.0739189;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29" width="28.63773" height="0.66228044" x="159.07536" y="43.558125" rx="1.3306036" /><path style="fill:none;fill-opacity:1;stroke:#484848;stroke-width:0.349206;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 162.508,13.647747 11.06827,-7.6286199 10.62175,7.7935629" id="path40" /><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect3" width="10.649479" height="26.127604" x="173.30208" y="16.999477" /><rect style="opacity:0.579137;fill:url(#linearGradient14);fill-opacity:1;stroke:#787666;stroke-width:0.0915985;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27-2" width="7.9183006" height="23.873291" x="174.67079" y="18.037466" /><rect style="fill:#e5e5e5;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect4" width="0.52916974" height="26.309505" x="172.93828" y="16.900259" /><path id="rect14" style="fill:#e5e5e5;stroke-width:1.13801;stroke-linecap:square;paint-order:markers fill stroke" d="m 148.26509,17.630418 13.55405,-1.261677 v 19.680735 l -13.55325,-0.769448 z" /><path id="rect28" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 148.77929,18.605389 5.75537,-0.485973 1e-4,4.251266 -5.7553,0.288721 z" /><path id="rect15" style="opacity:0.656;fill:url(#linearGradient74);fill-opacity:1;stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 149.03002,19.04074 5.14062,-0.414267 9e-5,3.253325 -5.14058,0.279045 z" /><path id="rect31" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 154.77794,18.098874 6.36961,-0.537837 1e-5,4.477906 -6.36953,0.319534 z" /><path id="rect16" style="opacity:0.656;fill:url(#linearGradient75);fill-opacity:1;stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 155.09942,18.551626 5.69314,-0.458793 2e-5,3.427512 -5.69309,0.309037 z" /><path id="rect33" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 148.7168,23.217872 5.74904,-0.261403 2.8e-4,11.550378 -5.74884,-0.274199 z" /><path id="rect17" style="opacity:0.656;fill:url(#linearGradient73);fill-opacity:1;stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 149.03022,23.660128 5.14054,-0.213939 2.8e-4,10.622674 -5.14039,-0.22756 z" /><path id="rect32" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 154.77805,22.942272 6.36951,-0.289615 3e-5,12.172873 -6.36927,-0.303791 z" /><path id="rect18" style="opacity:0.656;fill:url(#linearGradient72);fill-opacity:1;stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 155.09953,23.407536 5.69305,-0.236934 4e-5,11.191393 -5.69285,-0.252017 z" /><path id="path34" style="fill:#e5e5e5;stroke-width:1.13801;stroke-linecap:square;paint-order:markers fill stroke" d="m 198.16913,17.630418 -13.55405,-1.261677 v 19.680735 l 13.55325,-0.769448 z" /><path id="path35" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.65494,18.605389 -5.75538,-0.485973 -1e-4,4.251266 5.7553,0.288721 z" /><path id="path36" style="opacity:0.656;fill:url(#linearGradient54);stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.4042,19.04074 -5.14062,-0.414267 -9e-5,3.253325 5.14058,0.279045 z" /><path id="path37" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.65628,18.098874 -6.36961,-0.537837 -10e-6,4.477906 6.36953,0.319534 z" /><path id="path38" style="opacity:0.656;fill:url(#linearGradient55);stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.3348,18.551626 -5.69314,-0.458793 -2e-5,3.427512 5.69309,0.309037 z" /><path id="path39" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.71742,23.217872 -5.74903,-0.261403 -2.9e-4,11.550378 5.74884,-0.274199 z" /><path id="path41" style="opacity:0.656;fill:url(#linearGradient56);stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.404,23.660128 -5.14054,-0.213939 -2.8e-4,10.622674 5.14039,-0.22756 z" /><path id="path42" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.65617,22.942272 -6.36951,-0.289615 -3e-5,12.172873 6.36927,-0.303791 z" /><path id="path53" style="opacity:0.656;fill:url(#linearGradient57);stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.33469,23.407536 -5.69305,-0.236934 -4e-5,11.191393 5.69285,-0.252017 z" /></g></svg>

            '''
        },
        {
            "text": "Edwardian",
            "order":1,
            "subtext": "Characterized by a square or rectangular footprint, this style maximizes floor space with flat walls and a timeless, symmetrical pitched roof.",
            "svg" : '''
                

                <svg width="243.88751" height="184.9209" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1"><pattern xlink:href="#Strips1_5" preserveAspectRatio="xMidYMid" id="pattern88" patternTransform="matrix(0,0.1,-0.1,0,0,0)" x="0" y="0" /><linearGradient id="linearGradient70"><stop style="stop-color:#6dabcf;stop-opacity:1;" offset="0" id="stop67" /><stop style="stop-color:#5fb0e6;stop-opacity:0.50588232;" offset="0.45308921" id="stop68" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop70" /></linearGradient><pattern patternUnits="userSpaceOnUse" width="6" height="1" patternTransform="translate(0,0) scale(2,2)" preserveAspectRatio="xMidYMid" id="Strips1_5" style="fill:#000000">&#10;      <rect style="stroke:none" x="0" y="-0.5" width="1" height="2" id="rect164" />&#10;    </pattern><linearGradient id="linearGradient64"><stop style="stop-color:#a3c9e1;stop-opacity:1;" offset="0" id="stop61" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop62" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop63" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop64" /></linearGradient><pattern xlink:href="#Bricks" id="pattern11" patternTransform="scale(0.02)" x="0" y="0" preserveAspectRatio="none" /><pattern patternUnits="userSpaceOnUse" width="100" height="100" id="Bricks" style="fill:#935219" patternTransform="scale(0.25,0.25)"><g id="g13367"><rect style="fill:none;stroke:none;stroke-width:0" id="rect13349" width="100" height="100" x="0" y="0" /><rect style="fill-opacity:1;stroke-width:0" id="rect13351" width="40" height="40" x="0" y="60" /><rect style="fill-opacity:1;stroke-width:0" id="rect13353" width="90" height="40" x="0" y="10" /><rect style="fill-opacity:1;stroke-width:0" id="rect13355" width="50" height="40" x="50" y="60" /></g></pattern><linearGradient xlink:href="#linearGradient64" id="linearGradient8" x1="247.16119" y1="22.064793" x2="255.86038" y2="28.017918" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient64" id="linearGradient9" x1="235.37469" y1="21.204893" x2="244.71271" y2="28.017914" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient81" x1="221.19521" y1="26.766003" x2="232.82535" y2="26.766003" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient83" x1="221.27644" y1="17.586765" x2="232.91472" y2="17.586765" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient85" x1="259.2952" y1="26.766003" x2="270.92535" y2="26.766003" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient87" x1="259.37646" y1="17.586765" x2="271.01471" y2="17.586765" gradientUnits="userSpaceOnUse" /></defs><g id="layer2" transform="translate(-214.32628,-0.6498566)"><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect88" width="10.649479" height="26.127604" x="234.95" y="14.816667" /><path id="path79" style="opacity:1;fill:#968334;fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 219.19239,34.129885 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><path id="rect30-8" style="opacity:1;fill:url(#pattern11);fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 219.19239,34.129885 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><path id="path25-4" style="fill:#414141;fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 273.02783,13.879819 -16.06221,-0.682543 h -23.66933 l -14.50441,0.682543 27.11797,-9.3871082 z" /><path id="rect25-2" style="fill:#302c2a;fill-opacity:1;stroke:none;stroke-width:0.0795385;stroke-linecap:square;paint-order:stroke markers fill" d="m 218.87407,13.294216 14.73106,-0.120338 h 23.3848 l 15.81024,0.120338 v 1.10675 l -15.86856,-0.120338 h -23.3848 l -14.67274,0.120338 z" /><rect style="opacity:1;fill:#e5e5e5;fill-opacity:1;stroke:#e5e5e5;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26-1" width="24.067005" height="27.844791" x="234.06995" y="14.266648" /><rect style="opacity:1;fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.11265;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect89" width="11.11319" height="25.726902" x="234.80177" y="15.154462" /><rect style="opacity:0.579137;fill:url(#linearGradient9);fill-opacity:1;stroke:#787666;stroke-width:0.093878;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27-3" width="8.3181" height="23.871012" x="236.34767" y="16.082407" /><rect style="opacity:1;fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.11265;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect90" width="11.11319" height="25.726902" x="246.1496" y="15.154462" /><rect style="opacity:0.579137;fill:url(#linearGradient8);fill-opacity:1;stroke:#787666;stroke-width:0.0954728;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect28-7" width="8.6037045" height="23.869417" x="247.20894" y="16.083208" /><rect style="fill:#fbfbfb;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29-0" width="28.617632" height="1.0721303" x="231.31697" y="41.602776" rx="1.3296698" /><path id="rect41" style="fill:#e5e5e5;fill-opacity:1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 219.97674,14.215631 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path90" style="fill:#ffffff;fill-opacity:1;stroke-width:0.853368;stroke-linecap:square;paint-order:stroke markers fill" d="m 220.4827,15.139068 h 13.22577 v 4.730031 h -13.22577 z" /><path id="rect42" style="opacity:0.651079;fill:url(#linearGradient83);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 221.27645,15.840274 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path92" style="fill:#ffffff;fill-opacity:1;stroke-width:1.45632;stroke-linecap:square;paint-order:stroke markers fill" d="m 220.4827,20.017327 h 13.22577 v 13.775473 h -13.22577 z" /><path id="rect43" style="opacity:0.654676;fill:url(#linearGradient81);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 221.19521,20.470508 h 11.63014 v 12.590987 h -11.63014 z" /><path id="path43" style="fill:#e5e5e5;fill-opacity:1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 258.07674,14.215631 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path98" style="fill:#ffffff;fill-opacity:1;stroke-width:0.853368;stroke-linecap:square;paint-order:stroke markers fill" d="m 258.51661,15.139068 h 13.22577 v 4.730031 h -13.22577 z" /><path id="path44" style="opacity:0.661871;fill:url(#linearGradient87);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 259.37645,15.840274 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path99" style="fill:#ffffff;fill-opacity:1;stroke-width:1.45632;stroke-linecap:square;paint-order:stroke markers fill" d="m 258.51661,20.017327 h 13.22577 v 13.775473 h -13.22577 z" /><path id="path45" style="opacity:0.645683;fill:url(#linearGradient85);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 259.29521,20.470508 h 11.63014 v 12.590987 h -11.63014 z" /><path id="path87" style="fill:url(#pattern88);fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 273.02783,13.879819 -16.06221,-0.682543 h -23.66933 l -14.50441,0.682543 27.11797,-9.3871082 z" /><path id="path91" style="fill:url(#pattern88);fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 273.02783,13.879819 -16.06221,-0.682543 h -23.66933 l -14.50441,0.682543 27.11797,-9.3871082 z" /></g></svg>
            
            '''
        },
        {
            "text": "Gable-Ended",
            "order":2,
            "subtext": "Features a high, upright front roof that mimics the gable end of a house, creating a grand, light-filled interior with impressive height.",
            "svg" : '''
                <svg width="243.88751" height="184.9209" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1"><linearGradient id="linearGradient70"><stop style="stop-color:#6dabcf;stop-opacity:1;" offset="0" id="stop67" /><stop style="stop-color:#5fb0e6;stop-opacity:0.50588232;" offset="0.45308921" id="stop68" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop70" /></linearGradient><linearGradient id="linearGradient64"><stop style="stop-color:#a3c9e1;stop-opacity:1;" offset="0" id="stop61" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop62" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop63" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop64" /></linearGradient><pattern xlink:href="#Bricks-3" id="pattern11-0" patternTransform="matrix(0.02,0,0,0.02,73.57676,-1.0399659)" x="0" y="0" preserveAspectRatio="none" /><pattern patternUnits="userSpaceOnUse" width="100" height="100" id="Bricks-3" style="fill:#935219" patternTransform="scale(0.25,0.25)"><g id="g13367-7"><rect style="fill:none;stroke:none;stroke-width:0" id="rect13349-3" width="100" height="100" x="0" y="0" /><rect style="fill-opacity:1;stroke-width:0" id="rect13351-4" width="40" height="40" x="0" y="60" /><rect style="fill-opacity:1;stroke-width:0" id="rect13353-2" width="90" height="40" x="0" y="10" /><rect style="fill-opacity:1;stroke-width:0" id="rect13355-6" width="50" height="40" x="50" y="60" /></g></pattern><linearGradient xlink:href="#linearGradient64" id="linearGradient92" gradientUnits="userSpaceOnUse" x1="235.37469" y1="21.204893" x2="244.71271" y2="28.017914" gradientTransform="translate(73.57676,-1.0399659)" /><linearGradient xlink:href="#linearGradient64" id="linearGradient93" gradientUnits="userSpaceOnUse" x1="247.16119" y1="22.064793" x2="255.86038" y2="28.017918" gradientTransform="translate(73.57676,-1.0399659)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient94" gradientUnits="userSpaceOnUse" x1="221.27644" y1="17.586765" x2="232.91472" y2="17.586765" gradientTransform="translate(73.57676,-1.0399659)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient95" gradientUnits="userSpaceOnUse" x1="221.19521" y1="26.766003" x2="232.82535" y2="26.766003" gradientTransform="translate(73.57676,-1.0399659)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient96" gradientUnits="userSpaceOnUse" x1="259.37646" y1="17.586765" x2="271.01471" y2="17.586765" gradientTransform="translate(73.57676,-1.0399659)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient97" gradientUnits="userSpaceOnUse" x1="259.2952" y1="26.766003" x2="270.92535" y2="26.766003" gradientTransform="translate(73.57676,-1.0399659)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient101" x1="296.92862" y1="9.2769527" x2="307.44583" y2="9.2769527" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient102" gradientUnits="userSpaceOnUse" x1="296.92862" y1="9.2769527" x2="307.44583" y2="9.2769527" gradientTransform="matrix(-1,0,0,1,638.90269,0)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient104" x1="308.08826" y1="6.6416469" x2="319.36032" y2="6.6416469" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient105" gradientUnits="userSpaceOnUse" x1="308.08826" y1="6.6416469" x2="319.36032" y2="6.6416469" gradientTransform="matrix(-1,0,0,1,639.09032,0)" /></defs><g id="layer2" transform="translate(-287.23021)"><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect88-9" width="10.649479" height="26.127604" x="308.52676" y="13.776701" /><path id="path79-9" style="fill:#968334;fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 292.76915,33.089919 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><path id="rect30-8-2" style="fill:url(#pattern11-0);fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 292.76915,33.089919 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><path id="path25-4-3" style="fill:#e5e5e5;fill-opacity:1;stroke:#666557;stroke-width:0.0283881;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 346.60357,12.837258 c -18.32479,-0.364849 -35.76725,-0.205081 -54.23391,0 l 27.11695,-12.22596641 z" /><path id="rect25-2-8" style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.0795385;stroke-linecap:square;paint-order:stroke markers fill" d="m 292.45083,12.25425 14.73106,-0.120338 h 23.3848 l 15.81024,0.120338 v 1.10675 l -15.86856,-0.120338 h -23.3848 l -14.67274,0.120338 z" /><rect style="fill:#e5e5e5;fill-opacity:1;stroke:#e5e5e5;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26-1-7" width="24.067005" height="27.844791" x="307.6467" y="13.226683" /><rect style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.113211;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect89-3" width="11.224282" height="25.726902" x="308.29773" y="14.114496" /><rect style="opacity:0.579137;fill:url(#linearGradient92);fill-opacity:1;stroke:#787666;stroke-width:0.093878;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27-3-4" width="8.3181" height="23.871012" x="309.92444" y="15.042441" /><rect style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.113044;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect90-7" width="11.19121" height="25.726902" x="319.79529" y="14.114496" /><rect style="opacity:0.579137;fill:url(#linearGradient93);fill-opacity:1;stroke:#787666;stroke-width:0.0954728;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect28-7-2" width="8.6037045" height="23.869417" x="320.78571" y="15.043242" /><rect style="fill:#fbfbfb;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29-0-2" width="28.617632" height="1.0721303" x="304.89374" y="40.562809" rx="1.3296698" /><path id="rect41-1" style="fill:#e5e5e5;fill-opacity:1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 293.5535,13.175665 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path90-9" style="fill:#ffffff;fill-opacity:1;stroke-width:0.853368;stroke-linecap:square;paint-order:stroke markers fill" d="m 294.05946,14.099102 h 13.22577 v 4.730031 h -13.22577 z" /><path id="rect42-1" style="opacity:0.651079;fill:url(#linearGradient94);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 294.85321,14.800308 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path92-3" style="fill:#ffffff;fill-opacity:1;stroke-width:1.45632;stroke-linecap:square;paint-order:stroke markers fill" d="m 294.05946,18.977361 h 13.22577 v 13.775473 h -13.22577 z" /><path id="rect43-6" style="opacity:0.654676;fill:url(#linearGradient95);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 294.77197,19.430542 h 11.63014 v 12.590987 h -11.63014 z" /><path id="path43-5" style="fill:#e5e5e5;fill-opacity:1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 331.6535,13.175665 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path106" style="fill:#ffffff;fill-opacity:1;stroke-width:0.853368;stroke-linecap:square;paint-order:stroke markers fill" d="m 332.1016,14.099102 h 13.22577 v 4.730031 h -13.22577 z" /><path id="path44-9" style="opacity:0.661871;fill:url(#linearGradient96);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 332.95321,14.800308 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path105" style="fill:#ffffff;fill-opacity:1;stroke-width:1.45632;stroke-linecap:square;paint-order:stroke markers fill" d="m 332.09331,18.977361 h 13.22577 v 13.775473 h -13.22577 z" /><path id="path45-6" style="opacity:0.645683;fill:url(#linearGradient97);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 332.87197,19.430542 h 11.63014 v 12.590987 h -11.63014 z" /><path style="opacity:0.579137;fill:url(#linearGradient101);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 307.44582,11.476301 v -4.5309891 l -10.51719,4.6632811 z" id="path100" /><path style="opacity:0.579137;fill:url(#linearGradient102);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 331.45682,11.476301 v -4.5309891 l 10.51719,4.6632811 z" id="path101" /><path style="opacity:0.579137;fill:url(#linearGradient104);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 319.36032,11.552725 v -9.8689271 l -11.27207,4.9578493 v 4.9578488 z" id="path102" /><path style="opacity:0.579137;fill:url(#linearGradient105);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 319.72996,11.552725 v -9.8689271 l 11.27207,4.9578493 v 4.9578488 z" id="path104" /></g></svg>
            '''
        },
        {
            "text": "Lean-To",
            "order":3,
            "subtext": "A simple, modern option with a single sloped roof that leans against the main property, making it ideal for bungalows or limited spaces.",
            "svg" : '''

                    <svg width="243.88751" height="184.9209" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1"><pattern xlink:href="#Strips1_5-9" preserveAspectRatio="xMidYMid" id="pattern125" patternTransform="matrix(0,0.1,-0.1,0,0,0)" x="0" y="0" /><linearGradient id="linearGradient70"><stop style="stop-color:#6dabcf;stop-opacity:1;" offset="0" id="stop67" /><stop style="stop-color:#5fb0e6;stop-opacity:0.50588232;" offset="0.45308921" id="stop68" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop70" /></linearGradient><linearGradient id="linearGradient64"><stop style="stop-color:#a3c9e1;stop-opacity:1;" offset="0" id="stop61" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop62" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop63" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop64" /></linearGradient><pattern xlink:href="#Bricks-3-2" id="pattern11-0-1" patternTransform="matrix(0.02,0,0,0.02,148.19,0.21639575)" x="0" y="0" preserveAspectRatio="none" /><pattern patternUnits="userSpaceOnUse" width="100" height="100" id="Bricks-3-2" style="fill:#935219" patternTransform="scale(0.25,0.25)"><g id="g13367-7-8"><rect style="fill:none;stroke:none;stroke-width:0" id="rect13349-3-0" width="100" height="100" x="0" y="0" /><rect style="fill-opacity:1;stroke-width:0" id="rect13351-4-2" width="40" height="40" x="0" y="60" /><rect style="fill-opacity:1;stroke-width:0" id="rect13353-2-6" width="90" height="40" x="0" y="10" /><rect style="fill-opacity:1;stroke-width:0" id="rect13355-6-6" width="50" height="40" x="50" y="60" /></g></pattern><linearGradient xlink:href="#linearGradient64" id="linearGradient106" gradientUnits="userSpaceOnUse" gradientTransform="translate(148.19,0.21639575)" x1="235.37469" y1="21.204893" x2="244.71271" y2="28.017914" /><linearGradient xlink:href="#linearGradient64" id="linearGradient107" gradientUnits="userSpaceOnUse" gradientTransform="translate(148.19,0.21639575)" x1="247.16119" y1="22.064793" x2="255.86038" y2="28.017918" /><linearGradient xlink:href="#linearGradient70" id="linearGradient108" gradientUnits="userSpaceOnUse" gradientTransform="translate(148.19,0.21639575)" x1="221.27644" y1="17.586765" x2="232.91472" y2="17.586765" /><linearGradient xlink:href="#linearGradient70" id="linearGradient109" gradientUnits="userSpaceOnUse" gradientTransform="translate(148.19,0.21639575)" x1="221.19521" y1="26.766003" x2="232.82535" y2="26.766003" /><linearGradient xlink:href="#linearGradient70" id="linearGradient110" gradientUnits="userSpaceOnUse" gradientTransform="translate(148.19,0.21639575)" x1="259.37646" y1="17.586765" x2="271.01471" y2="17.586765" /><linearGradient xlink:href="#linearGradient70" id="linearGradient111" gradientUnits="userSpaceOnUse" gradientTransform="translate(148.19,0.21639575)" x1="259.2952" y1="26.766003" x2="270.92535" y2="26.766003" /><pattern patternUnits="userSpaceOnUse" width="6" height="1" patternTransform="translate(0,0) scale(2,2)" preserveAspectRatio="xMidYMid" id="Strips1_5-9" style="fill:#000000">&#10;      <rect style="stroke:none" x="0" y="-0.5" width="1" height="2" id="rect164-7" />&#10;    </pattern></defs><g id="layer2" transform="translate(-361.75877)"><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect88-9-3" width="10.649479" height="26.127604" x="383.14001" y="15.033063" /><path id="path79-9-5" style="fill:#968334;fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 367.38239,34.34628 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><path id="rect30-8-2-7" style="fill:url(#pattern11-0-1);fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 367.38239,34.34628 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><path id="rect25-2-8-7" style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.0795385;stroke-linecap:square;paint-order:stroke markers fill" d="m 367.06407,13.510611 14.73106,-0.120338 h 23.3848 l 15.81024,0.120338 v 1.10675 l -15.86856,-0.120338 h -23.3848 l -14.67274,0.120338 z" /><rect style="fill:#e5e5e5;fill-opacity:1;stroke:#e5e5e5;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26-1-7-1" width="24.067005" height="27.844791" x="382.25995" y="14.483045" /><rect style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.113211;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect89-3-4" width="11.224282" height="25.726902" x="382.91098" y="15.370858" /><rect style="opacity:0.579137;fill:url(#linearGradient106);fill-opacity:1;stroke:#787666;stroke-width:0.093878;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27-3-4-8" width="8.3181" height="23.871012" x="384.53769" y="16.298803" /><rect style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.113044;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect90-7-9" width="11.19121" height="25.726902" x="394.40854" y="15.370858" /><rect style="opacity:0.579137;fill:url(#linearGradient107);fill-opacity:1;stroke:#787666;stroke-width:0.0954728;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect28-7-2-1" width="8.6037045" height="23.869417" x="395.39896" y="16.299604" /><rect style="fill:#f2f2f2;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29-0-2-5" width="28.617632" height="1.0721303" x="379.50699" y="41.819172" rx="1.3296698" /><path id="rect41-1-6" style="fill:#e5e5e5;fill-opacity:1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 368.16674,14.432026 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path90-9-9" style="fill:#ffffff;fill-opacity:1;stroke-width:0.853368;stroke-linecap:square;paint-order:stroke markers fill" d="m 368.6727,15.355463 h 13.22577 v 4.730031 h -13.22577 z" /><path id="rect42-1-6" style="opacity:0.651079;fill:url(#linearGradient108);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 369.46645,16.056669 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path92-3-7" style="fill:#ffffff;fill-opacity:1;stroke-width:1.45632;stroke-linecap:square;paint-order:stroke markers fill" d="m 368.6727,20.233722 h 13.22577 v 13.775473 h -13.22577 z" /><path id="rect43-6-0" style="opacity:0.654676;fill:url(#linearGradient109);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 369.38521,20.686903 h 11.63014 v 12.590987 h -11.63014 z" /><path id="path43-5-7" style="fill:#e5e5e5;fill-opacity:1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 406.26674,14.432026 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path106-1" style="fill:#ffffff;fill-opacity:1;stroke-width:0.853368;stroke-linecap:square;paint-order:stroke markers fill" d="m 406.71484,15.355463 h 13.22577 v 4.730031 h -13.22577 z" /><path id="path44-9-4" style="opacity:0.661871;fill:url(#linearGradient110);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 407.56645,16.056669 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path105-5" style="fill:#ffffff;fill-opacity:1;stroke-width:1.45632;stroke-linecap:square;paint-order:stroke markers fill" d="m 406.70655,20.233722 h 13.22577 v 13.775473 h -13.22577 z" /><path id="path45-6-9" style="opacity:0.645683;fill:url(#linearGradient111);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 407.48521,20.686903 h 11.63014 v 12.590987 h -11.63014 z" /><path id="path115" style="fill:#464646;fill-opacity:1;stroke:none;stroke-width:0.187008;stroke-linecap:square;paint-order:stroke markers fill" d="m 367.06407,7.3767234 14.73106,-0.665228 h 23.3848 l 15.81024,0.665228 v 6.1181096 c -26.57622,-0.0093 -34.11948,-0.01511 -53.9261,0 z" /><path id="path124" style="fill:url(#pattern125);fill-opacity:1;stroke:none;stroke-width:0.187008;stroke-linecap:square;paint-order:stroke markers fill" d="m 367.06407,7.3767234 14.73106,-0.665228 h 23.3848 l 15.81024,0.665228 v 6.1181096 c -26.57622,-0.0093 -34.11948,-0.01511 -53.9261,0 z" /></g></svg>

            '''
        },
        {
            "text": "P-Shaped",
            "order":4,
            "subtext": "Combines a lean-to element with a rounded Victorian or Edwardian extension, creating a versatile, multi-functional, zoned living area.",
            "svg" : '''
                <svg width="243.88751" height="184.9209" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1"><pattern xlink:href="#Strips1_5-9" preserveAspectRatio="xMidYMid" id="pattern126" patternTransform="matrix(0,0.1,-0.1,0,0,0)" x="0" y="0" /><pattern xlink:href="#Bricks-35" id="pattern122" patternTransform="scale(0.017)" x="0" y="0" preserveAspectRatio="xMidYMid" /><pattern xlink:href="#pattern88-2" preserveAspectRatio="xMidYMid" id="pattern121" patternTransform="matrix(0,0.1,-0.1,0,225.97675,-1.5691325)" /><pattern xlink:href="#pattern88-2" preserveAspectRatio="xMidYMid" id="pattern120" patternTransform="matrix(0,0.1,-0.1,0,225.97675,-1.5691325)" /><linearGradient id="linearGradient70"><stop style="stop-color:#6dabcf;stop-opacity:1;" offset="0" id="stop67" /><stop style="stop-color:#5fb0e6;stop-opacity:0.50588232;" offset="0.45308921" id="stop68" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop70" /></linearGradient><linearGradient id="linearGradient64"><stop style="stop-color:#a3c9e1;stop-opacity:1;" offset="0" id="stop61" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop62" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop63" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop64" /></linearGradient><pattern xlink:href="#Bricks-35" id="pattern11-8" patternTransform="matrix(0.02,0,0,0.02,225.97675,-1.5691325)" x="0" y="0" preserveAspectRatio="none" /><pattern patternUnits="userSpaceOnUse" width="100" height="100" id="Bricks-35" style="fill:#935219" patternTransform="scale(0.25,0.25)"><g id="g13367-4"><rect style="fill:none;stroke:none;stroke-width:0" id="rect13349-1" width="100" height="100" x="0" y="0" /><rect style="fill-opacity:1;stroke-width:0" id="rect13351-41" width="40" height="40" x="0" y="60" /><rect style="fill-opacity:1;stroke-width:0" id="rect13353-8" width="90" height="40" x="0" y="10" /><rect style="fill-opacity:1;stroke-width:0" id="rect13355-8" width="50" height="40" x="50" y="60" /></g></pattern><pattern xlink:href="#Strips1_5-9" preserveAspectRatio="xMidYMid" id="pattern88-2" patternTransform="matrix(0,0.1,-0.1,0,0,0)" x="0" y="0" /><pattern patternUnits="userSpaceOnUse" width="6" height="1" patternTransform="translate(0,0) scale(2,2)" preserveAspectRatio="xMidYMid" id="Strips1_5-9" style="fill:#000000">&#10;      <rect style="stroke:none" x="0" y="-0.5" width="1" height="2" id="rect164-7" />&#10;    </pattern><linearGradient xlink:href="#linearGradient64" id="linearGradient115" gradientUnits="userSpaceOnUse" x1="235.37469" y1="21.204893" x2="244.71271" y2="28.017914" gradientTransform="translate(225.97675,-1.5691325)" /><linearGradient xlink:href="#linearGradient64" id="linearGradient116" gradientUnits="userSpaceOnUse" x1="247.16119" y1="22.064793" x2="255.86038" y2="28.017918" gradientTransform="translate(225.97675,-1.5691325)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient117" gradientUnits="userSpaceOnUse" x1="221.27644" y1="17.586765" x2="232.91472" y2="17.586765" gradientTransform="translate(225.97675,-1.5691325)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient118" gradientUnits="userSpaceOnUse" x1="221.19521" y1="26.766003" x2="232.82535" y2="26.766003" gradientTransform="translate(225.97675,-1.5691325)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient119" gradientUnits="userSpaceOnUse" x1="259.37646" y1="17.586765" x2="271.01471" y2="17.586765" gradientTransform="translate(225.97675,-1.5691325)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient120" gradientUnits="userSpaceOnUse" x1="259.2952" y1="26.766003" x2="270.92535" y2="26.766003" gradientTransform="translate(225.97675,-1.5691325)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient123" x1="441.69827" y1="19.838341" x2="448.43146" y2="19.838341" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient124" x1="441.64957" y1="25.727648" x2="448.37787" y2="25.727648" gradientUnits="userSpaceOnUse" /></defs><g id="layer2" transform="translate(-436.28734)"><path id="rect41-4-8" style="fill:#f1f1f1;fill-opacity:1;stroke-width:0.411538;stroke-linecap:square;paint-order:stroke markers fill" d="m 440.7262,17.675454 h 7.85235 v 12.798296 h -7.85235 z" /><path id="rect42-0-5" style="fill:url(#linearGradient123);stroke-width:0.426629;stroke-linecap:square;paint-order:stroke markers fill" d="m 441.69828,18.717809 h 6.73317 v 2.241064 h -6.73317 z" /><path id="rect43-7-7" style="fill:url(#linearGradient124);stroke-width:0.426629;stroke-linecap:square;paint-order:stroke markers fill" d="m 441.64958,21.688522 h 6.7283 v 8.078252 h -6.7283 z" /><path id="rect49" style="opacity:1;fill:#414141;stroke-width:1.03678;stroke-linecap:square;paint-order:stroke markers fill" d="m 442.63178,8.9355392 h 17.78985 v 8.6918428 h -21.49402 z" /><path style="opacity:1;fill:none;fill-opacity:1;stroke:#302c2a;stroke-width:0.580496;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 458.8411,8.9761553 h -15.76252" id="path50" /><path style="opacity:1;fill:none;fill-opacity:1;stroke:#302c2a;stroke-width:0.517811;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 439.24595,17.576586 h 8.0232" id="path51" /><path id="rect51" style="opacity:1;fill:#948319;fill-opacity:1;stroke:#3b3634;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" d="m 440.72079,30.299601 h 6.54124 v 10.316486 h -6.54124 z" /><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect88-1" width="10.649479" height="26.127604" x="460.92673" y="13.247536" /><path id="path121" style="opacity:1;fill:url(#pattern122);fill-opacity:1;stroke:#3b3634;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" d="m 440.72079,30.299601 h 6.54124 v 10.316486 h -6.54124 z" /><path id="path79-1" style="fill:#968334;fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 445.16914,32.56075 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><path id="rect30-8-27" style="fill:url(#pattern11-8);fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 445.16914,32.56075 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><path id="path125" style="opacity:1;fill:url(#pattern126);fill-opacity:1;stroke-width:1.03678;stroke-linecap:square;paint-order:stroke markers fill" d="m 442.63178,8.9355392 h 17.78985 v 8.6918428 h -21.49402 z" /><path id="path25-4-9" style="fill:#414141;fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 499.00458,12.310684 -16.06221,-0.682543 h -23.66933 l -14.50441,0.682543 27.11797,-9.3871055 z" /><path id="rect25-2-1" style="fill:#302c2a;fill-opacity:1;stroke:none;stroke-width:0.0795385;stroke-linecap:square;paint-order:stroke markers fill" d="m 444.85082,11.725081 14.73106,-0.120338 h 23.3848 l 15.81024,0.120338 v 1.10675 l -15.86856,-0.120338 h -23.3848 l -14.67274,0.120338 z" /><rect style="fill:#e5e5e5;fill-opacity:1;stroke:#e5e5e5;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26-1-0" width="24.067005" height="27.844791" x="460.04669" y="12.697518" /><rect style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.11265;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect89-8" width="11.11319" height="25.726902" x="460.7785" y="13.58533" /><rect style="opacity:0.579137;fill:url(#linearGradient115);fill-opacity:1;stroke:#787666;stroke-width:0.093878;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27-3-3" width="8.3181" height="23.871012" x="462.3244" y="14.513274" /><rect style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.11265;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect90-78" width="11.11319" height="25.726902" x="472.12634" y="13.58533" /><rect style="opacity:0.579137;fill:url(#linearGradient116);fill-opacity:1;stroke:#787666;stroke-width:0.0954728;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect28-7-1" width="8.6037045" height="23.869417" x="473.18567" y="14.514076" /><rect style="fill:#fbfbfb;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29-0-0" width="28.617632" height="1.0721303" x="457.2937" y="40.033638" rx="1.3296698" /><path id="rect41-6" style="fill:#e5e5e5;fill-opacity:1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 445.95349,12.646496 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path90-5" style="fill:#ffffff;fill-opacity:1;stroke-width:0.853368;stroke-linecap:square;paint-order:stroke markers fill" d="m 446.45945,13.569933 h 13.22577 v 4.730031 h -13.22577 z" /><path id="rect42-5" style="opacity:0.651079;fill:url(#linearGradient117);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 447.2532,14.271139 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path92-9" style="fill:#ffffff;fill-opacity:1;stroke-width:1.45632;stroke-linecap:square;paint-order:stroke markers fill" d="m 446.45945,18.448192 h 13.22577 v 13.775473 h -13.22577 z" /><path id="rect43-0" style="opacity:0.654676;fill:url(#linearGradient118);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 447.17196,18.901373 h 11.63014 v 12.590987 h -11.63014 z" /><path id="path43-9" style="fill:#e5e5e5;fill-opacity:1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 484.05349,12.646496 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path98-0" style="fill:#ffffff;fill-opacity:1;stroke-width:0.853368;stroke-linecap:square;paint-order:stroke markers fill" d="m 484.49336,13.569933 h 13.22577 v 4.730031 h -13.22577 z" /><path id="path44-1" style="opacity:0.661871;fill:url(#linearGradient119);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 485.3532,14.271139 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path99-6" style="fill:#ffffff;fill-opacity:1;stroke-width:1.45632;stroke-linecap:square;paint-order:stroke markers fill" d="m 484.49336,18.448192 h 13.22577 v 13.775473 h -13.22577 z" /><path id="path45-0" style="opacity:0.645683;fill:url(#linearGradient120);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 485.27196,18.901373 h 11.63014 v 12.590987 h -11.63014 z" /><path id="path87-8" style="fill:url(#pattern120);fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 499.00458,12.310684 -16.06221,-0.682543 h -23.66933 l -14.50441,0.682543 27.11797,-9.3871055 z" /><path id="path91-8" style="fill:url(#pattern121);fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 499.00458,12.310684 -16.06221,-0.682543 h -23.66933 l -14.50441,0.682543 27.11797,-9.3871055 z" /></g></svg>

            '''
        },
        {
            "text": "Other",
            "order": 5,
            "subtext": "Combines a lean-to element with a rounded Victorian or Edwardian extension, creating a versatile, multi-functional, zoned living area.",
            "svg" : '''

                <svg width="243.88751" height="184.9209" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"></svg>
            '''
        }

    ]

    },
    {
        'tag': 'about-intro',
        'section_id': 5, 
        'items': [
            {
                'order': 0,
                "text": 'Lorem Ipsum Dolar Amet',
                "svg" : '''                         
                    <svg width="243.88751" height="184.9209" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1"><linearGradient id="linearGradient70"><stop style="stop-color:#6dabcf;stop-opacity:1;" offset="0" id="stop67" /><stop style="stop-color:#5fb0e6;stop-opacity:0.50588232;" offset="0.45308921" id="stop68" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop70" /></linearGradient><pattern xlink:href="#Strips1_5" preserveAspectRatio="xMidYMid" id="pattern67" patternTransform="matrix(0,0.1,-0.1,0,0,0)" x="0" y="0" /><pattern patternUnits="userSpaceOnUse" width="6" height="1" patternTransform="translate(0,0) scale(2,2)" preserveAspectRatio="xMidYMid" id="Strips1_5" style="fill:#000000">&#10;      <rect style="stroke:none" x="0" y="-0.5" width="1" height="2" id="rect164" />&#10;    </pattern><linearGradient id="linearGradient64"><stop style="stop-color:#a3c9e1;stop-opacity:1;" offset="0" id="stop61" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop62" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop63" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop64" /></linearGradient><linearGradient id="linearGradient60"><stop style="stop-color:#8cbed9;stop-opacity:1;" offset="0" id="stop57" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop58" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop59" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop60" /></linearGradient><pattern xlink:href="#pattern13" preserveAspectRatio="xMidYMid" id="pattern14" patternTransform="matrix(-0.01995129,0.00139513,-0.00139513,-0.01995129,0,0)" x="0" y="0" /><pattern xlink:href="#Bricks" id="pattern13" patternTransform="matrix(0.01995129,0.00139513,-0.00139513,0.01995129,0.42094947,-11.739813)" x="0" y="0" preserveAspectRatio="xMidYMid" /><pattern xlink:href="#Bricks" id="pattern10" patternTransform="scale(0.02)" x="0" y="0" preserveAspectRatio="none" /><pattern patternUnits="userSpaceOnUse" width="100" height="100" id="Bricks" style="fill:#935219" patternTransform="scale(0.25,0.25)"><g id="g13367"><rect style="fill:none;stroke:none;stroke-width:0" id="rect13349" width="100" height="100" x="0" y="0" /><rect style="fill-opacity:1;stroke-width:0" id="rect13351" width="40" height="40" x="0" y="60" /><rect style="fill-opacity:1;stroke-width:0" id="rect13353" width="90" height="40" x="0" y="10" /><rect style="fill-opacity:1;stroke-width:0" id="rect13355" width="50" height="40" x="50" y="60" /></g></pattern><linearGradient xlink:href="#linearGradient60" id="linearGradient11" x1="167.06261" y1="27.089109" x2="173.57579" y2="31.392151" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient64" id="linearGradient14" gradientUnits="userSpaceOnUse" x1="167.06261" y1="27.089109" x2="173.57579" y2="31.392151" gradientTransform="translate(10.555822,-0.10841814)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient54" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="145.01958" y1="24.0648" x2="148.92474" y2="19.325005" /><linearGradient xlink:href="#linearGradient70" id="linearGradient55" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="152.00311" y1="23.510586" x2="157.09706" y2="17.924889" /><linearGradient xlink:href="#linearGradient70" id="linearGradient56" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="139.66898" y1="34.298935" x2="148.91502" y2="24.094034" /><linearGradient xlink:href="#linearGradient70" id="linearGradient57" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="150.92365" y1="34.486496" x2="160.32947" y2="26.142387" /><linearGradient xlink:href="#linearGradient70" id="linearGradient72" x1="155.09953" y1="28.766298" x2="160.79262" y2="28.766298" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient73" x1="149.03021" y1="28.757526" x2="154.17104" y2="28.757526" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient74" x1="149.03001" y1="20.392658" x2="154.17073" y2="20.392658" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient75" x1="155.09943" y1="19.961107" x2="160.79259" y2="19.961107" gradientUnits="userSpaceOnUse" /></defs><g id="layer2" transform="translate(-142.39713,-1.5863839)"><path style="fill:#968334;fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 198.60245,45.193143 -0.0661,-9.98802 -13.95677,1.124479 v 11.112499 z" id="path76" /><path id="path77" style="fill:#968334;fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 184.58344,43.618976 0.0583,3.696537 h -23.0349 l 0.0187,-5.481645 z" /><path style="fill:#968334;fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 147.79386,45.112527 0.0661,-9.98802 13.95677,1.124479 v 11.112499 z" id="path78" /><path id="path75" style="fill:#42403e;fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 200.79629,15.944435 -16.06221,-1.343101 h -23.66934 l -14.5044,1.343101 27.11797,-10.9746084 z" /><path style="fill:url(#pattern14);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 198.60245,45.193143 -0.0661,-9.98802 -13.95677,1.124479 v 11.112499 z" id="path13" /><path id="rect30" style="fill:url(#pattern10);fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 184.58344,43.618976 0.0583,3.696537 h -23.0349 l 0.0187,-5.481645 z" /><path id="path25" style="fill:url(#pattern67);fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 200.79629,15.944435 -16.06221,-1.343101 h -23.66934 l -14.5044,1.343101 27.11797,-10.9746084 z" /><path id="rect25" style="fill:#302c2a;fill-opacity:1;stroke:none;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 146.64253,15.977569 14.73106,-1.226469 h 23.3848 l 15.81024,1.226469 v 1.546345 l -15.86856,-1.226469 h -23.38479 l -14.67275,1.226469 z" /><rect style="fill:#e5e5e5;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26" width="22.803343" height="27.902233" x="161.83841" y="16.331261" /><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect2" width="10.649479" height="26.127604" x="162.71873" y="16.999477" /><rect style="opacity:0.579137;fill:url(#linearGradient11);fill-opacity:1;stroke:#787666;stroke-width:0.0915985;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27" width="7.9183006" height="23.873291" x="164.11497" y="18.145884" /><path style="fill:url(#pattern13);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 147.79386,45.112527 0.0661,-9.98802 13.95677,1.124479 v 11.112499 z" id="path11" /><rect style="fill:#f6f6f6;fill-opacity:1;stroke:#414141;stroke-width:0.0739189;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29" width="28.63773" height="0.66228044" x="159.07536" y="43.558125" rx="1.3306036" /><path style="fill:none;fill-opacity:1;stroke:#484848;stroke-width:0.349206;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 162.508,13.647747 11.06827,-7.6286199 10.62175,7.7935629" id="path40" /><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect3" width="10.649479" height="26.127604" x="173.30208" y="16.999477" /><rect style="opacity:0.579137;fill:url(#linearGradient14);fill-opacity:1;stroke:#787666;stroke-width:0.0915985;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27-2" width="7.9183006" height="23.873291" x="174.67079" y="18.037466" /><rect style="fill:#e5e5e5;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect4" width="0.52916974" height="26.309505" x="172.93828" y="16.900259" /><path id="rect14" style="fill:#e5e5e5;stroke-width:1.13801;stroke-linecap:square;paint-order:markers fill stroke" d="m 148.26509,17.630418 13.55405,-1.261677 v 19.680735 l -13.55325,-0.769448 z" /><path id="rect28" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 148.77929,18.605389 5.75537,-0.485973 1e-4,4.251266 -5.7553,0.288721 z" /><path id="rect15" style="opacity:0.656;fill:url(#linearGradient74);fill-opacity:1;stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 149.03002,19.04074 5.14062,-0.414267 9e-5,3.253325 -5.14058,0.279045 z" /><path id="rect31" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 154.77794,18.098874 6.36961,-0.537837 1e-5,4.477906 -6.36953,0.319534 z" /><path id="rect16" style="opacity:0.656;fill:url(#linearGradient75);fill-opacity:1;stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 155.09942,18.551626 5.69314,-0.458793 2e-5,3.427512 -5.69309,0.309037 z" /><path id="rect33" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 148.7168,23.217872 5.74904,-0.261403 2.8e-4,11.550378 -5.74884,-0.274199 z" /><path id="rect17" style="opacity:0.656;fill:url(#linearGradient73);fill-opacity:1;stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 149.03022,23.660128 5.14054,-0.213939 2.8e-4,10.622674 -5.14039,-0.22756 z" /><path id="rect32" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 154.77805,22.942272 6.36951,-0.289615 3e-5,12.172873 -6.36927,-0.303791 z" /><path id="rect18" style="opacity:0.656;fill:url(#linearGradient72);fill-opacity:1;stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 155.09953,23.407536 5.69305,-0.236934 4e-5,11.191393 -5.69285,-0.252017 z" /><path id="path34" style="fill:#e5e5e5;stroke-width:1.13801;stroke-linecap:square;paint-order:markers fill stroke" d="m 198.16913,17.630418 -13.55405,-1.261677 v 19.680735 l 13.55325,-0.769448 z" /><path id="path35" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.65494,18.605389 -5.75538,-0.485973 -1e-4,4.251266 5.7553,0.288721 z" /><path id="path36" style="opacity:0.656;fill:url(#linearGradient54);stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.4042,19.04074 -5.14062,-0.414267 -9e-5,3.253325 5.14058,0.279045 z" /><path id="path37" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.65628,18.098874 -6.36961,-0.537837 -10e-6,4.477906 6.36953,0.319534 z" /><path id="path38" style="opacity:0.656;fill:url(#linearGradient55);stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.3348,18.551626 -5.69314,-0.458793 -2e-5,3.427512 5.69309,0.309037 z" /><path id="path39" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.71742,23.217872 -5.74903,-0.261403 -2.9e-4,11.550378 5.74884,-0.274199 z" /><path id="path41" style="opacity:0.656;fill:url(#linearGradient56);stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.404,23.660128 -5.14054,-0.213939 -2.8e-4,10.622674 5.14039,-0.22756 z" /><path id="path42" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.65617,22.942272 -6.36951,-0.289615 -3e-5,12.172873 6.36927,-0.303791 z" /><path id="path53" style="opacity:0.656;fill:url(#linearGradient57);stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.33469,23.407536 -5.69305,-0.236934 -4e-5,11.191393 5.69285,-0.252017 z" /></g></svg>

                '''
            },
            {
                'order': 1,
                "text": 'Lorem Ipsum Dolar Amet',
                "svg" : '''                         
                    <svg width="243.88751" height="184.9209" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1"><linearGradient id="linearGradient70"><stop style="stop-color:#6dabcf;stop-opacity:1;" offset="0" id="stop67" /><stop style="stop-color:#5fb0e6;stop-opacity:0.50588232;" offset="0.45308921" id="stop68" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop70" /></linearGradient><pattern xlink:href="#Strips1_5" preserveAspectRatio="xMidYMid" id="pattern67" patternTransform="matrix(0,0.1,-0.1,0,0,0)" x="0" y="0" /><pattern patternUnits="userSpaceOnUse" width="6" height="1" patternTransform="translate(0,0) scale(2,2)" preserveAspectRatio="xMidYMid" id="Strips1_5" style="fill:#000000">&#10;      <rect style="stroke:none" x="0" y="-0.5" width="1" height="2" id="rect164" />&#10;    </pattern><linearGradient id="linearGradient64"><stop style="stop-color:#a3c9e1;stop-opacity:1;" offset="0" id="stop61" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop62" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop63" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop64" /></linearGradient><linearGradient id="linearGradient60"><stop style="stop-color:#8cbed9;stop-opacity:1;" offset="0" id="stop57" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop58" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop59" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop60" /></linearGradient><pattern xlink:href="#pattern13" preserveAspectRatio="xMidYMid" id="pattern14" patternTransform="matrix(-0.01995129,0.00139513,-0.00139513,-0.01995129,0,0)" x="0" y="0" /><pattern xlink:href="#Bricks" id="pattern13" patternTransform="matrix(0.01995129,0.00139513,-0.00139513,0.01995129,0.42094947,-11.739813)" x="0" y="0" preserveAspectRatio="xMidYMid" /><pattern xlink:href="#Bricks" id="pattern10" patternTransform="scale(0.02)" x="0" y="0" preserveAspectRatio="none" /><pattern patternUnits="userSpaceOnUse" width="100" height="100" id="Bricks" style="fill:#935219" patternTransform="scale(0.25,0.25)"><g id="g13367"><rect style="fill:none;stroke:none;stroke-width:0" id="rect13349" width="100" height="100" x="0" y="0" /><rect style="fill-opacity:1;stroke-width:0" id="rect13351" width="40" height="40" x="0" y="60" /><rect style="fill-opacity:1;stroke-width:0" id="rect13353" width="90" height="40" x="0" y="10" /><rect style="fill-opacity:1;stroke-width:0" id="rect13355" width="50" height="40" x="50" y="60" /></g></pattern><linearGradient xlink:href="#linearGradient60" id="linearGradient11" x1="167.06261" y1="27.089109" x2="173.57579" y2="31.392151" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient64" id="linearGradient14" gradientUnits="userSpaceOnUse" x1="167.06261" y1="27.089109" x2="173.57579" y2="31.392151" gradientTransform="translate(10.555822,-0.10841814)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient54" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="145.01958" y1="24.0648" x2="148.92474" y2="19.325005" /><linearGradient xlink:href="#linearGradient70" id="linearGradient55" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="152.00311" y1="23.510586" x2="157.09706" y2="17.924889" /><linearGradient xlink:href="#linearGradient70" id="linearGradient56" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="139.66898" y1="34.298935" x2="148.91502" y2="24.094034" /><linearGradient xlink:href="#linearGradient70" id="linearGradient57" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="150.92365" y1="34.486496" x2="160.32947" y2="26.142387" /><linearGradient xlink:href="#linearGradient70" id="linearGradient72" x1="155.09953" y1="28.766298" x2="160.79262" y2="28.766298" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient73" x1="149.03021" y1="28.757526" x2="154.17104" y2="28.757526" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient74" x1="149.03001" y1="20.392658" x2="154.17073" y2="20.392658" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient75" x1="155.09943" y1="19.961107" x2="160.79259" y2="19.961107" gradientUnits="userSpaceOnUse" /></defs><g id="layer2" transform="translate(-142.39713,-1.5863839)"><path style="fill:#968334;fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 198.60245,45.193143 -0.0661,-9.98802 -13.95677,1.124479 v 11.112499 z" id="path76" /><path id="path77" style="fill:#968334;fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 184.58344,43.618976 0.0583,3.696537 h -23.0349 l 0.0187,-5.481645 z" /><path style="fill:#968334;fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 147.79386,45.112527 0.0661,-9.98802 13.95677,1.124479 v 11.112499 z" id="path78" /><path id="path75" style="fill:#42403e;fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 200.79629,15.944435 -16.06221,-1.343101 h -23.66934 l -14.5044,1.343101 27.11797,-10.9746084 z" /><path style="fill:url(#pattern14);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 198.60245,45.193143 -0.0661,-9.98802 -13.95677,1.124479 v 11.112499 z" id="path13" /><path id="rect30" style="fill:url(#pattern10);fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 184.58344,43.618976 0.0583,3.696537 h -23.0349 l 0.0187,-5.481645 z" /><path id="path25" style="fill:url(#pattern67);fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 200.79629,15.944435 -16.06221,-1.343101 h -23.66934 l -14.5044,1.343101 27.11797,-10.9746084 z" /><path id="rect25" style="fill:#302c2a;fill-opacity:1;stroke:none;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 146.64253,15.977569 14.73106,-1.226469 h 23.3848 l 15.81024,1.226469 v 1.546345 l -15.86856,-1.226469 h -23.38479 l -14.67275,1.226469 z" /><rect style="fill:#e5e5e5;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26" width="22.803343" height="27.902233" x="161.83841" y="16.331261" /><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect2" width="10.649479" height="26.127604" x="162.71873" y="16.999477" /><rect style="opacity:0.579137;fill:url(#linearGradient11);fill-opacity:1;stroke:#787666;stroke-width:0.0915985;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27" width="7.9183006" height="23.873291" x="164.11497" y="18.145884" /><path style="fill:url(#pattern13);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 147.79386,45.112527 0.0661,-9.98802 13.95677,1.124479 v 11.112499 z" id="path11" /><rect style="fill:#f6f6f6;fill-opacity:1;stroke:#414141;stroke-width:0.0739189;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29" width="28.63773" height="0.66228044" x="159.07536" y="43.558125" rx="1.3306036" /><path style="fill:none;fill-opacity:1;stroke:#484848;stroke-width:0.349206;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 162.508,13.647747 11.06827,-7.6286199 10.62175,7.7935629" id="path40" /><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect3" width="10.649479" height="26.127604" x="173.30208" y="16.999477" /><rect style="opacity:0.579137;fill:url(#linearGradient14);fill-opacity:1;stroke:#787666;stroke-width:0.0915985;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27-2" width="7.9183006" height="23.873291" x="174.67079" y="18.037466" /><rect style="fill:#e5e5e5;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect4" width="0.52916974" height="26.309505" x="172.93828" y="16.900259" /><path id="rect14" style="fill:#e5e5e5;stroke-width:1.13801;stroke-linecap:square;paint-order:markers fill stroke" d="m 148.26509,17.630418 13.55405,-1.261677 v 19.680735 l -13.55325,-0.769448 z" /><path id="rect28" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 148.77929,18.605389 5.75537,-0.485973 1e-4,4.251266 -5.7553,0.288721 z" /><path id="rect15" style="opacity:0.656;fill:url(#linearGradient74);fill-opacity:1;stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 149.03002,19.04074 5.14062,-0.414267 9e-5,3.253325 -5.14058,0.279045 z" /><path id="rect31" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 154.77794,18.098874 6.36961,-0.537837 1e-5,4.477906 -6.36953,0.319534 z" /><path id="rect16" style="opacity:0.656;fill:url(#linearGradient75);fill-opacity:1;stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 155.09942,18.551626 5.69314,-0.458793 2e-5,3.427512 -5.69309,0.309037 z" /><path id="rect33" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 148.7168,23.217872 5.74904,-0.261403 2.8e-4,11.550378 -5.74884,-0.274199 z" /><path id="rect17" style="opacity:0.656;fill:url(#linearGradient73);fill-opacity:1;stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 149.03022,23.660128 5.14054,-0.213939 2.8e-4,10.622674 -5.14039,-0.22756 z" /><path id="rect32" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 154.77805,22.942272 6.36951,-0.289615 3e-5,12.172873 -6.36927,-0.303791 z" /><path id="rect18" style="opacity:0.656;fill:url(#linearGradient72);fill-opacity:1;stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 155.09953,23.407536 5.69305,-0.236934 4e-5,11.191393 -5.69285,-0.252017 z" /><path id="path34" style="fill:#e5e5e5;stroke-width:1.13801;stroke-linecap:square;paint-order:markers fill stroke" d="m 198.16913,17.630418 -13.55405,-1.261677 v 19.680735 l 13.55325,-0.769448 z" /><path id="path35" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.65494,18.605389 -5.75538,-0.485973 -1e-4,4.251266 5.7553,0.288721 z" /><path id="path36" style="opacity:0.656;fill:url(#linearGradient54);stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.4042,19.04074 -5.14062,-0.414267 -9e-5,3.253325 5.14058,0.279045 z" /><path id="path37" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.65628,18.098874 -6.36961,-0.537837 -10e-6,4.477906 6.36953,0.319534 z" /><path id="path38" style="opacity:0.656;fill:url(#linearGradient55);stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.3348,18.551626 -5.69314,-0.458793 -2e-5,3.427512 5.69309,0.309037 z" /><path id="path39" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.71742,23.217872 -5.74903,-0.261403 -2.9e-4,11.550378 5.74884,-0.274199 z" /><path id="path41" style="opacity:0.656;fill:url(#linearGradient56);stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.404,23.660128 -5.14054,-0.213939 -2.8e-4,10.622674 5.14039,-0.22756 z" /><path id="path42" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.65617,22.942272 -6.36951,-0.289615 -3e-5,12.172873 6.36927,-0.303791 z" /><path id="path53" style="opacity:0.656;fill:url(#linearGradient57);stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.33469,23.407536 -5.69305,-0.236934 -4e-5,11.191393 5.69285,-0.252017 z" /></g></svg>

                '''
            },
            {
                'order': 2,
                "text": 'Lorem Ipsum Dolar Amet',
                "svg" : '''                         
                    <svg width="243.88751" height="184.9209" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1"><linearGradient id="linearGradient70"><stop style="stop-color:#6dabcf;stop-opacity:1;" offset="0" id="stop67" /><stop style="stop-color:#5fb0e6;stop-opacity:0.50588232;" offset="0.45308921" id="stop68" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop70" /></linearGradient><pattern xlink:href="#Strips1_5" preserveAspectRatio="xMidYMid" id="pattern67" patternTransform="matrix(0,0.1,-0.1,0,0,0)" x="0" y="0" /><pattern patternUnits="userSpaceOnUse" width="6" height="1" patternTransform="translate(0,0) scale(2,2)" preserveAspectRatio="xMidYMid" id="Strips1_5" style="fill:#000000">&#10;      <rect style="stroke:none" x="0" y="-0.5" width="1" height="2" id="rect164" />&#10;    </pattern><linearGradient id="linearGradient64"><stop style="stop-color:#a3c9e1;stop-opacity:1;" offset="0" id="stop61" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop62" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop63" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop64" /></linearGradient><linearGradient id="linearGradient60"><stop style="stop-color:#8cbed9;stop-opacity:1;" offset="0" id="stop57" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop58" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop59" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop60" /></linearGradient><pattern xlink:href="#pattern13" preserveAspectRatio="xMidYMid" id="pattern14" patternTransform="matrix(-0.01995129,0.00139513,-0.00139513,-0.01995129,0,0)" x="0" y="0" /><pattern xlink:href="#Bricks" id="pattern13" patternTransform="matrix(0.01995129,0.00139513,-0.00139513,0.01995129,0.42094947,-11.739813)" x="0" y="0" preserveAspectRatio="xMidYMid" /><pattern xlink:href="#Bricks" id="pattern10" patternTransform="scale(0.02)" x="0" y="0" preserveAspectRatio="none" /><pattern patternUnits="userSpaceOnUse" width="100" height="100" id="Bricks" style="fill:#935219" patternTransform="scale(0.25,0.25)"><g id="g13367"><rect style="fill:none;stroke:none;stroke-width:0" id="rect13349" width="100" height="100" x="0" y="0" /><rect style="fill-opacity:1;stroke-width:0" id="rect13351" width="40" height="40" x="0" y="60" /><rect style="fill-opacity:1;stroke-width:0" id="rect13353" width="90" height="40" x="0" y="10" /><rect style="fill-opacity:1;stroke-width:0" id="rect13355" width="50" height="40" x="50" y="60" /></g></pattern><linearGradient xlink:href="#linearGradient60" id="linearGradient11" x1="167.06261" y1="27.089109" x2="173.57579" y2="31.392151" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient64" id="linearGradient14" gradientUnits="userSpaceOnUse" x1="167.06261" y1="27.089109" x2="173.57579" y2="31.392151" gradientTransform="translate(10.555822,-0.10841814)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient54" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="145.01958" y1="24.0648" x2="148.92474" y2="19.325005" /><linearGradient xlink:href="#linearGradient70" id="linearGradient55" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="152.00311" y1="23.510586" x2="157.09706" y2="17.924889" /><linearGradient xlink:href="#linearGradient70" id="linearGradient56" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="139.66898" y1="34.298935" x2="148.91502" y2="24.094034" /><linearGradient xlink:href="#linearGradient70" id="linearGradient57" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="150.92365" y1="34.486496" x2="160.32947" y2="26.142387" /><linearGradient xlink:href="#linearGradient70" id="linearGradient72" x1="155.09953" y1="28.766298" x2="160.79262" y2="28.766298" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient73" x1="149.03021" y1="28.757526" x2="154.17104" y2="28.757526" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient74" x1="149.03001" y1="20.392658" x2="154.17073" y2="20.392658" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient75" x1="155.09943" y1="19.961107" x2="160.79259" y2="19.961107" gradientUnits="userSpaceOnUse" /></defs><g id="layer2" transform="translate(-142.39713,-1.5863839)"><path style="fill:#968334;fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 198.60245,45.193143 -0.0661,-9.98802 -13.95677,1.124479 v 11.112499 z" id="path76" /><path id="path77" style="fill:#968334;fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 184.58344,43.618976 0.0583,3.696537 h -23.0349 l 0.0187,-5.481645 z" /><path style="fill:#968334;fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 147.79386,45.112527 0.0661,-9.98802 13.95677,1.124479 v 11.112499 z" id="path78" /><path id="path75" style="fill:#42403e;fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 200.79629,15.944435 -16.06221,-1.343101 h -23.66934 l -14.5044,1.343101 27.11797,-10.9746084 z" /><path style="fill:url(#pattern14);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 198.60245,45.193143 -0.0661,-9.98802 -13.95677,1.124479 v 11.112499 z" id="path13" /><path id="rect30" style="fill:url(#pattern10);fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 184.58344,43.618976 0.0583,3.696537 h -23.0349 l 0.0187,-5.481645 z" /><path id="path25" style="fill:url(#pattern67);fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 200.79629,15.944435 -16.06221,-1.343101 h -23.66934 l -14.5044,1.343101 27.11797,-10.9746084 z" /><path id="rect25" style="fill:#302c2a;fill-opacity:1;stroke:none;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 146.64253,15.977569 14.73106,-1.226469 h 23.3848 l 15.81024,1.226469 v 1.546345 l -15.86856,-1.226469 h -23.38479 l -14.67275,1.226469 z" /><rect style="fill:#e5e5e5;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26" width="22.803343" height="27.902233" x="161.83841" y="16.331261" /><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect2" width="10.649479" height="26.127604" x="162.71873" y="16.999477" /><rect style="opacity:0.579137;fill:url(#linearGradient11);fill-opacity:1;stroke:#787666;stroke-width:0.0915985;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27" width="7.9183006" height="23.873291" x="164.11497" y="18.145884" /><path style="fill:url(#pattern13);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 147.79386,45.112527 0.0661,-9.98802 13.95677,1.124479 v 11.112499 z" id="path11" /><rect style="fill:#f6f6f6;fill-opacity:1;stroke:#414141;stroke-width:0.0739189;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29" width="28.63773" height="0.66228044" x="159.07536" y="43.558125" rx="1.3306036" /><path style="fill:none;fill-opacity:1;stroke:#484848;stroke-width:0.349206;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 162.508,13.647747 11.06827,-7.6286199 10.62175,7.7935629" id="path40" /><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect3" width="10.649479" height="26.127604" x="173.30208" y="16.999477" /><rect style="opacity:0.579137;fill:url(#linearGradient14);fill-opacity:1;stroke:#787666;stroke-width:0.0915985;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27-2" width="7.9183006" height="23.873291" x="174.67079" y="18.037466" /><rect style="fill:#e5e5e5;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect4" width="0.52916974" height="26.309505" x="172.93828" y="16.900259" /><path id="rect14" style="fill:#e5e5e5;stroke-width:1.13801;stroke-linecap:square;paint-order:markers fill stroke" d="m 148.26509,17.630418 13.55405,-1.261677 v 19.680735 l -13.55325,-0.769448 z" /><path id="rect28" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 148.77929,18.605389 5.75537,-0.485973 1e-4,4.251266 -5.7553,0.288721 z" /><path id="rect15" style="opacity:0.656;fill:url(#linearGradient74);fill-opacity:1;stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 149.03002,19.04074 5.14062,-0.414267 9e-5,3.253325 -5.14058,0.279045 z" /><path id="rect31" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 154.77794,18.098874 6.36961,-0.537837 1e-5,4.477906 -6.36953,0.319534 z" /><path id="rect16" style="opacity:0.656;fill:url(#linearGradient75);fill-opacity:1;stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 155.09942,18.551626 5.69314,-0.458793 2e-5,3.427512 -5.69309,0.309037 z" /><path id="rect33" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 148.7168,23.217872 5.74904,-0.261403 2.8e-4,11.550378 -5.74884,-0.274199 z" /><path id="rect17" style="opacity:0.656;fill:url(#linearGradient73);fill-opacity:1;stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 149.03022,23.660128 5.14054,-0.213939 2.8e-4,10.622674 -5.14039,-0.22756 z" /><path id="rect32" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 154.77805,22.942272 6.36951,-0.289615 3e-5,12.172873 -6.36927,-0.303791 z" /><path id="rect18" style="opacity:0.656;fill:url(#linearGradient72);fill-opacity:1;stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 155.09953,23.407536 5.69305,-0.236934 4e-5,11.191393 -5.69285,-0.252017 z" /><path id="path34" style="fill:#e5e5e5;stroke-width:1.13801;stroke-linecap:square;paint-order:markers fill stroke" d="m 198.16913,17.630418 -13.55405,-1.261677 v 19.680735 l 13.55325,-0.769448 z" /><path id="path35" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.65494,18.605389 -5.75538,-0.485973 -1e-4,4.251266 5.7553,0.288721 z" /><path id="path36" style="opacity:0.656;fill:url(#linearGradient54);stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.4042,19.04074 -5.14062,-0.414267 -9e-5,3.253325 5.14058,0.279045 z" /><path id="path37" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.65628,18.098874 -6.36961,-0.537837 -10e-6,4.477906 6.36953,0.319534 z" /><path id="path38" style="opacity:0.656;fill:url(#linearGradient55);stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.3348,18.551626 -5.69314,-0.458793 -2e-5,3.427512 5.69309,0.309037 z" /><path id="path39" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.71742,23.217872 -5.74903,-0.261403 -2.9e-4,11.550378 5.74884,-0.274199 z" /><path id="path41" style="opacity:0.656;fill:url(#linearGradient56);stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.404,23.660128 -5.14054,-0.213939 -2.8e-4,10.622674 5.14039,-0.22756 z" /><path id="path42" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.65617,22.942272 -6.36951,-0.289615 -3e-5,12.172873 6.36927,-0.303791 z" /><path id="path53" style="opacity:0.656;fill:url(#linearGradient57);stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.33469,23.407536 -5.69305,-0.236934 -4e-5,11.191393 5.69285,-0.252017 z" /></g></svg>

                '''
            },
            {
                'order': 3,
                "text": 'Lorem Ipsum Dolar Amet',
                "svg" : '''                         
                    <svg width="243.88751" height="184.9209" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1"><linearGradient id="linearGradient70"><stop style="stop-color:#6dabcf;stop-opacity:1;" offset="0" id="stop67" /><stop style="stop-color:#5fb0e6;stop-opacity:0.50588232;" offset="0.45308921" id="stop68" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop70" /></linearGradient><pattern xlink:href="#Strips1_5" preserveAspectRatio="xMidYMid" id="pattern67" patternTransform="matrix(0,0.1,-0.1,0,0,0)" x="0" y="0" /><pattern patternUnits="userSpaceOnUse" width="6" height="1" patternTransform="translate(0,0) scale(2,2)" preserveAspectRatio="xMidYMid" id="Strips1_5" style="fill:#000000">&#10;      <rect style="stroke:none" x="0" y="-0.5" width="1" height="2" id="rect164" />&#10;    </pattern><linearGradient id="linearGradient64"><stop style="stop-color:#a3c9e1;stop-opacity:1;" offset="0" id="stop61" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop62" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop63" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop64" /></linearGradient><linearGradient id="linearGradient60"><stop style="stop-color:#8cbed9;stop-opacity:1;" offset="0" id="stop57" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop58" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop59" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop60" /></linearGradient><pattern xlink:href="#pattern13" preserveAspectRatio="xMidYMid" id="pattern14" patternTransform="matrix(-0.01995129,0.00139513,-0.00139513,-0.01995129,0,0)" x="0" y="0" /><pattern xlink:href="#Bricks" id="pattern13" patternTransform="matrix(0.01995129,0.00139513,-0.00139513,0.01995129,0.42094947,-11.739813)" x="0" y="0" preserveAspectRatio="xMidYMid" /><pattern xlink:href="#Bricks" id="pattern10" patternTransform="scale(0.02)" x="0" y="0" preserveAspectRatio="none" /><pattern patternUnits="userSpaceOnUse" width="100" height="100" id="Bricks" style="fill:#935219" patternTransform="scale(0.25,0.25)"><g id="g13367"><rect style="fill:none;stroke:none;stroke-width:0" id="rect13349" width="100" height="100" x="0" y="0" /><rect style="fill-opacity:1;stroke-width:0" id="rect13351" width="40" height="40" x="0" y="60" /><rect style="fill-opacity:1;stroke-width:0" id="rect13353" width="90" height="40" x="0" y="10" /><rect style="fill-opacity:1;stroke-width:0" id="rect13355" width="50" height="40" x="50" y="60" /></g></pattern><linearGradient xlink:href="#linearGradient60" id="linearGradient11" x1="167.06261" y1="27.089109" x2="173.57579" y2="31.392151" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient64" id="linearGradient14" gradientUnits="userSpaceOnUse" x1="167.06261" y1="27.089109" x2="173.57579" y2="31.392151" gradientTransform="translate(10.555822,-0.10841814)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient54" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="145.01958" y1="24.0648" x2="148.92474" y2="19.325005" /><linearGradient xlink:href="#linearGradient70" id="linearGradient55" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="152.00311" y1="23.510586" x2="157.09706" y2="17.924889" /><linearGradient xlink:href="#linearGradient70" id="linearGradient56" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="139.66898" y1="34.298935" x2="148.91502" y2="24.094034" /><linearGradient xlink:href="#linearGradient70" id="linearGradient57" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="150.92365" y1="34.486496" x2="160.32947" y2="26.142387" /><linearGradient xlink:href="#linearGradient70" id="linearGradient72" x1="155.09953" y1="28.766298" x2="160.79262" y2="28.766298" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient73" x1="149.03021" y1="28.757526" x2="154.17104" y2="28.757526" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient74" x1="149.03001" y1="20.392658" x2="154.17073" y2="20.392658" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient75" x1="155.09943" y1="19.961107" x2="160.79259" y2="19.961107" gradientUnits="userSpaceOnUse" /></defs><g id="layer2" transform="translate(-142.39713,-1.5863839)"><path style="fill:#968334;fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 198.60245,45.193143 -0.0661,-9.98802 -13.95677,1.124479 v 11.112499 z" id="path76" /><path id="path77" style="fill:#968334;fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 184.58344,43.618976 0.0583,3.696537 h -23.0349 l 0.0187,-5.481645 z" /><path style="fill:#968334;fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 147.79386,45.112527 0.0661,-9.98802 13.95677,1.124479 v 11.112499 z" id="path78" /><path id="path75" style="fill:#42403e;fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 200.79629,15.944435 -16.06221,-1.343101 h -23.66934 l -14.5044,1.343101 27.11797,-10.9746084 z" /><path style="fill:url(#pattern14);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 198.60245,45.193143 -0.0661,-9.98802 -13.95677,1.124479 v 11.112499 z" id="path13" /><path id="rect30" style="fill:url(#pattern10);fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 184.58344,43.618976 0.0583,3.696537 h -23.0349 l 0.0187,-5.481645 z" /><path id="path25" style="fill:url(#pattern67);fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 200.79629,15.944435 -16.06221,-1.343101 h -23.66934 l -14.5044,1.343101 27.11797,-10.9746084 z" /><path id="rect25" style="fill:#302c2a;fill-opacity:1;stroke:none;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 146.64253,15.977569 14.73106,-1.226469 h 23.3848 l 15.81024,1.226469 v 1.546345 l -15.86856,-1.226469 h -23.38479 l -14.67275,1.226469 z" /><rect style="fill:#e5e5e5;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26" width="22.803343" height="27.902233" x="161.83841" y="16.331261" /><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect2" width="10.649479" height="26.127604" x="162.71873" y="16.999477" /><rect style="opacity:0.579137;fill:url(#linearGradient11);fill-opacity:1;stroke:#787666;stroke-width:0.0915985;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27" width="7.9183006" height="23.873291" x="164.11497" y="18.145884" /><path style="fill:url(#pattern13);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 147.79386,45.112527 0.0661,-9.98802 13.95677,1.124479 v 11.112499 z" id="path11" /><rect style="fill:#f6f6f6;fill-opacity:1;stroke:#414141;stroke-width:0.0739189;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29" width="28.63773" height="0.66228044" x="159.07536" y="43.558125" rx="1.3306036" /><path style="fill:none;fill-opacity:1;stroke:#484848;stroke-width:0.349206;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 162.508,13.647747 11.06827,-7.6286199 10.62175,7.7935629" id="path40" /><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect3" width="10.649479" height="26.127604" x="173.30208" y="16.999477" /><rect style="opacity:0.579137;fill:url(#linearGradient14);fill-opacity:1;stroke:#787666;stroke-width:0.0915985;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27-2" width="7.9183006" height="23.873291" x="174.67079" y="18.037466" /><rect style="fill:#e5e5e5;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect4" width="0.52916974" height="26.309505" x="172.93828" y="16.900259" /><path id="rect14" style="fill:#e5e5e5;stroke-width:1.13801;stroke-linecap:square;paint-order:markers fill stroke" d="m 148.26509,17.630418 13.55405,-1.261677 v 19.680735 l -13.55325,-0.769448 z" /><path id="rect28" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 148.77929,18.605389 5.75537,-0.485973 1e-4,4.251266 -5.7553,0.288721 z" /><path id="rect15" style="opacity:0.656;fill:url(#linearGradient74);fill-opacity:1;stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 149.03002,19.04074 5.14062,-0.414267 9e-5,3.253325 -5.14058,0.279045 z" /><path id="rect31" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 154.77794,18.098874 6.36961,-0.537837 1e-5,4.477906 -6.36953,0.319534 z" /><path id="rect16" style="opacity:0.656;fill:url(#linearGradient75);fill-opacity:1;stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 155.09942,18.551626 5.69314,-0.458793 2e-5,3.427512 -5.69309,0.309037 z" /><path id="rect33" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 148.7168,23.217872 5.74904,-0.261403 2.8e-4,11.550378 -5.74884,-0.274199 z" /><path id="rect17" style="opacity:0.656;fill:url(#linearGradient73);fill-opacity:1;stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 149.03022,23.660128 5.14054,-0.213939 2.8e-4,10.622674 -5.14039,-0.22756 z" /><path id="rect32" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 154.77805,22.942272 6.36951,-0.289615 3e-5,12.172873 -6.36927,-0.303791 z" /><path id="rect18" style="opacity:0.656;fill:url(#linearGradient72);fill-opacity:1;stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 155.09953,23.407536 5.69305,-0.236934 4e-5,11.191393 -5.69285,-0.252017 z" /><path id="path34" style="fill:#e5e5e5;stroke-width:1.13801;stroke-linecap:square;paint-order:markers fill stroke" d="m 198.16913,17.630418 -13.55405,-1.261677 v 19.680735 l 13.55325,-0.769448 z" /><path id="path35" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.65494,18.605389 -5.75538,-0.485973 -1e-4,4.251266 5.7553,0.288721 z" /><path id="path36" style="opacity:0.656;fill:url(#linearGradient54);stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.4042,19.04074 -5.14062,-0.414267 -9e-5,3.253325 5.14058,0.279045 z" /><path id="path37" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.65628,18.098874 -6.36961,-0.537837 -10e-6,4.477906 6.36953,0.319534 z" /><path id="path38" style="opacity:0.656;fill:url(#linearGradient55);stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.3348,18.551626 -5.69314,-0.458793 -2e-5,3.427512 5.69309,0.309037 z" /><path id="path39" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.71742,23.217872 -5.74903,-0.261403 -2.9e-4,11.550378 5.74884,-0.274199 z" /><path id="path41" style="opacity:0.656;fill:url(#linearGradient56);stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.404,23.660128 -5.14054,-0.213939 -2.8e-4,10.622674 5.14039,-0.22756 z" /><path id="path42" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.65617,22.942272 -6.36951,-0.289615 -3e-5,12.172873 6.36927,-0.303791 z" /><path id="path53" style="opacity:0.656;fill:url(#linearGradient57);stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.33469,23.407536 -5.69305,-0.236934 -4e-5,11.191393 5.69285,-0.252017 z" /></g></svg>

                '''
            }
        ]
    } ,
    {
        'tag' : 'about-skills',
        'section_id': 5, 
        'items': [
            {
                'order': 0,
                'text': 'Roof Conversions',
                'subtext': '98',
            },
            {
                'order': 1,
                'text': 'Garden Rooms',
                'subtext': '95',
            },
            {
                'order': 2,
                'text': 'Interior Design',
                'subtext': '92',
            },
        ]
    },
    {
        'tag': 'about-numbers',
        'section_id': 5,
        'items' : [
            {
                'order' : 0,
                'text': 'Residential Projects',
                'subtext': '1613',
                'svg' : '''
                    <svg width="40px" height="40px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M11.8903 9.11013L6.52606 3.74585C6.13004 3.34983 5.93203 3.15182 5.7037 3.07763C5.50286 3.01237 5.28651 3.01237 5.08567 3.07763C4.85734 3.15182 4.65933 3.34983 4.26331 3.74584L3.69763 4.31153C3.30161 4.70755 3.1036 4.90555 3.02941 5.13388C2.96415 5.33473 2.96415 5.55107 3.02941 5.75192C3.1036 5.98024 3.30161 6.17826 3.69763 6.57427L9.06192 11.9386M14.7188 11.9386L20.0828 17.3026C20.4788 17.6986 20.6768 17.8966 20.751 18.125C20.8163 18.3258 20.8163 18.5422 20.751 18.743C20.6768 18.9713 20.4788 19.1693 20.0828 19.5654L19.5171 20.131C19.1211 20.5271 18.9231 20.7251 18.6948 20.7993C18.4939 20.8645 18.2776 20.8645 18.0767 20.7993C17.8484 20.7251 17.6504 20.5271 17.2544 20.131L11.8903 14.767M8.00024 6.99968L8.88946 6.10925M17.0002 15.9999L17.8945 15.1143M15.4998 5.50202L18.3282 8.33044M3 21.0018L3.04745 20.6696C3.21536 19.4942 3.29932 18.9066 3.49029 18.3579C3.65975 17.871 3.89124 17.408 4.17906 16.9803C4.50341 16.4984 4.92319 16.0786 5.76274 15.239L17.4107 3.59104C18.1918 2.80999 19.4581 2.80999 20.2392 3.59103C21.0202 4.37208 21.0202 5.63841 20.2392 6.41946L8.37744 18.2812C7.61579 19.0428 7.23497 19.4237 6.8012 19.7265C6.41618 19.9953 6.00093 20.218 5.56398 20.39C5.07171 20.5838 4.54375 20.6903 3.48793 20.9033L3 21.0018Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                '''
            },
            {
                'order' : 1,

                'text': 'Satisfied Customers',
                'subtext': '2507',
                'svg' : '''
                    <svg width="40px" height="40px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M8.4 13.8C8.4 13.8 9.75 15.6 12 15.6C14.25 15.6 15.6 13.8 15.6 13.8M14.7 9.3H14.709M9.3 9.3H9.309M21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12ZM15.15 9.3C15.15 9.54853 14.9485 9.75 14.7 9.75C14.4515 9.75 14.25 9.54853 14.25 9.3C14.25 9.05147 14.4515 8.85 14.7 8.85C14.9485 8.85 15.15 9.05147 15.15 9.3ZM9.75 9.3C9.75 9.54853 9.54853 9.75 9.3 9.75C9.05147 9.75 8.85 9.54853 8.85 9.3C8.85 9.05147 9.05147 8.85 9.3 8.85C9.54853 8.85 9.75 9.05147 9.75 9.3Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                '''
            },
            {
                'order' : 2,
                'text': 'Certifications',
                'subtext': '5',
                'svg' : '''
                    <svg width="40px" height="40px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M13 3H8.2C7.0799 3 6.51984 3 6.09202 3.21799C5.71569 3.40973 5.40973 3.71569 5.21799 4.09202C5 4.51984 5 5.0799 5 6.2V17.8C5 18.9201 5 19.4802 5.21799 19.908C5.40973 20.2843 5.71569 20.5903 6.09202 20.782C6.51984 21 7.0799 21 8.2 21H12M13 3L19 9M13 3V7.4C13 7.96005 13 8.24008 13.109 8.45399C13.2049 8.64215 13.3578 8.79513 13.546 8.89101C13.7599 9 14.0399 9 14.6 9H19M19 9V10M9 17H12M9 13H12M9 9H10M16 14H21V21L18.5 19.611L16 21V14Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>                
                '''
            },
            {
                'order' : 3,
                'text': 'National Awards',
                'subtext': '1',
                'svg': '''
                    <svg width="40px" height="40px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 3L12.4892 2.12785C12.1854 1.95738 11.8146 1.95738 11.5108 2.12785L12 3ZM13.3976 3.784L12.9084 4.65615C13.0542 4.73792 13.2181 4.78185 13.3852 4.78392L13.3976 3.784ZM15 3.80385L15.8598 3.29316C15.6818 2.99359 15.3608 2.80824 15.0124 2.80392L15 3.80385ZM15.8184 5.18162L14.9586 5.69231C15.044 5.83601 15.164 5.95603 15.3077 6.04139L15.8184 5.18162ZM17.1962 6L18.1961 5.98761C18.1918 5.63921 18.0064 5.31817 17.7068 5.14023L17.1962 6ZM17.216 7.60238L16.2161 7.61476C16.2181 7.78189 16.2621 7.94584 16.3438 8.09161L17.216 7.60238ZM18 9L18.8722 9.48924C19.0426 9.18535 19.0426 8.81465 18.8722 8.51076L18 9ZM17.216 10.3976L16.3438 9.90839C16.2621 10.0542 16.2181 10.2181 16.2161 10.3852L17.216 10.3976ZM17.1962 12L17.7068 12.8598C18.0064 12.6818 18.1918 12.3608 18.1961 12.0124L17.1962 12ZM15.8184 12.8184L15.3077 11.9586C15.164 12.044 15.044 12.164 14.9586 12.3077L15.8184 12.8184ZM15 14.1962L15.0124 15.1961C15.3608 15.1918 15.6818 15.0064 15.8598 14.7068L15 14.1962ZM13.3976 14.216L13.3852 13.2161C13.2181 13.2181 13.0542 13.2621 12.9084 13.3438L13.3976 14.216ZM12 15L11.5108 15.8722C11.8146 16.0426 12.1854 16.0426 12.4892 15.8722L12 15ZM10.6024 14.216L11.0916 13.3438C10.9458 13.2621 10.7819 13.2181 10.6148 13.2161L10.6024 14.216ZM9 14.1962L8.14023 14.7068C8.31817 15.0064 8.63921 15.1918 8.98761 15.1961L9 14.1962ZM8.18162 12.8184L9.04139 12.3077C8.95603 12.164 8.83602 12.044 8.69231 11.9586L8.18162 12.8184ZM6.80385 12L5.80392 12.0124C5.80824 12.3608 5.99359 12.6818 6.29316 12.8598L6.80385 12ZM6.784 10.3976L7.78392 10.3852C7.78185 10.2181 7.73792 10.0542 7.65615 9.90839L6.784 10.3976ZM6 9L5.12785 8.51076C4.95738 8.81465 4.95738 9.18535 5.12785 9.48924L6 9ZM6.784 7.60238L7.65615 8.09161C7.73792 7.94584 7.78185 7.78189 7.78392 7.61476L6.784 7.60238ZM6.80385 6L6.29316 5.14023C5.99359 5.31817 5.80824 5.63921 5.80392 5.98762L6.80385 6ZM8.18162 5.18162L8.69231 6.04139C8.83602 5.95603 8.95603 5.83602 9.04139 5.69231L8.18162 5.18162ZM9 3.80385L8.98762 2.80392C8.63921 2.80824 8.31817 2.99359 8.14023 3.29316L9 3.80385ZM10.6024 3.784L10.6148 4.78392C10.7819 4.78185 10.9458 4.73792 11.0916 4.65615L10.6024 3.784ZM4 19L3.10557 18.5528C2.95058 18.8628 2.96714 19.2309 3.14935 19.5258C3.33156 19.8206 3.65342 20 4 20V19ZM6.5 19L7.3 18.4C7.11115 18.1482 6.81476 18 6.5 18V19ZM8 21L7.2 21.6C7.40795 21.8773 7.74463 22.0271 8.08981 21.996C8.43498 21.9649 8.73943 21.7572 8.89443 21.4472L8 21ZM20 19V20C20.3466 20 20.6684 19.8206 20.8507 19.5258C21.0329 19.2309 21.0494 18.8628 20.8944 18.5528L20 19ZM17.5 19V18C17.1852 18 16.8889 18.1482 16.7 18.4L17.5 19ZM16 21L15.1056 21.4472C15.2606 21.7572 15.565 21.9649 15.9102 21.996C16.2554 22.0271 16.5921 21.8773 16.8 21.6L16 21ZM19.3944 15.5528C19.1474 15.0588 18.5468 14.8586 18.0528 15.1056C17.5588 15.3526 17.3586 15.9533 17.6056 16.4472L19.3944 15.5528ZM15.3944 17.5528C15.1474 17.0588 14.5468 16.8586 14.0528 17.1056C13.5588 17.3526 13.3586 17.9533 13.6056 18.4472L15.3944 17.5528ZM10.3944 18.4472C10.6414 17.9533 10.4412 17.3526 9.94721 17.1056C9.45324 16.8586 8.85256 17.0588 8.60557 17.5528L10.3944 18.4472ZM6.39443 16.4472C6.64142 15.9533 6.44119 15.3526 5.94721 15.1056C5.45324 14.8586 4.85256 15.0588 4.60557 15.5528L6.39443 16.4472ZM11.5108 3.87215L12.9084 4.65615L13.8869 2.91185L12.4892 2.12785L11.5108 3.87215ZM13.3852 4.78392L14.9876 4.80377L15.0124 2.80392L13.41 2.78408L13.3852 4.78392ZM14.1402 4.31454L14.9586 5.69231L16.6781 4.67094L15.8598 3.29316L14.1402 4.31454ZM15.3077 6.04139L16.6855 6.85977L17.7068 5.14023L16.3291 4.32186L15.3077 6.04139ZM16.1962 6.01239L16.2161 7.61476L18.2159 7.58999L18.1961 5.98761L16.1962 6.01239ZM16.3438 8.09161L17.1278 9.48924L18.8722 8.51076L18.0882 7.11314L16.3438 8.09161ZM17.1278 8.51076L16.3438 9.90839L18.0882 10.8869L18.8722 9.48924L17.1278 8.51076ZM16.2161 10.3852L16.1962 11.9876L18.1961 12.0124L18.2159 10.41L16.2161 10.3852ZM14.9586 12.3077L14.1402 13.6855L15.8598 14.7068L16.6781 13.3291L14.9586 12.3077ZM14.9876 13.1962L13.3852 13.2161L13.41 15.2159L15.0124 15.1961L14.9876 13.1962ZM10.6148 13.2161L9.01239 13.1962L8.98761 15.1961L10.59 15.2159L10.6148 13.2161ZM9.85977 13.6855L9.04139 12.3077L7.32186 13.3291L8.14023 14.7068L9.85977 13.6855ZM7.80377 11.9876L7.78392 10.3852L5.78408 10.41L5.80392 12.0124L7.80377 11.9876ZM7.65615 9.90839L6.87215 8.51076L5.12785 9.48924L5.91185 10.8869L7.65615 9.90839ZM6.87215 9.48924L7.65615 8.09161L5.91185 7.11314L5.12785 8.51076L6.87215 9.48924ZM7.78392 7.61476L7.80377 6.01238L5.80392 5.98762L5.78408 7.58999L7.78392 7.61476ZM7.31454 6.85977L8.69231 6.04139L7.67094 4.32186L6.29316 5.14023L7.31454 6.85977ZM9.04139 5.69231L9.85977 4.31454L8.14023 3.29316L7.32186 4.67094L9.04139 5.69231ZM9.01238 4.80377L10.6148 4.78392L10.59 2.78408L8.98762 2.80392L9.01238 4.80377ZM11.0916 4.65615L12.4892 3.87215L11.5108 2.12785L10.1131 2.91185L11.0916 4.65615ZM16.6855 11.1402L15.3077 11.9586L16.3291 13.6781L17.7068 12.8598L16.6855 11.1402ZM8.69231 11.9586L7.31454 11.1402L6.29316 12.8598L7.67094 13.6781L8.69231 11.9586ZM12.9084 13.3438L11.5108 14.1278L12.4892 15.8722L13.8869 15.0882L12.9084 13.3438ZM12.4892 14.1278L11.0916 13.3438L10.1131 15.0882L11.5108 15.8722L12.4892 14.1278ZM4 20H6.5V18H4V20ZM5.7 19.6L7.2 21.6L8.8 20.4L7.3 18.4L5.7 19.6ZM20 18H17.5V20H20V18ZM16.7 18.4L15.2 20.4L16.8 21.6L18.3 19.6L16.7 18.4ZM17.6056 16.4472L19.1056 19.4472L20.8944 18.5528L19.3944 15.5528L17.6056 16.4472ZM13.6056 18.4472L15.1056 21.4472L16.8944 20.5528L15.3944 17.5528L13.6056 18.4472ZM8.60557 17.5528L7.10557 20.5528L8.89443 21.4472L10.3944 18.4472L8.60557 17.5528ZM4.60557 15.5528L3.10557 18.5528L4.89443 19.4472L6.39443 16.4472L4.60557 15.5528ZM13 9C13 9.55228 12.5523 10 12 10V12C13.6569 12 15 10.6569 15 9H13ZM12 10C11.4477 10 11 9.55228 11 9H9C9 10.6569 10.3431 12 12 12V10ZM11 9C11 8.44772 11.4477 8 12 8V6C10.3431 6 9 7.34315 9 9H11ZM12 8C12.5523 8 13 8.44772 13 9H15C15 7.34315 13.6569 6 12 6V8Z" fill="currentColor"/>
                    </svg>
                '''
            },
        ]
    },

    {
        'tag': 'service-construction',
        'section_id': 7,
        'title': 'Construction Quality', 
        'description': 'As active members of the Eurcell Group, We offer premium ranges of tiles offering the latest in temprature regulating technology.',
        'items' : [
            {
                'order' : 0,
                'text' : 'Premium Materials'
            },
            {
                'order' : 1,
                'text' : 'Industry Leading Tools'
            },
            {
                'order' : 2,
                'text' : 'Best Practices'
            },
            {
                'order' : 3,
                'text' : 'Industry Connections'
            },
            {
                'order' : 4,
                'text' : 'Wide Range of Tiles'
            },
            {
                'order' : 5,
                'text' : 'Multiple Glazing Options'
            },
            
        ]
    },
    {
        'tag': 'service-process',
        'section_id': 7,
        'title': 'Process Qaulity', 
        'description': 'Our vision is to be the most trusted impactful extension specialists in the south east, known for transforming external spaces.',
        'items' : [
            {
                'order' : 0,
                'text' : 'South East Coverage'
            },
            {
                'order' : 1,
                'text' : '24/7 Support'
            },
            {
                'order' : 2,
                'text' : 'Quick Installation'
            },
            {
                'order' : 3,
                'text' : 'Weather Proof Standard'
            },
            {
                'order' : 4,
                'text' : 'As Low as 5° Angle'
            },
            {
                'order' : 5,
                'text' : 'All Conservatory Shapes'
            },
            
        ]
    },

    {
        'section_id': 7,
        'tag': 'service-safety',
        'title': 'Certification & Safety', 
        'description': 'Our vision is to be the most trusted impactful extension specialists in the south east, known for transforming external spaces.',
        'items' : [
            {
                'order' : 0,
                'text' : 'LABC Certified'
            },
            {
                'order' : 1,
                'text' : 'LABSS Certified'
            },
            {
                'order' : 2,
                'text' : '10 Year Guarantee'
            },
            {
                'order' : 3,
                'text' : 'Eurocell Affiliate'
            },
            {
                'order' : 4,
                'text' : '24 Years Experience'
            },
            {
                'order' : 5,
                'text' : "98% Satisfied Customers"
            },
            
        ]
    },

    {
        'section_id': 8,
        'tag' : 'service-process',
        'items': [
            {
                'order' : 0,
                'text': 'Planning & Consultation',
                'subtext' : 'We operate around your needs and co-operate to create a working plan of action.'
            },
            {
                'order' : 1,
                'text': 'Design & Engineering',
                'subtext' : 'We ask you to  complete a tile and window selection process. for your perfect finish.'
            },
            {
                'order' : 2,
                'text': 'Construction Execution',
                'subtext' : 'A project can be complete in as little as two days! dependant on the user specification.'
            },
            {
                'order' : 3,
                'text': 'Inspection & Handover',
                'subtext' : 'We execcute frivolous testing on all of our roofs to ensure a P value below 0.5!'
            },
        ]
    },
    {
        'tag' : 'cmp-approval',
        'section_id' : 10,
        'description': 'BOTH LABC & JHAI APPROVED',
        'items': [
            {
                "text": "Yes",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "No",
                "order" : 1, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            {
                "text": "No",
                "order" : 2, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            
        ]
    },
    {
        'tag' : 'cmp-u-value',
        'section_id' : 10,
        'description': 'ACHIEVABLE 0.15 U VALUE SUPPLIED AS STANDARD, NO MATTER WHERE INSTALLED IN GREAT BRITAIN',
        'items': [
            {
                "text": "Yes",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "No",
                "order" : 1, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            {
                "text": "No",
                "order" : 2, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            
        ]
    },
    {
        'tag' : 'cmp-five-deg',
        'section_id' : 10,
        'description': 'SLATESKIN GRP SHEET TILE SYSTEM COMPATIBLE ALLOWING A PITCH AS LOW AS 5° (ON LEAN TO DESIGNS)',
        'items': [
            {
                "text": "Yes",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "No",
                "order" : 1, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            {
                "text": "No",
                "order" : 2, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            
        ]
    },
    {
        'tag' : 'cmp-slate-cut',
        'section_id' : 10,
        'description': 'SLATESKIN CUT TO SIZE FOR ALL ROOF KITS THAT CUTS TILING TIME DOWN BY UP TO 50%',
        'items': [
            {
                "text": "Yes",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "No",
                "order" : 1, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            {
                "text": "No",
                "order" : 2, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            
        ]
    },
    
    {
        'tag' : 'cmp-softfit-ringbeam',
        'section_id' : 10,
        'description': 'SOFFIT RINGBEAM AND EAVES WHICH CAN BE SUPPLIED WITH VARIABLE CCT DOWNLIGHTERS',
        'items': [
            {
                "text": "Yes",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "Some",
                "order" : 1, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4a8 8 0 1 0 0 16 8 8 0 0 0 0-16zM2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12z" fill="#0D0D0D"/><path d="M12 14a1 1 0 0 1-1-1V7a1 1 0 1 1 2 0v6a1 1 0 0 1-1 1zm-1.5 2.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0z" fill="#0D0D0D"/></svg>
                ''',         
            },
            {
                "text": "Some",
                "order" : 2, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4a8 8 0 1 0 0 16 8 8 0 0 0 0-16zM2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12z" fill="#0D0D0D"/><path d="M12 14a1 1 0 0 1-1-1V7a1 1 0 1 1 2 0v6a1 1 0 0 1-1 1zm-1.5 2.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0z" fill="#0D0D0D"/></svg>
                ''',         
            },
            
        ]
    },

     {
        'tag' : 'cmp-variable-pitch',
        'section_id' : 10,
        'description': 'FULLY VARIABLE PITCH SYSTEM CAPABLE OF HANDLING A RANGE BETWEEN 5° - 35° ON LEAN TO’S AND 15° - 35° ON RIDGED DESIGNS',
        'items': [
            {
                "text": "Yes",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "No",
                "order" : 1, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            {
                "text": "No",
                "order" : 2, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            
        ]
    },
    
    {
        'tag' : 'cmp-fixed-pitch',
        'section_id' : 10,
        'description': "FIXED PITCH LEAN TO’S AT 15° AND RIDGED DESIGNS AT 25° POSSIBLE TO REDUCE COST PRICES OF KITS.",
        'items': [
            {
                "text": "Yes",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "No",
                "order" : 1, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            {
                "text": "No",
                "order" : 2, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            
        ]
    },
    {
        'tag' : 'cmp-fully-ventilated',
        'section_id' : 10,
        'description': "FULLY VENTILATED SYSTEM FROM RING BEAM TO RIDGE / WALLPLATE",
        'items': [
            {
                "text": "Yes",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "Some",
                "order" : 1, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4a8 8 0 1 0 0 16 8 8 0 0 0 0-16zM2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12z" fill="#0D0D0D"/><path d="M12 14a1 1 0 0 1-1-1V7a1 1 0 1 1 2 0v6a1 1 0 0 1-1 1zm-1.5 2.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0z" fill="#0D0D0D"/></svg>
                ''',       
            },
            {
                "text": "No",
                "order" : 2, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            
        ]
    },
    {
        'tag' : 'cmp-site-assitance',
        'section_id' : 10,
        'description': "ON SITE ASSISTANCE ON BOTH SURVEYS AND INSTALLATIONS BY EUROCELL TECHNICAL ENGINEERS",
        'items': [
            {
                "text": "Yes",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "Some",
                "order" : 1, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4a8 8 0 1 0 0 16 8 8 0 0 0 0-16zM2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12z" fill="#0D0D0D"/><path d="M12 14a1 1 0 0 1-1-1V7a1 1 0 1 1 2 0v6a1 1 0 0 1-1 1zm-1.5 2.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0z" fill="#0D0D0D"/></svg>
                ''',       
            },
            {
                "text": "No",
                "order" : 2, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            
        ]
    },
    {
        'tag' : 'cmp-made-to-measure',
        'section_id' : 10,
        'description': "MADE TO MEASURE ROOF KITS SUPPLIED OUT OF THE FACTORY WITH AN ACHIEVABLE 5 DAY LEAD TIME",
        'items': [
            {
                "text": "Yes",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "Some",
                "order" : 1, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4a8 8 0 1 0 0 16 8 8 0 0 0 0-16zM2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12z" fill="#0D0D0D"/><path d="M12 14a1 1 0 0 1-1-1V7a1 1 0 1 1 2 0v6a1 1 0 0 1-1 1zm-1.5 2.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0z" fill="#0D0D0D"/></svg>
                ''',       
            },
            {
                "text": "No",
                "order" : 2, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            
        ]
    },
    {
        'tag' : 'cmp-sys-designed',
        'section_id' : 10,
        'description': "SYSTEM DESIGNED FROM THE GROUND UP TO BE PURELY A SOLID ROOF, NOT A MIXTURE OF EXISTING PARTS",
        'items': [
            {
                "text": "Yes",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "Some",
                "order" : 1, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4a8 8 0 1 0 0 16 8 8 0 0 0 0-16zM2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12z" fill="#0D0D0D"/><path d="M12 14a1 1 0 0 1-1-1V7a1 1 0 1 1 2 0v6a1 1 0 0 1-1 1zm-1.5 2.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0z" fill="#0D0D0D"/></svg>
                ''',       
            },
            {
                "text": "No",
                "order" : 2, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            
        ]
    },
    
     {
        'tag' : 'cmp-quote-turn',
        'section_id' : 10,
        'description': "QUOTE TURNAROUND OF LESS THAN 1 HOUR",
        'items': [
            {
                "text": "Yes",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "Some",
                "order" : 1, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4a8 8 0 1 0 0 16 8 8 0 0 0 0-16zM2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12z" fill="#0D0D0D"/><path d="M12 14a1 1 0 0 1-1-1V7a1 1 0 1 1 2 0v6a1 1 0 0 1-1 1zm-1.5 2.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0z" fill="#0D0D0D"/></svg>
                ''',       
            },
            {
                "text": "No",
                "order" : 2, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            
        ]
    },
     {
        'tag' : 'cmp-full-length',
        'section_id' : 10,
        'description': "FULL LENGTH GLASS PANEL OPTION POSSIBLE TO CREATE HYBRID GLASS AND TILED ROOFS",
        'items': [
            {
                "text": "Yes",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "Some",
                "order" : 1, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4a8 8 0 1 0 0 16 8 8 0 0 0 0-16zM2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12z" fill="#0D0D0D"/><path d="M12 14a1 1 0 0 1-1-1V7a1 1 0 1 1 2 0v6a1 1 0 0 1-1 1zm-1.5 2.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0z" fill="#0D0D0D"/></svg>
                ''',       
            },
            {
                "text": "No",
                "order" : 2, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            
        ]
    },
    {
        'tag' : 'cmp-internal-ins',
        'section_id' : 10,
        'description': "ALL INTERNAL INSULATION PRODUCTS SUPPLIED WITH ALL ROOF KITS TO GUARANTEE 0.15 U VALUE",
        'items': [
            {
                "text": "Yes",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "Some",
                "order" : 1, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4a8 8 0 1 0 0 16 8 8 0 0 0 0-16zM2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12z" fill="#0D0D0D"/><path d="M12 14a1 1 0 0 1-1-1V7a1 1 0 1 1 2 0v6a1 1 0 0 1-1 1zm-1.5 2.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0z" fill="#0D0D0D"/></svg>
                ''',       
            },
            {
                "text": "No",
                "order" : 2, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            
        ]
    },
    {
        'tag' : 'cmp-window-support',
        'section_id' : 10,
        'description': "WINDOW SUPPORT MULLIONS CAN BE SUPPLIED TO ENSURE THE SUPPORTING PVC-U FRAMES CAN WITHSTAND THE WEIGHT OF THE ROOF. GREAT FOR RETROFIT NEW ROOFS ONTO EXISTING FRAMES",
        'items': [
            {
                "text": "Yes",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "Some",
                "order" : 1, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 4a8 8 0 1 0 0 16 8 8 0 0 0 0-16zM2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12z" fill="#0D0D0D"/><path d="M12 14a1 1 0 0 1-1-1V7a1 1 0 1 1 2 0v6a1 1 0 0 1-1 1zm-1.5 2.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0z" fill="#0D0D0D"/></svg>
                ''',       
            },
            {
                "text": "No",
                "order" : 2, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            
        ]
    },
    {
        'tag' : 'cmp-tile-options',
        'section_id' : 10,
        'description': "4 x ROOF TILE OPTIONS AVAILABLE. (STEEL TILES, COMPOSITE SLATE, ENVIROTILE & SLATESKIN)",
        'items': [
            {
                "text": "Yes",
                "order" : 0, 
                "svg" : '''
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle" viewBox="0 0 16 16">
                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16"/>
                        <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05"/>
                    </svg>
                ''',
            },
            {
                "text": "No",
                "order" : 1, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            {
                "text": "No",
                "order" : 2, 
                "svg" : '''
                    <svg width="16px" height="16px" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns">
    
                        <title>cross-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs>

                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                            <g id="Icon-Set" sketch:type="MSLayerGroup" transform="translate(-568.000000, -1087.000000)" fill="#000000">
                                <path d="M584,1117 C576.268,1117 570,1110.73 570,1103 C570,1095.27 576.268,1089 584,1089 C591.732,1089 598,1095.27 598,1103 C598,1110.73 591.732,1117 584,1117 L584,1117 Z M584,1087 C575.163,1087 568,1094.16 568,1103 C568,1111.84 575.163,1119 584,1119 C592.837,1119 600,1111.84 600,1103 C600,1094.16 592.837,1087 584,1087 L584,1087 Z M589.717,1097.28 C589.323,1096.89 588.686,1096.89 588.292,1097.28 L583.994,1101.58 L579.758,1097.34 C579.367,1096.95 578.733,1096.95 578.344,1097.34 C577.953,1097.73 577.953,1098.37 578.344,1098.76 L582.58,1102.99 L578.314,1107.26 C577.921,1107.65 577.921,1108.29 578.314,1108.69 C578.708,1109.08 579.346,1109.08 579.74,1108.69 L584.006,1104.42 L588.242,1108.66 C588.633,1109.05 589.267,1109.05 589.657,1108.66 C590.048,1108.27 590.048,1107.63 589.657,1107.24 L585.42,1103.01 L589.717,1098.71 C590.11,1098.31 590.11,1097.68 589.717,1097.28 L589.717,1097.28 Z" id="cross-circle" sketch:type="MSShapeGroup">

                                </path>
                            </g>
                        </g>
                    </svg>
                ''',         
            },
            
        ]
    },
     
]


blog_cat_data = [
    {
        "title": "Tips & Tricks", 
    },
    {
        "title": "Trade Knowhow", 
    },
    {
        "title": "Thought Peices", 
    },
]
article_data = [
    {
        "title" : 'Summer 2026 Design Guide',
        "slug" : "summer-2026-design-guide",
        "abstract": "The seasons are fast changing. Let's take a look at some of the latest interior design trends.",
        "body_one": "Thiw will be a very intriguing article soon...",
        "author": "Marcus Redcliffe",
        "published" : True, 
        "published_date" : datetime.datetime.now(),
        "category_id" : 1

    },
    {
        "title" : "5 Do's & Dont's for your Conservatory in the Heat",
        "slug" : "five-dos-and-donts-for-your-conservatory-in-the-heat",
        "abstract": "When the weather is this hot, here's how to make the most of your conservatory, and what to avoid!.",
        "body_one": "Thiw will be a very intriguing article soon...",
        "author": "Marcus Redcliffe",
        "published" : True, 
        "published_date" : datetime.datetime.now(),
        "category_id" : 2

    },
    {
        "title" : "How Eurocell changed the conservatory roof industry  ",
        "slug" : "five-dos-and-donts-for-your-conservatory-in-the-heat",
        "abstract": "Conservatories have always been a double edged sword, too hot in the summer, and too cold in the winter.",
        "body_one": "Thiw will be a very intriguing article soon...",
        "author": "Marcus Redcliffe",
        "published" : True, 
        "published_date" : datetime.datetime.now(),
        "category_id" : 3

    },
    
]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def seed_app():
    app = create_app()
    with app.app_context():
        print(f"{bcolors.OKBLUE}Initializing application context for seeding...{bcolors.ENDC}\n\n")
        print(f"{bcolors.WARNING}Clearing old data...{bcolors.ENDC}")
        
        db.drop_all()
        db.create_all()
        print(f"{bcolors.BOLD}Adding Pages Data...{bcolors.ENDC}\n\n")

        pages_to_add = []
        for pg in page_data:
            page = Page(
                tag=pg['tag'],
                title=pg['title'],
                description=pg['description'],
                keywords=pg['keywords'],
                body_title=pg['body_title'],
                body_intro=pg['body_intro']
            )
            pages_to_add.append(page)
        try:
            db.session.add_all(pages_to_add)
        except Exception as e:
            print(f"{bcolors.FAIL}Unable to add Pages:\n", e)
        else:
            print(f"{bcolors.OKGREEN}Success! Added {len(pages_to_add)} Pages!{bcolors.ENDC}\n\n")

        db.session.flush()

        print(f"{bcolors.BOLD}Adding Service Category Data...{bcolors.ENDC}")
        sections_to_add = []
        for sec in section_data:
            section = Section(
                **sec
            )
            sections_to_add.append(section)
        try:
            db.session.add_all(sections_to_add)
        except Exception as e:
            print(f"{bcolors.FAIL}Unable to add Sections:{bcolors.ENDC}\n", e)
        else:
            print(f"{bcolors.OKGREEN}Success! Added {len(sections_to_add)} Sections!{bcolors.ENDC}\n\n")


        print(f"{bcolors.BOLD}Adding Service Category Data...{bcolors.ENDC}\n\n")

        cats_to_add = []
        for cat in category_data:
            category = Category(
                title=cat['title']
            )
            cats_to_add.append(category)
        try:
            db.session.add_all(cats_to_add)
        except Exception as e:
            print("Unable to add Service Categories:\n", e)
        else:
            print(f"Success! Added {len(cats_to_add)} Service Categories!\n\n")

        print("Adding Service Data...")
    
        services_to_add = []
        for serv in service_data:
            service = Service(
                title = serv['title'],
                short_desc = serv['short_desc'],
                slug = serv['slug'],
                desc = serv['desc'],
                category_id = serv['category_id'],
                is_featured = serv['is_featured']
            )
            services_to_add.append(service)
        try:
            db.session.add_all(services_to_add)
        except Exception as e:
            print("Unable to add Service Categories:\n", e)
        else:
            print(f"{bcolors.OKGREEN}Success! Added {len(services_to_add)} Services!{bcolors.ENDC}\n\n")
            db.session.flush()

        print("Adding Service Intro List Data...")
        for ul in service_intro_lists:
            service = Service.get_by_id(ul['service_id'])
            if not service: 
                continue
            s_list = List(
                tag = f"{service.slug}-intro",

            )
            db.session.add(s_list)
            db.session.flush()
            items_to_add = []
            for li in ul['items']:
                list_item = ListItem(**li)
                list_item.list_id = s_list.id
                items_to_add.append(list_item)
            db.session.add_all(items_to_add)
            service.intro_list_id = s_list.id
            print(f"{bcolors.OKGREEN}Success! Added {service.title} Intro List!{bcolors.ENDC}\n\n")




        print("Adding Project Data...")
        projects_to_add = []
        for pt in project_data:
            project = Project(
                **pt
            )
            projects_to_add.append(project)
        try:
            db.session.add_all(projects_to_add)
        except Exception as e:
            print(f"{bcolors.FAIL}Unable to Add Projects{bcolors.ENDC}")
        else:
            print(f"{bcolors.OKGREEN}Success! Added {len(projects_to_add)} Projects!{bcolors.ENDC} \n\n")

        print("Adding Service Section Data...")
        for ss in service_section_data:
            service_section = ServiceSection(
                service_id= ss['service_id'],
                title=ss['title'],
                tag=ss['tag']
            )
            try:

                db.session.add(service_section)
            except Exception as e:
                print(f"{bcolors.FAIL}Unable to Add Service Sections{bcolors.ENDC}")
            else:
                db.session.flush()
                _list_data = ss['list']
                ss_list = List(
                    tag=_list_data['tag'],
                    service_section_id=service_section.id

                )
                try:
                    db.session.add(ss_list)
                except Exception as e:
                    print(f"{bcolors.FAIL}Unable to Add Service Section List{bcolors.ENDC}")
                else:
                    db.session.flush()
                    inner_items_to_add = []
                    for item in _list_data['items']:
                        list_item = ListItem(**item)
                        list_item.list_id = ss_list.id
                        inner_items_to_add.append(list_item)
                    db.session.add_all(inner_items_to_add)
            
        print(f"{bcolors.OKGREEN}Success! Added {len(service_section_data)} Projects!{bcolors.ENDC} \n\n")


        print("Adding List Data...")

        lists_to_add = []
        for lst in list_data:
            list_ = List(
                tag=lst['tag'],
                section_id = lst['section_id']
            )

            if lst.get('title'):
                list_.title = lst.get('title')
            if lst.get('description'):
                list_.description = lst.get('description')
            
            try:
                db.session.add(list_)
            except Exception as e:
                print(f"{bcolors.FAIL}Unable to add List:\n{bcolors.ENDC}", e)
            else:
                print(f"{bcolors.OKGREEN}Success! Added {list_.tag} List!{bcolors.ENDC}\n\n")
                db.session.flush()
                print(f"Adding {list_.tag} Items...\n")

                items_to_add = []
                for item in lst['items']:
                    list_item = ListItem(
                        **item,
                        list_id = list_.id
                    )
                    items_to_add.append(list_item)
            try:
                db.session.add_all(items_to_add)
            except Exception as e:
                print(f"{bcolors.FAIL}Unable to add List Items for {list_.tag}:{bcolors.ENDC}\n", e)
            else: 
                print(f"{bcolors.OKGREEN}Success! Added {len(lst['items'])} Items to {list_.tag}{bcolors.ENDC} \n\n")


        print("Adding Blog Categories...")
        revs_to_add = []
        for rev in review_data:
            review = Review(**rev)
            revs_to_add.append(review)
        try:
            db.session.add_all(revs_to_add)
        
        except Exception as e:
            print(f"{bcolors.FAIL}Unable to add List Items for {list_.tag}:{bcolors.ENDC}\n", e)
        else: 
            print(f"{bcolors.OKGREEN}Success! Added {len(revs_to_add)} Reviews! {bcolors.ENDC} \n\n")

        print("Adding Blog Categories...")

        blog_cats_to_add = []
        for blg_ct in blog_cat_data:
            blog_cat = BlogCategory( **blg_ct)
            blog_cats_to_add.append(blog_cat)
        try:
            db.session.add_all(blog_cats_to_add)
        except Exception as e:
            print("Oh no!! Unable to add blog categories", e)
        else:
            print(f"Success, Addded {len(blog_cats_to_add)}  Blog Cateogires\n\n")
            db.session.flush()

        print("Adding Articles")
        arts_to_add = []
        for atcl in article_data:
            article = Article(**atcl)
            arts_to_add.append(article)
        try:
            db.session.add_all(arts_to_add)
        except Exception as e:
            print(f"{bcolors.OKGREEN}Oh no unable to add articles{bcolors.ENDC}", e)
        else: 
            print(f"{bcolors.OKGREEN}Success! Added {len(arts_to_add)} articles.{bcolors.ENDC}\n\n")
        db.session.commit()

        print("Seeding complete!!!")

if __name__ == '__main__':
    seed_app()