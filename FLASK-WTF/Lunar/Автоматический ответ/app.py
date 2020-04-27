from flask import Flask, render_template

site = Flask(__name__)
site.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@site.route('/')
@site.route('/index')
@site.route('/answer')
@site.route('/auto_answer')
def index():
    ans = {
        "title": "congratulations",
        "surname": "watson",
        "name": "wat",
        "education": "high",
        "profession": "engineer",
        "sex": "male",
        "motivation": "big",
        "ready": True
    }

    return render_template('index.html', title='Домашняя страница', ans=ans)


site.run(host='127.0.0.1', port=8080)
