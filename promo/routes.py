from flask import Blueprint, request, session, current_app, redirect, url_for, flash, render_template
from flask_login import current_user, login_user
from promo.admin.forms.login import LoginForm
from promo.models.user import User
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


@main.route('//')
def home():
    page = {
        'tag' : 'home',
        'body_title' : 'Welcome to CRC Group',
        'title' : 'About CRC Group',
        'body_intro' : 'We are The Conservatory Roof Convrersion Group. And our specialism is in the name. We offer premium external space installations and conversions.'
       
    }
    welcome_cards = [
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
    
    con_shapes = [
        {
            "title": "Victorian",
            "description": "A classic design featuring a faceted, curved bay front, a steep roof, and ornate ridge details that deliver traditional British elegance.",
            "svg" : '''
                
<svg width="243.88751" height="184.9209" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1"><linearGradient id="linearGradient70"><stop style="stop-color:#6dabcf;stop-opacity:1;" offset="0" id="stop67" /><stop style="stop-color:#5fb0e6;stop-opacity:0.50588232;" offset="0.45308921" id="stop68" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop70" /></linearGradient><pattern xlink:href="#Strips1_5" preserveAspectRatio="xMidYMid" id="pattern67" patternTransform="matrix(0,0.1,-0.1,0,0,0)" x="0" y="0" /><pattern patternUnits="userSpaceOnUse" width="6" height="1" patternTransform="translate(0,0) scale(2,2)" preserveAspectRatio="xMidYMid" id="Strips1_5" style="fill:#000000">&#10;      <rect style="stroke:none" x="0" y="-0.5" width="1" height="2" id="rect164" />&#10;    </pattern><linearGradient id="linearGradient64"><stop style="stop-color:#a3c9e1;stop-opacity:1;" offset="0" id="stop61" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop62" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop63" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop64" /></linearGradient><linearGradient id="linearGradient60"><stop style="stop-color:#8cbed9;stop-opacity:1;" offset="0" id="stop57" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop58" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop59" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop60" /></linearGradient><pattern xlink:href="#pattern13" preserveAspectRatio="xMidYMid" id="pattern14" patternTransform="matrix(-0.01995129,0.00139513,-0.00139513,-0.01995129,0,0)" x="0" y="0" /><pattern xlink:href="#Bricks" id="pattern13" patternTransform="matrix(0.01995129,0.00139513,-0.00139513,0.01995129,0.42094947,-11.739813)" x="0" y="0" preserveAspectRatio="xMidYMid" /><pattern xlink:href="#Bricks" id="pattern10" patternTransform="scale(0.02)" x="0" y="0" preserveAspectRatio="none" /><pattern patternUnits="userSpaceOnUse" width="100" height="100" id="Bricks" style="fill:#935219" patternTransform="scale(0.25,0.25)"><g id="g13367"><rect style="fill:none;stroke:none;stroke-width:0" id="rect13349" width="100" height="100" x="0" y="0" /><rect style="fill-opacity:1;stroke-width:0" id="rect13351" width="40" height="40" x="0" y="60" /><rect style="fill-opacity:1;stroke-width:0" id="rect13353" width="90" height="40" x="0" y="10" /><rect style="fill-opacity:1;stroke-width:0" id="rect13355" width="50" height="40" x="50" y="60" /></g></pattern><linearGradient xlink:href="#linearGradient60" id="linearGradient11" x1="167.06261" y1="27.089109" x2="173.57579" y2="31.392151" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient64" id="linearGradient14" gradientUnits="userSpaceOnUse" x1="167.06261" y1="27.089109" x2="173.57579" y2="31.392151" gradientTransform="translate(10.555822,-0.10841814)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient54" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="145.01958" y1="24.0648" x2="148.92474" y2="19.325005" /><linearGradient xlink:href="#linearGradient70" id="linearGradient55" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="152.00311" y1="23.510586" x2="157.09706" y2="17.924889" /><linearGradient xlink:href="#linearGradient70" id="linearGradient56" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="139.66898" y1="34.298935" x2="148.91502" y2="24.094034" /><linearGradient xlink:href="#linearGradient70" id="linearGradient57" gradientUnits="userSpaceOnUse" gradientTransform="matrix(-0.64051216,0,0,0.9671019,288.32576,0.9940494)" x1="150.92365" y1="34.486496" x2="160.32947" y2="26.142387" /><linearGradient xlink:href="#linearGradient70" id="linearGradient72" x1="155.09953" y1="28.766298" x2="160.79262" y2="28.766298" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient73" x1="149.03021" y1="28.757526" x2="154.17104" y2="28.757526" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient74" x1="149.03001" y1="20.392658" x2="154.17073" y2="20.392658" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient75" x1="155.09943" y1="19.961107" x2="160.79259" y2="19.961107" gradientUnits="userSpaceOnUse" /></defs><g id="layer2" transform="translate(-142.39713,-1.5863839)"><path style="fill:#968334;fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 198.60245,45.193143 -0.0661,-9.98802 -13.95677,1.124479 v 11.112499 z" id="path76" /><path id="path77" style="fill:#968334;fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 184.58344,43.618976 0.0583,3.696537 h -23.0349 l 0.0187,-5.481645 z" /><path style="fill:#968334;fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 147.79386,45.112527 0.0661,-9.98802 13.95677,1.124479 v 11.112499 z" id="path78" /><path id="path75" style="fill:#42403e;fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 200.79629,15.944435 -16.06221,-1.343101 h -23.66934 l -14.5044,1.343101 27.11797,-10.9746084 z" /><path style="fill:url(#pattern14);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 198.60245,45.193143 -0.0661,-9.98802 -13.95677,1.124479 v 11.112499 z" id="path13" /><path id="rect30" style="fill:url(#pattern10);fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 184.58344,43.618976 0.0583,3.696537 h -23.0349 l 0.0187,-5.481645 z" /><path id="path25" style="fill:url(#pattern67);fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 200.79629,15.944435 -16.06221,-1.343101 h -23.66934 l -14.5044,1.343101 27.11797,-10.9746084 z" /><path id="rect25" style="fill:#302c2a;fill-opacity:1;stroke:none;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 146.64253,15.977569 14.73106,-1.226469 h 23.3848 l 15.81024,1.226469 v 1.546345 l -15.86856,-1.226469 h -23.38479 l -14.67275,1.226469 z" /><rect style="fill:#e5e5e5;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26" width="22.803343" height="27.902233" x="161.83841" y="16.331261" /><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect2" width="10.649479" height="26.127604" x="162.71873" y="16.999477" /><rect style="opacity:0.579137;fill:url(#linearGradient11);fill-opacity:1;stroke:#787666;stroke-width:0.0915985;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27" width="7.9183006" height="23.873291" x="164.11497" y="18.145884" /><path style="fill:url(#pattern13);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 147.79386,45.112527 0.0661,-9.98802 13.95677,1.124479 v 11.112499 z" id="path11" /><rect style="fill:#f6f6f6;fill-opacity:1;stroke:#414141;stroke-width:0.0739189;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29" width="28.63773" height="0.66228044" x="159.07536" y="43.558125" rx="1.3306036" /><path style="fill:none;fill-opacity:1;stroke:#484848;stroke-width:0.349206;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 162.508,13.647747 11.06827,-7.6286199 10.62175,7.7935629" id="path40" /><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect3" width="10.649479" height="26.127604" x="173.30208" y="16.999477" /><rect style="opacity:0.579137;fill:url(#linearGradient14);fill-opacity:1;stroke:#787666;stroke-width:0.0915985;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27-2" width="7.9183006" height="23.873291" x="174.67079" y="18.037466" /><rect style="fill:#e5e5e5;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect4" width="0.52916974" height="26.309505" x="172.93828" y="16.900259" /><path id="rect14" style="fill:#e5e5e5;stroke-width:1.13801;stroke-linecap:square;paint-order:markers fill stroke" d="m 148.26509,17.630418 13.55405,-1.261677 v 19.680735 l -13.55325,-0.769448 z" /><path id="rect28" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 148.77929,18.605389 5.75537,-0.485973 1e-4,4.251266 -5.7553,0.288721 z" /><path id="rect15" style="opacity:0.656;fill:url(#linearGradient74);fill-opacity:1;stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 149.03002,19.04074 5.14062,-0.414267 9e-5,3.253325 -5.14058,0.279045 z" /><path id="rect31" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 154.77794,18.098874 6.36961,-0.537837 1e-5,4.477906 -6.36953,0.319534 z" /><path id="rect16" style="opacity:0.656;fill:url(#linearGradient75);fill-opacity:1;stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 155.09942,18.551626 5.69314,-0.458793 2e-5,3.427512 -5.69309,0.309037 z" /><path id="rect33" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 148.7168,23.217872 5.74904,-0.261403 2.8e-4,11.550378 -5.74884,-0.274199 z" /><path id="rect17" style="opacity:0.656;fill:url(#linearGradient73);fill-opacity:1;stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 149.03022,23.660128 5.14054,-0.213939 2.8e-4,10.622674 -5.14039,-0.22756 z" /><path id="rect32" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 154.77805,22.942272 6.36951,-0.289615 3e-5,12.172873 -6.36927,-0.303791 z" /><path id="rect18" style="opacity:0.656;fill:url(#linearGradient72);fill-opacity:1;stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 155.09953,23.407536 5.69305,-0.236934 4e-5,11.191393 -5.69285,-0.252017 z" /><path id="path34" style="fill:#e5e5e5;stroke-width:1.13801;stroke-linecap:square;paint-order:markers fill stroke" d="m 198.16913,17.630418 -13.55405,-1.261677 v 19.680735 l 13.55325,-0.769448 z" /><path id="path35" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.65494,18.605389 -5.75538,-0.485973 -1e-4,4.251266 5.7553,0.288721 z" /><path id="path36" style="opacity:0.656;fill:url(#linearGradient54);stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.4042,19.04074 -5.14062,-0.414267 -9e-5,3.253325 5.14058,0.279045 z" /><path id="path37" style="fill:#ffffff;stroke-width:0.984295;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.65628,18.098874 -6.36961,-0.537837 -10e-6,4.477906 6.36953,0.319534 z" /><path id="path38" style="opacity:0.656;fill:url(#linearGradient55);stroke-width:1.02529;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.3348,18.551626 -5.69314,-0.458793 -2e-5,3.427512 5.69309,0.309037 z" /><path id="path39" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.71742,23.217872 -5.74903,-0.261403 -2.9e-4,11.550378 5.74884,-0.274199 z" /><path id="path41" style="opacity:0.656;fill:url(#linearGradient56);stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 197.404,23.660128 -5.14054,-0.213939 -2.8e-4,10.622674 5.14039,-0.22756 z" /><path id="path42" style="fill:#ffffff;stroke-width:1.62292;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.65617,22.942272 -6.36951,-0.289615 -3e-5,12.172873 6.36927,-0.303791 z" /><path id="path53" style="opacity:0.656;fill:url(#linearGradient57);stroke-width:1.85274;stroke-linecap:square;paint-order:markers fill stroke" d="m 191.33469,23.407536 -5.69305,-0.236934 -4e-5,11.191393 5.69285,-0.252017 z" /></g></svg>
            
            '''
        },
        {
            "title": "Edwardian",
            "description": "Characterized by a square or rectangular footprint, this style maximizes floor space with flat walls and a timeless, symmetrical pitched roof.",
            "svg" : '''
                

        

<svg width="243.88751" height="184.9209" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1"><pattern xlink:href="#Strips1_5" preserveAspectRatio="xMidYMid" id="pattern88" patternTransform="matrix(0,0.1,-0.1,0,0,0)" x="0" y="0" /><linearGradient id="linearGradient70"><stop style="stop-color:#6dabcf;stop-opacity:1;" offset="0" id="stop67" /><stop style="stop-color:#5fb0e6;stop-opacity:0.50588232;" offset="0.45308921" id="stop68" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop70" /></linearGradient><pattern patternUnits="userSpaceOnUse" width="6" height="1" patternTransform="translate(0,0) scale(2,2)" preserveAspectRatio="xMidYMid" id="Strips1_5" style="fill:#000000">&#10;      <rect style="stroke:none" x="0" y="-0.5" width="1" height="2" id="rect164" />&#10;    </pattern><linearGradient id="linearGradient64"><stop style="stop-color:#a3c9e1;stop-opacity:1;" offset="0" id="stop61" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop62" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop63" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop64" /></linearGradient><pattern xlink:href="#Bricks" id="pattern11" patternTransform="scale(0.02)" x="0" y="0" preserveAspectRatio="none" /><pattern patternUnits="userSpaceOnUse" width="100" height="100" id="Bricks" style="fill:#935219" patternTransform="scale(0.25,0.25)"><g id="g13367"><rect style="fill:none;stroke:none;stroke-width:0" id="rect13349" width="100" height="100" x="0" y="0" /><rect style="fill-opacity:1;stroke-width:0" id="rect13351" width="40" height="40" x="0" y="60" /><rect style="fill-opacity:1;stroke-width:0" id="rect13353" width="90" height="40" x="0" y="10" /><rect style="fill-opacity:1;stroke-width:0" id="rect13355" width="50" height="40" x="50" y="60" /></g></pattern><linearGradient xlink:href="#linearGradient64" id="linearGradient8" x1="247.16119" y1="22.064793" x2="255.86038" y2="28.017918" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient64" id="linearGradient9" x1="235.37469" y1="21.204893" x2="244.71271" y2="28.017914" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient81" x1="221.19521" y1="26.766003" x2="232.82535" y2="26.766003" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient83" x1="221.27644" y1="17.586765" x2="232.91472" y2="17.586765" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient85" x1="259.2952" y1="26.766003" x2="270.92535" y2="26.766003" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient87" x1="259.37646" y1="17.586765" x2="271.01471" y2="17.586765" gradientUnits="userSpaceOnUse" /></defs><g id="layer2" transform="translate(-214.32628,-0.6498566)"><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect88" width="10.649479" height="26.127604" x="234.95" y="14.816667" /><path id="path79" style="opacity:1;fill:#968334;fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 219.19239,34.129885 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><path id="rect30-8" style="opacity:1;fill:url(#pattern11);fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 219.19239,34.129885 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><path id="path25-4" style="fill:#414141;fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 273.02783,13.879819 -16.06221,-0.682543 h -23.66933 l -14.50441,0.682543 27.11797,-9.3871082 z" /><path id="rect25-2" style="fill:#302c2a;fill-opacity:1;stroke:none;stroke-width:0.0795385;stroke-linecap:square;paint-order:stroke markers fill" d="m 218.87407,13.294216 14.73106,-0.120338 h 23.3848 l 15.81024,0.120338 v 1.10675 l -15.86856,-0.120338 h -23.3848 l -14.67274,0.120338 z" /><rect style="opacity:1;fill:#e5e5e5;fill-opacity:1;stroke:#e5e5e5;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26-1" width="24.067005" height="27.844791" x="234.06995" y="14.266648" /><rect style="opacity:1;fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.11265;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect89" width="11.11319" height="25.726902" x="234.80177" y="15.154462" /><rect style="opacity:0.579137;fill:url(#linearGradient9);fill-opacity:1;stroke:#787666;stroke-width:0.093878;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27-3" width="8.3181" height="23.871012" x="236.34767" y="16.082407" /><rect style="opacity:1;fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.11265;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect90" width="11.11319" height="25.726902" x="246.1496" y="15.154462" /><rect style="opacity:0.579137;fill:url(#linearGradient8);fill-opacity:1;stroke:#787666;stroke-width:0.0954728;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect28-7" width="8.6037045" height="23.869417" x="247.20894" y="16.083208" /><rect style="fill:#fbfbfb;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29-0" width="28.617632" height="1.0721303" x="231.31697" y="41.602776" rx="1.3296698" /><path id="rect41" style="fill:#e5e5e5;fill-opacity:1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 219.97674,14.215631 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path90" style="fill:#ffffff;fill-opacity:1;stroke-width:0.853368;stroke-linecap:square;paint-order:stroke markers fill" d="m 220.4827,15.139068 h 13.22577 v 4.730031 h -13.22577 z" /><path id="rect42" style="opacity:0.651079;fill:url(#linearGradient83);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 221.27645,15.840274 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path92" style="fill:#ffffff;fill-opacity:1;stroke-width:1.45632;stroke-linecap:square;paint-order:stroke markers fill" d="m 220.4827,20.017327 h 13.22577 v 13.775473 h -13.22577 z" /><path id="rect43" style="opacity:0.654676;fill:url(#linearGradient81);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 221.19521,20.470508 h 11.63014 v 12.590987 h -11.63014 z" /><path id="path43" style="fill:#e5e5e5;fill-opacity:1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 258.07674,14.215631 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path98" style="fill:#ffffff;fill-opacity:1;stroke-width:0.853368;stroke-linecap:square;paint-order:stroke markers fill" d="m 258.51661,15.139068 h 13.22577 v 4.730031 h -13.22577 z" /><path id="path44" style="opacity:0.661871;fill:url(#linearGradient87);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 259.37645,15.840274 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path99" style="fill:#ffffff;fill-opacity:1;stroke-width:1.45632;stroke-linecap:square;paint-order:stroke markers fill" d="m 258.51661,20.017327 h 13.22577 v 13.775473 h -13.22577 z" /><path id="path45" style="opacity:0.645683;fill:url(#linearGradient85);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 259.29521,20.470508 h 11.63014 v 12.590987 h -11.63014 z" /><path id="path87" style="fill:url(#pattern88);fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 273.02783,13.879819 -16.06221,-0.682543 h -23.66933 l -14.50441,0.682543 27.11797,-9.3871082 z" /><path id="path91" style="fill:url(#pattern88);fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 273.02783,13.879819 -16.06221,-0.682543 h -23.66933 l -14.50441,0.682543 27.11797,-9.3871082 z" /></g></svg>
            
            '''
        },
        {
            "title": "Gable-Ended",
            "description": "Features a high, upright front roof that mimics the gable end of a house, creating a grand, light-filled interior with impressive height.",
            "svg" : '''
                
<svg width="243.88751" height="184.9209" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1"><linearGradient id="linearGradient70"><stop style="stop-color:#6dabcf;stop-opacity:1;" offset="0" id="stop67" /><stop style="stop-color:#5fb0e6;stop-opacity:0.50588232;" offset="0.45308921" id="stop68" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop70" /></linearGradient><linearGradient id="linearGradient64"><stop style="stop-color:#a3c9e1;stop-opacity:1;" offset="0" id="stop61" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop62" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop63" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop64" /></linearGradient><pattern xlink:href="#Bricks-3" id="pattern11-0" patternTransform="matrix(0.02,0,0,0.02,73.57676,-1.0399659)" x="0" y="0" preserveAspectRatio="none" /><pattern patternUnits="userSpaceOnUse" width="100" height="100" id="Bricks-3" style="fill:#935219" patternTransform="scale(0.25,0.25)"><g id="g13367-7"><rect style="fill:none;stroke:none;stroke-width:0" id="rect13349-3" width="100" height="100" x="0" y="0" /><rect style="fill-opacity:1;stroke-width:0" id="rect13351-4" width="40" height="40" x="0" y="60" /><rect style="fill-opacity:1;stroke-width:0" id="rect13353-2" width="90" height="40" x="0" y="10" /><rect style="fill-opacity:1;stroke-width:0" id="rect13355-6" width="50" height="40" x="50" y="60" /></g></pattern><linearGradient xlink:href="#linearGradient64" id="linearGradient92" gradientUnits="userSpaceOnUse" x1="235.37469" y1="21.204893" x2="244.71271" y2="28.017914" gradientTransform="translate(73.57676,-1.0399659)" /><linearGradient xlink:href="#linearGradient64" id="linearGradient93" gradientUnits="userSpaceOnUse" x1="247.16119" y1="22.064793" x2="255.86038" y2="28.017918" gradientTransform="translate(73.57676,-1.0399659)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient94" gradientUnits="userSpaceOnUse" x1="221.27644" y1="17.586765" x2="232.91472" y2="17.586765" gradientTransform="translate(73.57676,-1.0399659)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient95" gradientUnits="userSpaceOnUse" x1="221.19521" y1="26.766003" x2="232.82535" y2="26.766003" gradientTransform="translate(73.57676,-1.0399659)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient96" gradientUnits="userSpaceOnUse" x1="259.37646" y1="17.586765" x2="271.01471" y2="17.586765" gradientTransform="translate(73.57676,-1.0399659)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient97" gradientUnits="userSpaceOnUse" x1="259.2952" y1="26.766003" x2="270.92535" y2="26.766003" gradientTransform="translate(73.57676,-1.0399659)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient101" x1="296.92862" y1="9.2769527" x2="307.44583" y2="9.2769527" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient102" gradientUnits="userSpaceOnUse" x1="296.92862" y1="9.2769527" x2="307.44583" y2="9.2769527" gradientTransform="matrix(-1,0,0,1,638.90269,0)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient104" x1="308.08826" y1="6.6416469" x2="319.36032" y2="6.6416469" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient105" gradientUnits="userSpaceOnUse" x1="308.08826" y1="6.6416469" x2="319.36032" y2="6.6416469" gradientTransform="matrix(-1,0,0,1,639.09032,0)" /></defs><g id="layer2" transform="translate(-287.23021)"><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect88-9" width="10.649479" height="26.127604" x="308.52676" y="13.776701" /><path id="path79-9" style="fill:#968334;fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 292.76915,33.089919 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><path id="rect30-8-2" style="fill:url(#pattern11-0);fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 292.76915,33.089919 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><path id="path25-4-3" style="fill:#e5e5e5;fill-opacity:1;stroke:#666557;stroke-width:0.0283881;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 346.60357,12.837258 c -18.32479,-0.364849 -35.76725,-0.205081 -54.23391,0 l 27.11695,-12.22596641 z" /><path id="rect25-2-8" style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.0795385;stroke-linecap:square;paint-order:stroke markers fill" d="m 292.45083,12.25425 14.73106,-0.120338 h 23.3848 l 15.81024,0.120338 v 1.10675 l -15.86856,-0.120338 h -23.3848 l -14.67274,0.120338 z" /><rect style="fill:#e5e5e5;fill-opacity:1;stroke:#e5e5e5;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26-1-7" width="24.067005" height="27.844791" x="307.6467" y="13.226683" /><rect style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.113211;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect89-3" width="11.224282" height="25.726902" x="308.29773" y="14.114496" /><rect style="opacity:0.579137;fill:url(#linearGradient92);fill-opacity:1;stroke:#787666;stroke-width:0.093878;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27-3-4" width="8.3181" height="23.871012" x="309.92444" y="15.042441" /><rect style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.113044;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect90-7" width="11.19121" height="25.726902" x="319.79529" y="14.114496" /><rect style="opacity:0.579137;fill:url(#linearGradient93);fill-opacity:1;stroke:#787666;stroke-width:0.0954728;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect28-7-2" width="8.6037045" height="23.869417" x="320.78571" y="15.043242" /><rect style="fill:#fbfbfb;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29-0-2" width="28.617632" height="1.0721303" x="304.89374" y="40.562809" rx="1.3296698" /><path id="rect41-1" style="fill:#e5e5e5;fill-opacity:1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 293.5535,13.175665 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path90-9" style="fill:#ffffff;fill-opacity:1;stroke-width:0.853368;stroke-linecap:square;paint-order:stroke markers fill" d="m 294.05946,14.099102 h 13.22577 v 4.730031 h -13.22577 z" /><path id="rect42-1" style="opacity:0.651079;fill:url(#linearGradient94);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 294.85321,14.800308 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path92-3" style="fill:#ffffff;fill-opacity:1;stroke-width:1.45632;stroke-linecap:square;paint-order:stroke markers fill" d="m 294.05946,18.977361 h 13.22577 v 13.775473 h -13.22577 z" /><path id="rect43-6" style="opacity:0.654676;fill:url(#linearGradient95);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 294.77197,19.430542 h 11.63014 v 12.590987 h -11.63014 z" /><path id="path43-5" style="fill:#e5e5e5;fill-opacity:1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 331.6535,13.175665 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path106" style="fill:#ffffff;fill-opacity:1;stroke-width:0.853368;stroke-linecap:square;paint-order:stroke markers fill" d="m 332.1016,14.099102 h 13.22577 v 4.730031 h -13.22577 z" /><path id="path44-9" style="opacity:0.661871;fill:url(#linearGradient96);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 332.95321,14.800308 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path105" style="fill:#ffffff;fill-opacity:1;stroke-width:1.45632;stroke-linecap:square;paint-order:stroke markers fill" d="m 332.09331,18.977361 h 13.22577 v 13.775473 h -13.22577 z" /><path id="path45-6" style="opacity:0.645683;fill:url(#linearGradient97);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 332.87197,19.430542 h 11.63014 v 12.590987 h -11.63014 z" /><path style="opacity:0.579137;fill:url(#linearGradient101);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 307.44582,11.476301 v -4.5309891 l -10.51719,4.6632811 z" id="path100" /><path style="opacity:0.579137;fill:url(#linearGradient102);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 331.45682,11.476301 v -4.5309891 l 10.51719,4.6632811 z" id="path101" /><path style="opacity:0.579137;fill:url(#linearGradient104);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 319.36032,11.552725 v -9.8689271 l -11.27207,4.9578493 v 4.9578488 z" id="path102" /><path style="opacity:0.579137;fill:url(#linearGradient105);fill-opacity:1;stroke:none;stroke-width:1.41023;stroke-linecap:square;stroke-dasharray:none;paint-order:markers fill stroke" d="m 319.72996,11.552725 v -9.8689271 l 11.27207,4.9578493 v 4.9578488 z" id="path104" /></g></svg>

            '''
        },
        {
            "title": "Lean-To",
            "description": "A simple, modern option with a single sloped roof that leans against the main property, making it ideal for bungalows or limited spaces.",
            "svg" : '''
                    <svg width="243.88751" height="184.9209" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1"><pattern xlink:href="#Strips1_5-9" preserveAspectRatio="xMidYMid" id="pattern125" patternTransform="matrix(0,0.1,-0.1,0,0,0)" x="0" y="0" /><linearGradient id="linearGradient70"><stop style="stop-color:#6dabcf;stop-opacity:1;" offset="0" id="stop67" /><stop style="stop-color:#5fb0e6;stop-opacity:0.50588232;" offset="0.45308921" id="stop68" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop70" /></linearGradient><linearGradient id="linearGradient64"><stop style="stop-color:#a3c9e1;stop-opacity:1;" offset="0" id="stop61" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop62" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop63" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop64" /></linearGradient><pattern xlink:href="#Bricks-3-2" id="pattern11-0-1" patternTransform="matrix(0.02,0,0,0.02,148.19,0.21639575)" x="0" y="0" preserveAspectRatio="none" /><pattern patternUnits="userSpaceOnUse" width="100" height="100" id="Bricks-3-2" style="fill:#935219" patternTransform="scale(0.25,0.25)"><g id="g13367-7-8"><rect style="fill:none;stroke:none;stroke-width:0" id="rect13349-3-0" width="100" height="100" x="0" y="0" /><rect style="fill-opacity:1;stroke-width:0" id="rect13351-4-2" width="40" height="40" x="0" y="60" /><rect style="fill-opacity:1;stroke-width:0" id="rect13353-2-6" width="90" height="40" x="0" y="10" /><rect style="fill-opacity:1;stroke-width:0" id="rect13355-6-6" width="50" height="40" x="50" y="60" /></g></pattern><linearGradient xlink:href="#linearGradient64" id="linearGradient106" gradientUnits="userSpaceOnUse" gradientTransform="translate(148.19,0.21639575)" x1="235.37469" y1="21.204893" x2="244.71271" y2="28.017914" /><linearGradient xlink:href="#linearGradient64" id="linearGradient107" gradientUnits="userSpaceOnUse" gradientTransform="translate(148.19,0.21639575)" x1="247.16119" y1="22.064793" x2="255.86038" y2="28.017918" /><linearGradient xlink:href="#linearGradient70" id="linearGradient108" gradientUnits="userSpaceOnUse" gradientTransform="translate(148.19,0.21639575)" x1="221.27644" y1="17.586765" x2="232.91472" y2="17.586765" /><linearGradient xlink:href="#linearGradient70" id="linearGradient109" gradientUnits="userSpaceOnUse" gradientTransform="translate(148.19,0.21639575)" x1="221.19521" y1="26.766003" x2="232.82535" y2="26.766003" /><linearGradient xlink:href="#linearGradient70" id="linearGradient110" gradientUnits="userSpaceOnUse" gradientTransform="translate(148.19,0.21639575)" x1="259.37646" y1="17.586765" x2="271.01471" y2="17.586765" /><linearGradient xlink:href="#linearGradient70" id="linearGradient111" gradientUnits="userSpaceOnUse" gradientTransform="translate(148.19,0.21639575)" x1="259.2952" y1="26.766003" x2="270.92535" y2="26.766003" /><pattern patternUnits="userSpaceOnUse" width="6" height="1" patternTransform="translate(0,0) scale(2,2)" preserveAspectRatio="xMidYMid" id="Strips1_5-9" style="fill:#000000">&#10;      <rect style="stroke:none" x="0" y="-0.5" width="1" height="2" id="rect164-7" />&#10;    </pattern></defs><g id="layer2" transform="translate(-361.75877)"><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect88-9-3" width="10.649479" height="26.127604" x="383.14001" y="15.033063" /><path id="path79-9-5" style="fill:#968334;fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 367.38239,34.34628 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><path id="rect30-8-2-7" style="fill:url(#pattern11-0-1);fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 367.38239,34.34628 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><path id="rect25-2-8-7" style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.0795385;stroke-linecap:square;paint-order:stroke markers fill" d="m 367.06407,13.510611 14.73106,-0.120338 h 23.3848 l 15.81024,0.120338 v 1.10675 l -15.86856,-0.120338 h -23.3848 l -14.67274,0.120338 z" /><rect style="fill:#e5e5e5;fill-opacity:1;stroke:#e5e5e5;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26-1-7-1" width="24.067005" height="27.844791" x="382.25995" y="14.483045" /><rect style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.113211;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect89-3-4" width="11.224282" height="25.726902" x="382.91098" y="15.370858" /><rect style="opacity:0.579137;fill:url(#linearGradient106);fill-opacity:1;stroke:#787666;stroke-width:0.093878;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27-3-4-8" width="8.3181" height="23.871012" x="384.53769" y="16.298803" /><rect style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.113044;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect90-7-9" width="11.19121" height="25.726902" x="394.40854" y="15.370858" /><rect style="opacity:0.579137;fill:url(#linearGradient107);fill-opacity:1;stroke:#787666;stroke-width:0.0954728;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect28-7-2-1" width="8.6037045" height="23.869417" x="395.39896" y="16.299604" /><rect style="fill:#f2f2f2;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29-0-2-5" width="28.617632" height="1.0721303" x="379.50699" y="41.819172" rx="1.3296698" /><path id="rect41-1-6" style="fill:#e5e5e5;fill-opacity:1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 368.16674,14.432026 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path90-9-9" style="fill:#ffffff;fill-opacity:1;stroke-width:0.853368;stroke-linecap:square;paint-order:stroke markers fill" d="m 368.6727,15.355463 h 13.22577 v 4.730031 h -13.22577 z" /><path id="rect42-1-6" style="opacity:0.651079;fill:url(#linearGradient108);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 369.46645,16.056669 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path92-3-7" style="fill:#ffffff;fill-opacity:1;stroke-width:1.45632;stroke-linecap:square;paint-order:stroke markers fill" d="m 368.6727,20.233722 h 13.22577 v 13.775473 h -13.22577 z" /><path id="rect43-6-0" style="opacity:0.654676;fill:url(#linearGradient109);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 369.38521,20.686903 h 11.63014 v 12.590987 h -11.63014 z" /><path id="path43-5-7" style="fill:#e5e5e5;fill-opacity:1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 406.26674,14.432026 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path106-1" style="fill:#ffffff;fill-opacity:1;stroke-width:0.853368;stroke-linecap:square;paint-order:stroke markers fill" d="m 406.71484,15.355463 h 13.22577 v 4.730031 h -13.22577 z" /><path id="path44-9-4" style="opacity:0.661871;fill:url(#linearGradient110);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 407.56645,16.056669 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path105-5" style="fill:#ffffff;fill-opacity:1;stroke-width:1.45632;stroke-linecap:square;paint-order:stroke markers fill" d="m 406.70655,20.233722 h 13.22577 v 13.775473 h -13.22577 z" /><path id="path45-6-9" style="opacity:0.645683;fill:url(#linearGradient111);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 407.48521,20.686903 h 11.63014 v 12.590987 h -11.63014 z" /><path id="path115" style="fill:#464646;fill-opacity:1;stroke:none;stroke-width:0.187008;stroke-linecap:square;paint-order:stroke markers fill" d="m 367.06407,7.3767234 14.73106,-0.665228 h 23.3848 l 15.81024,0.665228 v 6.1181096 c -26.57622,-0.0093 -34.11948,-0.01511 -53.9261,0 z" /><path id="path124" style="fill:url(#pattern125);fill-opacity:1;stroke:none;stroke-width:0.187008;stroke-linecap:square;paint-order:stroke markers fill" d="m 367.06407,7.3767234 14.73106,-0.665228 h 23.3848 l 15.81024,0.665228 v 6.1181096 c -26.57622,-0.0093 -34.11948,-0.01511 -53.9261,0 z" /></g></svg>
            '''
        },
        {
            "title": "P-Shaped",
            "description": "Combines a lean-to element with a rounded Victorian or Edwardian extension, creating a versatile, multi-functional, zoned living area.",
            "svg" : '''

                <svg width="243.88751" height="184.9209" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1"><pattern xlink:href="#Strips1_5-9" preserveAspectRatio="xMidYMid" id="pattern126" patternTransform="matrix(0,0.1,-0.1,0,0,0)" x="0" y="0" /><pattern xlink:href="#Bricks-35" id="pattern122" patternTransform="scale(0.017)" x="0" y="0" preserveAspectRatio="xMidYMid" /><pattern xlink:href="#pattern88-2" preserveAspectRatio="xMidYMid" id="pattern121" patternTransform="matrix(0,0.1,-0.1,0,225.97675,-1.5691325)" /><pattern xlink:href="#pattern88-2" preserveAspectRatio="xMidYMid" id="pattern120" patternTransform="matrix(0,0.1,-0.1,0,225.97675,-1.5691325)" /><linearGradient id="linearGradient70"><stop style="stop-color:#6dabcf;stop-opacity:1;" offset="0" id="stop67" /><stop style="stop-color:#5fb0e6;stop-opacity:0.50588232;" offset="0.45308921" id="stop68" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop70" /></linearGradient><linearGradient id="linearGradient64"><stop style="stop-color:#a3c9e1;stop-opacity:1;" offset="0" id="stop61" /><stop style="stop-color:#92c0db;stop-opacity:0.50588235;" offset="0.45308921" id="stop62" /><stop style="stop-color:#bad7e8;stop-opacity:0;" offset="0.61556059" id="stop63" /><stop style="stop-color:#99c5df;stop-opacity:1;" offset="1" id="stop64" /></linearGradient><pattern xlink:href="#Bricks-35" id="pattern11-8" patternTransform="matrix(0.02,0,0,0.02,225.97675,-1.5691325)" x="0" y="0" preserveAspectRatio="none" /><pattern patternUnits="userSpaceOnUse" width="100" height="100" id="Bricks-35" style="fill:#935219" patternTransform="scale(0.25,0.25)"><g id="g13367-4"><rect style="fill:none;stroke:none;stroke-width:0" id="rect13349-1" width="100" height="100" x="0" y="0" /><rect style="fill-opacity:1;stroke-width:0" id="rect13351-41" width="40" height="40" x="0" y="60" /><rect style="fill-opacity:1;stroke-width:0" id="rect13353-8" width="90" height="40" x="0" y="10" /><rect style="fill-opacity:1;stroke-width:0" id="rect13355-8" width="50" height="40" x="50" y="60" /></g></pattern><pattern xlink:href="#Strips1_5-9" preserveAspectRatio="xMidYMid" id="pattern88-2" patternTransform="matrix(0,0.1,-0.1,0,0,0)" x="0" y="0" /><pattern patternUnits="userSpaceOnUse" width="6" height="1" patternTransform="translate(0,0) scale(2,2)" preserveAspectRatio="xMidYMid" id="Strips1_5-9" style="fill:#000000">&#10;      <rect style="stroke:none" x="0" y="-0.5" width="1" height="2" id="rect164-7" />&#10;    </pattern><linearGradient xlink:href="#linearGradient64" id="linearGradient115" gradientUnits="userSpaceOnUse" x1="235.37469" y1="21.204893" x2="244.71271" y2="28.017914" gradientTransform="translate(225.97675,-1.5691325)" /><linearGradient xlink:href="#linearGradient64" id="linearGradient116" gradientUnits="userSpaceOnUse" x1="247.16119" y1="22.064793" x2="255.86038" y2="28.017918" gradientTransform="translate(225.97675,-1.5691325)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient117" gradientUnits="userSpaceOnUse" x1="221.27644" y1="17.586765" x2="232.91472" y2="17.586765" gradientTransform="translate(225.97675,-1.5691325)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient118" gradientUnits="userSpaceOnUse" x1="221.19521" y1="26.766003" x2="232.82535" y2="26.766003" gradientTransform="translate(225.97675,-1.5691325)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient119" gradientUnits="userSpaceOnUse" x1="259.37646" y1="17.586765" x2="271.01471" y2="17.586765" gradientTransform="translate(225.97675,-1.5691325)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient120" gradientUnits="userSpaceOnUse" x1="259.2952" y1="26.766003" x2="270.92535" y2="26.766003" gradientTransform="translate(225.97675,-1.5691325)" /><linearGradient xlink:href="#linearGradient70" id="linearGradient123" x1="441.69827" y1="19.838341" x2="448.43146" y2="19.838341" gradientUnits="userSpaceOnUse" /><linearGradient xlink:href="#linearGradient70" id="linearGradient124" x1="441.64957" y1="25.727648" x2="448.37787" y2="25.727648" gradientUnits="userSpaceOnUse" /></defs><g id="layer2" transform="translate(-436.28734)"><path id="rect41-4-8" style="fill:#f1f1f1;fill-opacity:1;stroke-width:0.411538;stroke-linecap:square;paint-order:stroke markers fill" d="m 440.7262,17.675454 h 7.85235 v 12.798296 h -7.85235 z" /><path id="rect42-0-5" style="fill:url(#linearGradient123);stroke-width:0.426629;stroke-linecap:square;paint-order:stroke markers fill" d="m 441.69828,18.717809 h 6.73317 v 2.241064 h -6.73317 z" /><path id="rect43-7-7" style="fill:url(#linearGradient124);stroke-width:0.426629;stroke-linecap:square;paint-order:stroke markers fill" d="m 441.64958,21.688522 h 6.7283 v 8.078252 h -6.7283 z" /><path id="rect49" style="opacity:1;fill:#414141;stroke-width:1.03678;stroke-linecap:square;paint-order:stroke markers fill" d="m 442.63178,8.9355392 h 17.78985 v 8.6918428 h -21.49402 z" /><path style="opacity:1;fill:none;fill-opacity:1;stroke:#302c2a;stroke-width:0.580496;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 458.8411,8.9761553 h -15.76252" id="path50" /><path style="opacity:1;fill:none;fill-opacity:1;stroke:#302c2a;stroke-width:0.517811;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 439.24595,17.576586 h 8.0232" id="path51" /><path id="rect51" style="opacity:1;fill:#948319;fill-opacity:1;stroke:#3b3634;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" d="m 440.72079,30.299601 h 6.54124 v 10.316486 h -6.54124 z" /><rect style="fill:#ffffff;fill-opacity:1;stroke:#e5e5e5;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" id="rect88-1" width="10.649479" height="26.127604" x="460.92673" y="13.247536" /><path id="path121" style="opacity:1;fill:url(#pattern122);fill-opacity:1;stroke:#3b3634;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" d="m 440.72079,30.299601 h 6.54124 v 10.316486 h -6.54124 z" /><path id="path79-1" style="fill:#968334;fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 445.16914,32.56075 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><path id="rect30-8-27" style="fill:url(#pattern11-8);fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 445.16914,32.56075 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><path id="path125" style="opacity:1;fill:url(#pattern126);fill-opacity:1;stroke-width:1.03678;stroke-linecap:square;paint-order:stroke markers fill" d="m 442.63178,8.9355392 h 17.78985 v 8.6918428 h -21.49402 z" /><path id="path25-4-9" style="fill:#414141;fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 499.00458,12.310684 -16.06221,-0.682543 h -23.66933 l -14.50441,0.682543 27.11797,-9.3871055 z" /><path id="rect25-2-1" style="fill:#302c2a;fill-opacity:1;stroke:none;stroke-width:0.0795385;stroke-linecap:square;paint-order:stroke markers fill" d="m 444.85082,11.725081 14.73106,-0.120338 h 23.3848 l 15.81024,0.120338 v 1.10675 l -15.86856,-0.120338 h -23.3848 l -14.67274,0.120338 z" /><rect style="fill:#e5e5e5;fill-opacity:1;stroke:#e5e5e5;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26-1-0" width="24.067005" height="27.844791" x="460.04669" y="12.697518" /><rect style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.11265;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect89-8" width="11.11319" height="25.726902" x="460.7785" y="13.58533" /><rect style="opacity:0.579137;fill:url(#linearGradient115);fill-opacity:1;stroke:#787666;stroke-width:0.093878;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27-3-3" width="8.3181" height="23.871012" x="462.3244" y="14.513274" /><rect style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.11265;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect90-78" width="11.11319" height="25.726902" x="472.12634" y="13.58533" /><rect style="opacity:0.579137;fill:url(#linearGradient116);fill-opacity:1;stroke:#787666;stroke-width:0.0954728;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect28-7-1" width="8.6037045" height="23.869417" x="473.18567" y="14.514076" /><rect style="fill:#fbfbfb;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29-0-0" width="28.617632" height="1.0721303" x="457.2937" y="40.033638" rx="1.3296698" /><path id="rect41-6" style="fill:#e5e5e5;fill-opacity:1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 445.95349,12.646496 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path90-5" style="fill:#ffffff;fill-opacity:1;stroke-width:0.853368;stroke-linecap:square;paint-order:stroke markers fill" d="m 446.45945,13.569933 h 13.22577 v 4.730031 h -13.22577 z" /><path id="rect42-5" style="opacity:0.651079;fill:url(#linearGradient117);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 447.2532,14.271139 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path92-9" style="fill:#ffffff;fill-opacity:1;stroke-width:1.45632;stroke-linecap:square;paint-order:stroke markers fill" d="m 446.45945,18.448192 h 13.22577 v 13.775473 h -13.22577 z" /><path id="rect43-0" style="opacity:0.654676;fill:url(#linearGradient118);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 447.17196,18.901373 h 11.63014 v 12.590987 h -11.63014 z" /><path id="path43-9" style="fill:#e5e5e5;fill-opacity:1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 484.05349,12.646496 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path98-0" style="fill:#ffffff;fill-opacity:1;stroke-width:0.853368;stroke-linecap:square;paint-order:stroke markers fill" d="m 484.49336,13.569933 h 13.22577 v 4.730031 h -13.22577 z" /><path id="path44-1" style="opacity:0.661871;fill:url(#linearGradient119);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 485.3532,14.271139 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path99-6" style="fill:#ffffff;fill-opacity:1;stroke-width:1.45632;stroke-linecap:square;paint-order:stroke markers fill" d="m 484.49336,18.448192 h 13.22577 v 13.775473 h -13.22577 z" /><path id="path45-0" style="opacity:0.645683;fill:url(#linearGradient120);stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 485.27196,18.901373 h 11.63014 v 12.590987 h -11.63014 z" /><path id="path87-8" style="fill:url(#pattern120);fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 499.00458,12.310684 -16.06221,-0.682543 h -23.66933 l -14.50441,0.682543 27.11797,-9.3871055 z" /><path id="path91-8" style="fill:url(#pattern121);fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 499.00458,12.310684 -16.06221,-0.682543 h -23.66933 l -14.50441,0.682543 27.11797,-9.3871055 z" /></g></svg>
            '''
        },
        {
            "title": "Other",
            "description": "Combines a lean-to element with a rounded Victorian or Edwardian extension, creating a versatile, multi-functional, zoned living area.",
            "svg" : '''

                <svg width="243.88751" height="184.9209" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"></svg>
            '''
        }

    ]

    services = [
        {
            "title" : "Conservatory Roof Conversions",
        },
        {
            "title" : "Gard Room Installations",
        },
        {
            "title" : "Interior Decorating & Desgin",
        },
        
    ]

    context = {
        'page' : page,
        'welcome_cards' : welcome_cards,
        'con_shapes' : con_shapes,
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
    about_numbers = [
        {
            'text': 'Total Projects',
            'subtext': '1,028',
            'svg' : ''
        },
        {
            'text': 'Satisfied Customers',
            'subtext': '1,324',
            'svg' : ''
        },
        {
            'text': 'Certifications',
            'subtext': '3',
            'svg' : ''
        },
        {
            'text': 'National Awards',
            'subtext': '1',
            'svg' : ''
        },

    ]
    page = {
            'tag' : 'about',
            'body_title' : 'About Us',
            'title' : 'About CRC Group',
            'body_intro' : 'We are The Conservatory Roof Convrersion Group. And our specialism is in the name. We offer premium external space installations and conversions.'
        }
    context = {
        'page' :page,
        'about_numbers' : about_numbers


    }
    return render_template('pages/about.html', **context)

@main.route('/services/')
def service_list():
    page = {
        'tag' : 'services',
        'body_title' : 'Our Services',
        'title' : 'Our Services | CRC Group',
        'body_intro' : 'We are The Conservatory Roof Convrersion Group. And our specialism is in the name. We offer premium external space installations and conversions.'
    }
    services = [
        {
             
            'title' : 'Roof Conversions',
            'short_desc' : 'We utilise modern state of the art tiling solutions to maximise your conservatories light and tempature stabilisation, Allowing comfort all-year round',
            'svg' : '',
            'benefits': {
                'text' : [
                    'Tailored Roof Designs',
                    'Industry Experience'
                ]
            }

            
        },
        {
            'title' : 'Garden Rooms',
            'short_desc' : 'We convert open spaces into fully functioning exterior buildings, with functioning electricity and gas, and a regulated temprature all yar round.',
            'svg' : '' ,
            'benefits': {
                'text' : [
                    'Tailored Roof Designs',
                    'Industry Experience'
                ]
            }

        },
         {
            'title' : 'Extension Redesigns',
            'short_desc' : 'Feel as good on the inside as you do on the out! Interior redesigns to match your premium new exterior spaces. From Painting & Decorating to Furnishing.',
            'svg' : '' ,
            'benefits': {
                'text' : [
                    'Tailored Roof Designs',
                    'Industry Experience'
                ]
            }

        }
    ]
    context = {
        'page' : page,
        'services' : services
    }
    return render_template('pages/service-list.html', **context)

      

@main.route('/services/<string:slug>/')
def service_detail(slug):
    pass

@main.route('/projects/')
def project_list():
    page = {
        'tag' : 'projects',
        'body_title' : 'Projects',
        'title' : 'Our Work | CRC Group',
        'body_intro' : 'We are The Conservatory Roof Convrersion Group. And our specialism is in the name. We offer premium external space installations and conversions.'
    }
    projects = [
        {
            'title': 'St Anthony\'s Conversion',
            'short_desc' : 'Lorem Ipsum Dolar Amet some other stuff that goes in here.!'
        },
         {
            'title': 'Stone\'s Cross Garden Room',
            'short_desc' : 'Lorem Ipsum Dolar Amet some other stuff that goes in here.!'
        },

    ]
    context = {
        'page' : page,
        'projects' : projects
    } 
    return render_template('pages/project-list.html', **context)


@main.route('/projects/<string:slug>/')
def project_detail(slug):
    project = {
        'parent_page' : {'title' : 'Projects', 'link' : '/projects'},
        'title' : 'Stones Cross Conversion',
        'intro' : 'An envirotile roof conversion solution in Stones Cross', 
        'location': {'title' : 'Eastbourne'},
        'short_desc': 'Joan contacted us requesting a roof conversion after months of mulling it over.\n'
        'After she contacted us, we arranged a free, no strings attached quote before week\'s end. We are proud of our flexibility, and arranged a date and time that worked around her schedule.\n'
        'Joan opted for the envirotile terracota finish on her victorian style conservatory.\n'
    }
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
    page = {
        'body_title' : 'Our Blog',
        'body_intro': 'Thoughts & Musings From the CRC Group. Latest Insights, Trends and More.',
        'tag' : 'blog'
    }
    articles = [
        {
            "title": 'Summer 2026 Design Guide', 
            "abstract": "The seasons are fast changing. Let's take a look at some of the latest interior design trends."
        }
    ]

    categories = [
        {
            "title" : "Latest Trends",
        },
         {
            "title" : "Best Practices",
        },
    ]
    context = {
        'page' : page,
        'articles' : articles,
        'categories' : categories
    }
    return render_template('pages/article-list.html', **context)

