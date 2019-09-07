from flask import Flask, render_template, request, redirect, session, url_for
from flask_material import Material
from models import LoginForm

application = Flask(__name__)
Material(application) 
application.config ['SECRET_KEY'] = 'sus1loh4rj0'

@application.route('/', methods =['GET', 'POST'])
def index():
    form = LoginForm()
    if request.method == 'POST':
        namaUser = form.namaUser.data
        kataSandi = form.kataSandi.data
        if namaUser == 'onix' and kataSandi == '4ku4ku':
            # return render_template('response.html', namaUser=namaUser)
            return redirect(url_for('dashboard', namaUser=namaUser))

        else:
            pesan = 'anda bukan admin'
            return render_template('form.html', pesan=pesan, form=form)
    return render_template('form.html', form=form)

@application.route('/dashboard/<namaUser>')
def dashboard(namaUser):
    return render_template('response.html', namaUser=namaUser)



if __name__== '__main__':
    application.run(host='0.0.0.0', debug=True)

        

