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
    page = {}
    why_us = [
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
            "svg" : ''''''
            
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
                
                <svg width="140px" height="107px" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1" /><g id="layer2" transform="translate(-142.39713,-1.5863839)"><g id="g41" transform="matrix(0.50762868,0,0,0.50762868,83.87136,-13.732813)"><path id="rect30" style="opacity:1;fill:#302c2a;fill-opacity:1;stroke:#787666;stroke-width:0.185208;stroke-linecap:square;paint-order:stroke markers fill" d="m 135.46562,115.11501 26.65207,2.11666 h 45.37746 l 27.45505,-2.11666 v 19.7593 l -27.34017,4.23333 h -45.37746 l -26.76695,-4.23333 z" transform="translate(-9.0980042,-18.845866)" /><path id="path25" style="opacity:1;fill:#414141;fill-opacity:1;stroke:#666557;stroke-width:0.185208;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" transform="matrix(0.26458332,0,0,0.26458332,5.5142228,11.028446)" d="m 849.71841,179.27837 -119.59045,-10 h -176.22906 l -107.99195,10 201.90573,-81.710979 z" /><path id="rect25" style="opacity:1;fill:#302c2a;fill-opacity:1;stroke:none;stroke-width:0.185208;stroke-linecap:square;paint-order:stroke markers fill" d="m 132.75369,77.37365 29.01936,-2.416074 h 46.06674 l 31.14528,2.416074 v 3.046213 l -31.26016,-2.416074 h -46.06674 l -28.90448,2.416074 z" transform="translate(-9.0980042,-18.845866)" /><rect style="opacity:1;fill:#414141;fill-opacity:1;stroke:#414141;stroke-width:0.185208;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26" width="44.921307" height="54.965832" x="162.68871" y="78.070404" transform="translate(-9.0980042,-18.845866)" /><rect style="opacity:0.894587;fill:#6dabcf;fill-opacity:1;stroke:#787666;stroke-width:0.180444;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27" width="15.598608" height="47.029041" x="158.07542" y="62.799244" /><rect style="opacity:0.894587;fill:#6dabcf;fill-opacity:1;stroke:#787666;stroke-width:0.180444;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect28" width="15.598608" height="47.029041" x="179.08238" y="62.799244" /><rect style="opacity:1;fill:#414141;fill-opacity:1;stroke:#414141;stroke-width:0.185208;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29" width="56.37513" height="2.1120365" x="157.26549" y="131.92105" rx="2.619375" transform="translate(-9.0980042,-18.845866)" /><path id="rect31" style="fill:#7cb4d4;fill-opacity:1;stroke:#787666;stroke-width:0.191832;stroke-linecap:square;paint-order:stroke markers fill" d="m 126.37078,61.269202 27.36528,-2.096409 v 38.760377 l -27.36528,-1.607758 z" /><path style="fill:none;fill-opacity:1;stroke:#414141;stroke-width:2.77812;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 152.31532,60.713892 -24.55479,1.866794 v 32.539661 l 24.56988,1.865946 c 0.067,-11.890086 -0.0762,-24.382297 -0.0151,-36.272401 z" id="path33" /><path style="fill:none;fill-opacity:1;stroke:#414141;stroke-width:2.75194;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 151.66504,71.424295 -23.81017,0.692047" id="path34" /><path style="fill:none;fill-opacity:1;stroke:#414141;stroke-width:2.51354;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 138.77461,95.809623 v -32.991272" id="path35" /><path id="path36" style="fill:#7cb4d4;fill-opacity:1;stroke:#787666;stroke-width:0.191832;stroke-linecap:square;paint-order:stroke markers fill" d="m 225.87023,61.269202 -27.36528,-2.096409 v 38.760377 l 27.36528,-1.607758 z" /><path style="fill:none;fill-opacity:1;stroke:#414141;stroke-width:2.77812;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 199.92569,60.713892 24.55479,1.866794 v 32.539661 l -24.56988,2.067831 c -0.067,-11.890086 0.0762,-24.584182 0.0151,-36.474286 z" id="path37" /><path style="fill:none;fill-opacity:1;stroke:#414141;stroke-width:2.75194;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 200.57597,71.424295 23.81017,0.692047" id="path38" /><path style="fill:none;fill-opacity:1;stroke:#414141;stroke-width:2.51354;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 213.4664,95.809623 v -32.991272" id="path39" /><path style="opacity:1;fill:none;fill-opacity:1;stroke:#484848;stroke-width:0.687917;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 154.90976,53.938165 21.80387,-15.027952 20.92425,15.352881" id="path40" /></g></g></svg>


            
            '''
        },
        {
            "title": "Edwardian",
            "description": "Characterized by a square or rectangular footprint, this style maximizes floor space with flat walls and a timeless, symmetrical pitched roof.",
            "svg" : '''
                

                <svg class="mx-auto" width="140px" height="107px" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1" /><g id="layer2" transform="translate(-214.32628,-0.6498566)"><path id="rect30-8" style="opacity:1;fill:#302c2a;fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 219.19239,34.129885 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><path id="path25-4" style="fill:#414141;fill-opacity:1;stroke:#666557;stroke-width:0.0248753;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 273.02783,13.879819 -16.06221,-0.682543 h -23.66933 l -14.50441,0.682543 27.11797,-9.3871082 z" /><path id="rect25-2" style="fill:#302c2a;fill-opacity:1;stroke:none;stroke-width:0.0795385;stroke-linecap:square;paint-order:stroke markers fill" d="m 218.87407,13.294216 14.73106,-0.120338 h 23.3848 l 15.81024,0.120338 v 1.10675 l -15.86856,-0.120338 h -23.3848 l -14.67274,0.120338 z" /><rect style="opacity:1;fill:#414141;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26-1" width="24.067005" height="27.844791" x="234.06995" y="14.266648" /><rect style="opacity:1;fill:#6dabcf;fill-opacity:1;stroke:#787666;stroke-width:0.093878;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27-3" width="8.3181" height="23.871012" x="236.34767" y="16.082407" /><rect style="opacity:1;fill:#6dabcf;fill-opacity:1;stroke:#787666;stroke-width:0.0954728;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect28-7" width="8.6037045" height="23.869417" x="247.20894" y="16.083208" /><rect style="fill:#414141;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29-0" width="28.617632" height="1.0721303" x="231.31697" y="41.602776" rx="1.3296698" /><g id="g43" transform="translate(-2.2745009,0.64985777)"><path id="rect41" style="opacity:1;fill:#414141;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 222.25124,13.565773 h 14.07696 v 19.947775 h -14.07696 z" /><path id="rect42" style="opacity:1;fill:#99a1c1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 223.55095,15.190416 h 11.63827 v 3.492984 h -11.63827 z" /><path id="rect43" style="opacity:1;fill:#99a1c1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 223.46971,19.82065 h 11.63014 v 12.590987 h -11.63014 z" /></g><g id="g45" transform="translate(35.825497,0.64985777)"><path id="path43" style="opacity:1;fill:#414141;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 222.25124,13.565773 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path44" style="opacity:1;fill:#99a1c1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 223.55095,15.190416 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path45" style="opacity:1;fill:#99a1c1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 223.46971,19.82065 h 11.63014 v 12.590987 h -11.63014 z" /></g></g></svg>
            
            '''
        },
        {
            "title": "Gable-Ended",
            "description": "Features a high, upright front roof that mimics the gable end of a house, creating a grand, light-filled interior with impressive height.",
            "svg" : '''
                <svg class="mx-auto" width="140px" height="107px" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1" /><g id="layer2" transform="translate(-287.23021)"><path id="rect30-8-9" style="fill:#302c2a;fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 293.29364,34.171455 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><path id="path25-4-4" style="fill:#99a1c1;fill-opacity:1;stroke:#414141;stroke-width:1.7182;stroke-linecap:square;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 347.12908,13.921389 -16.06221,-0.682543 h -23.66933 l -14.50441,0.682543 27.11797,-11.5037744 z" /><rect style="fill:#414141;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26-1-0" width="24.067005" height="27.844791" x="308.17117" y="14.308219" /><rect style="fill:#6dabcf;fill-opacity:1;stroke:#787666;stroke-width:0.093878;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27-3-7" width="8.3181" height="23.871012" x="310.44891" y="16.123976" /><rect style="fill:#6dabcf;fill-opacity:1;stroke:#787666;stroke-width:0.0954728;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect28-7-3" width="8.6037045" height="23.869417" x="321.31018" y="16.124777" /><rect style="fill:#414141;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29-0-4" width="28.617632" height="1.0721303" x="305.41821" y="41.644348" rx="1.3296698" /><g id="g43-1" transform="translate(71.826742,0.69142819)"><path id="rect41-5" style="opacity:1;fill:#414141;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 222.25124,13.565773 h 14.07696 v 19.947775 h -14.07696 z" /><path id="rect42-9" style="opacity:1;fill:#99a1c1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 223.55095,15.190416 h 11.63827 v 3.492984 h -11.63827 z" /><path id="rect43-0" style="opacity:1;fill:#99a1c1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 223.46971,19.82065 h 11.63014 v 12.590987 h -11.63014 z" /></g><g id="g45-1" transform="translate(109.92674,0.69142819)"><path id="path43-1" style="opacity:1;fill:#414141;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 222.25124,13.565773 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path44-6" style="opacity:1;fill:#99a1c1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 223.55095,15.190416 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path45-3" style="opacity:1;fill:#99a1c1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 223.46971,19.82065 h 11.63014 v 12.590987 h -11.63014 z" /></g><path style="opacity:1;fill:#99a1c1;fill-opacity:1;stroke:#414141;stroke-width:0.950912;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 308.7635,13.62554 v -6.5786488" id="path46" /><path style="opacity:1;fill:#99a1c1;fill-opacity:1;stroke:#414141;stroke-width:0.950912;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 331.76181,13.76914 v -6.5786488" id="path47" /><path style="opacity:1;fill:#99a1c1;fill-opacity:1;stroke:#414141;stroke-width:0.950912;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 320.04034,13.555798 v -11.2639781" id="path48" /><path id="rect25-2-4" style="fill:#302c2a;fill-opacity:1;stroke:none;stroke-width:0.0795385;stroke-linecap:square;paint-order:stroke markers fill" d="m 292.97532,13.335786 14.73106,-0.120338 h 23.3848 l 15.81024,0.120338 v 1.10675 l -15.86856,-0.120338 h -23.3848 l -14.67274,0.120338 z" /></g></svg>
            '''
        },
        {
            "title": "Lean-To",
            "description": "A simple, modern option with a single sloped roof that leans against the main property, making it ideal for bungalows or limited spaces.",
            "svg" : '''

                <svg class="mx-auto" width="960px" height="107px" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1" /><g id="layer2" transform="translate(-361.75877)"><path id="rect30-8-9-4" style="fill:#302c2a;fill-opacity:1;stroke:#787666;stroke-width:0.0940169;stroke-linecap:square;paint-order:stroke markers fill" d="m 367.07715,33.926416 14.58769,0.01614 h 23.0349 l 16.05364,-0.01614 v 11.08872 l -15.99532,0.03229 h -23.0349 l -14.64601,-0.03229 z" /><rect style="fill:#414141;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26-1-0-8" width="24.067005" height="27.844791" x="381.95468" y="14.06318" /><rect style="fill:#6dabcf;fill-opacity:1;stroke:#787666;stroke-width:0.093878;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27-3-7-1" width="8.3181" height="23.871012" x="384.23242" y="15.878937" /><rect style="fill:#6dabcf;fill-opacity:1;stroke:#787666;stroke-width:0.0954728;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect28-7-3-4" width="8.6037045" height="23.869417" x="395.09369" y="15.879738" /><rect style="fill:#414141;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29-0-4-1" width="28.617632" height="1.0721303" x="379.20172" y="41.399307" rx="1.3296698" /><g id="g43-1-5" transform="translate(145.61025,0.4463893)"><path id="rect41-5-6" style="opacity:1;fill:#414141;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 222.25124,13.565773 h 14.07696 v 19.947775 h -14.07696 z" /><path id="rect42-9-9" style="opacity:1;fill:#99a1c1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 223.55095,15.190416 h 11.63827 v 3.492984 h -11.63827 z" /><path id="rect43-0-5" style="opacity:1;fill:#99a1c1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 223.46971,19.82065 h 11.63014 v 12.590987 h -11.63014 z" /></g><g id="g45-1-4" transform="translate(183.71025,0.4463893)"><path id="path43-1-9" style="opacity:1;fill:#414141;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 222.25124,13.565773 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path44-6-2" style="opacity:1;fill:#99a1c1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 223.55095,15.190416 h 11.63827 v 3.492984 h -11.63827 z" /><path id="path45-3-6" style="opacity:1;fill:#99a1c1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 223.46971,19.82065 h 11.63014 v 12.590987 h -11.63014 z" /></g><path id="rect25-2-4-6" style="fill:#302c2a;fill-opacity:1;stroke:none;stroke-width:0.0674504;stroke-linecap:square;paint-order:stroke markers fill" d="m 366.75883,13.401588 14.73106,-0.08654 h 23.3848 l 15.81024,0.08654 v 0.795909 l -15.86856,-0.08654 h -23.3848 l -14.67274,0.08654 z" /><path id="rect48" style="opacity:1;fill:#414141;fill-opacity:1;stroke:none;stroke-width:0.998157;stroke-linecap:square;stroke-dasharray:none;paint-order:stroke markers fill" d="m 368.38886,9.242437 h 50.65104 l 1.66388,4.141124 h -53.97879 z" /><path id="path49" style="fill:#302c2a;fill-opacity:1;stroke:none;stroke-width:0.0629069;stroke-linecap:square;paint-order:stroke markers fill" d="m 368.34633,8.7427017 13.14356,-0.075274 h 23.3848 l 14.22274,0.075274 v 0.6922955 l -14.28106,-0.075274 h -23.3848 l -13.08524,0.075274 z" /></g></svg>

            '''
        },
        {
            "title": "P-Shaped",
            "description": "Combines a lean-to element with a rounded Victorian or Edwardian extension, creating a versatile, multi-functional, zoned living area.",
            "svg" : '''
                <svg class="mx-auto" width="980px" height="107px" viewBox="0 0 64.528571 48.926983" version="1.1" id="svg1" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"><defs id="defs1" /><g id="layer2" transform="translate(-436.28734)"><g id="g50" transform="translate(1.0583333,-0.17231946)"><path id="rect41-4-8" style="fill:#414141;stroke-width:0.411538;stroke-linecap:square;paint-order:stroke markers fill" d="m 440.7262,17.847773 h 7.85235 v 12.798296 h -7.85235 z" /><path id="rect42-0-5" style="fill:#99a1c1;stroke-width:0.426629;stroke-linecap:square;paint-order:stroke markers fill" d="m 441.69828,18.890128 h 6.73317 v 2.241064 h -6.73317 z" /><path id="rect43-7-7" style="fill:#99a1c1;stroke-width:0.426629;stroke-linecap:square;paint-order:stroke markers fill" d="m 441.64958,21.860841 h 6.7283 v 8.078252 h -6.7283 z" /></g><path id="rect49" style="opacity:1;fill:#414141;stroke-width:1.03678;stroke-linecap:square;paint-order:stroke markers fill" d="m 443.69012,8.9355392 h 17.78985 v 8.6918428 h -21.49402 z" /><path style="opacity:1;fill:none;fill-opacity:1;stroke:#302c2a;stroke-width:0.580496;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 459.89944,8.9761553 h -15.76252" id="path50" /><path id="rect30-8-8" style="fill:#302c2a;fill-opacity:1;stroke:#787666;stroke-width:0.089503;stroke-linecap:square;paint-order:stroke markers fill" d="m 448.20004,33.212948 13.21519,0.01615 h 20.86763 l 14.54321,-0.01615 v 11.093222 l -14.49038,0.0323 h -20.86763 l -13.26802,-0.0323 z" /><path id="path25-4-2" style="fill:#414141;fill-opacity:1;stroke:#666557;stroke-width:0.0236887;stroke-linecap:square;stroke-opacity:1;paint-order:stroke markers fill" d="m 496.98308,13.022924 -14.56527,-0.153426 h -21.46343 l -13.15265,0.153426 24.59067,-9.3877958 z" /><path id="rect25-2-3" style="fill:#302c2a;fill-opacity:1;stroke:none;stroke-width:0;stroke-linecap:square;stroke-dasharray:none;paint-order:stroke markers fill" d="m 447.76909,12.627305 13.41303,-0.08091 h 21.29248 l 14.39565,0.08091 v 0.744103 l -14.44875,-0.08091 h -21.29249 l -13.35992,0.08091 z" /><rect style="fill:#414141;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect26-1-1" width="24.067005" height="27.844791" x="460.55252" y="13.35197" /><rect style="fill:#6dabcf;fill-opacity:1;stroke:#787666;stroke-width:0.093878;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect27-3-6" width="8.3181" height="23.871012" x="462.83023" y="15.167728" /><rect style="fill:#6dabcf;fill-opacity:1;stroke:#787666;stroke-width:0.0954728;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect28-7-6" width="8.6037045" height="23.869417" x="473.6915" y="15.16853" /><rect style="fill:#414141;fill-opacity:1;stroke:#414141;stroke-width:0.0940169;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" id="rect29-0-9" width="28.617632" height="1.0721303" x="457.79953" y="40.688095" rx="1.3296698" /><g id="g43-6" transform="matrix(0.86942676,0,0,1,255.06619,-0.26482094)"><path id="rect41-4" style="opacity:1;fill:#414141;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 222.25124,13.565773 h 14.07696 v 19.947775 h -14.07696 z" /><path id="rect42-0" style="opacity:1;fill:#99a1c1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 224.15959,15.190416 h 11.02963 v 3.492984 h -11.02963 z" /><path id="rect43-7" style="opacity:1;fill:#99a1c1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 224.07835,19.82065 h 11.0215 v 12.590987 h -11.0215 z" /></g><g id="g45-14" transform="matrix(0.86126593,0,0,1,293.14187,-0.26482094)"><path id="path43-4" style="opacity:1;fill:#414141;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 222.25124,13.565773 h 14.07696 v 19.947775 h -14.07696 z" /><path id="path44-5" style="opacity:1;fill:#99a1c1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 223.55095,15.190416 h 11.02386 v 3.492984 h -11.02386 z" /><path id="path45-36" style="opacity:1;fill:#99a1c1;stroke-width:0.687917;stroke-linecap:square;paint-order:stroke markers fill" d="m 223.46971,19.82065 h 11.01573 v 12.590987 h -11.01573 z" /></g><path style="opacity:1;fill:none;fill-opacity:1;stroke:#302c2a;stroke-width:0.517811;stroke-linecap:square;stroke-linejoin:miter;stroke-dasharray:none;stroke-opacity:1;paint-order:stroke markers fill" d="m 440.30429,17.576586 h 8.0232" id="path51" /><path id="rect51" style="opacity:1;fill:#302c2a;fill-opacity:1;stroke:#3b3634;stroke-width:0;stroke-linecap:square;paint-order:stroke markers fill" d="m 441.77913,30.299601 h 6.54124 v 10.316486 h -6.54124 z" /></g></svg>

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
        'why_us' : why_us,
        'con_shapes' : con_shapes,
        'services' : services
    }
    return render_template('pages/index.html', **context)

@main.route('/contact')
def contact():
    pass

@main.route('/about')
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