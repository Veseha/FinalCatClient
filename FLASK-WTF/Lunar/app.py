from flask import Flask, render_template

site = Flask(__name__)
site.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@site.route('/')
@site.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница', username=user)


site.run(host='127.0.0.1', port=8080)