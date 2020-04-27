from flask import Flask, render_template

site = Flask(__name__)
site.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@site.route('/')
@site.route('/index')
def index():
    return render_template('index.html', title='Домашняя страница')


@site.route('/training/<prof>')
def PROf(prof):

    if 'инженер' in prof:
        pagename = 'training_tech.html'
    elif 'врач' in prof:
        pagename = 'training_science.html'
    else:
        pagename = 'shipmap.html'
    return render_template(pagename, title='Домашняя страница')


site.run(host='127.0.0.1', port=8080)
