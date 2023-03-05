from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "OUT"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2') 

        if len(email) < 4:
            flash('Email phải dài hơn 4', category='error')
        elif len(firstName) < 2:
            flash('Tên phải dài hơn 1', category='error')
        elif len(lastName) < 2:
            flash('Họ và tên đệm phải dài hơn 1', category='error')
        elif password1 != password2:
            flash('Nhập lại mật khẩu sai', category='error')
        else:
            #add user to database
            flash('Đã thêm tài khoản', category='success')

    return render_template("sign_up.html")
