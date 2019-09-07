from flask import Flask, render_template, request
from models import LoginForm

application = Flask(__name__)
application.config ['SECRET_KEY'] = 'sus1loh4rj0'

@application.route('/', methods =['GET', 'POST'])
def index():
    form = LoginForm()
    if request.method == 'POST':
        namaUser = form.namaUser.data
        kataSandi = form.kataSandi.data
        if namaUser == 'admin' and kataSandi == 'password':
            return render_template('response.html', namaUser=namaUser)
        else:
            pesan = 'anda bukan admin'
            return render_template('form.html', pesan=pesan, form=form)
    return render_template('form.html', form=form)

if __name__== '__main__':
    application.run(host='0.0.0.0', debug=True)

        

