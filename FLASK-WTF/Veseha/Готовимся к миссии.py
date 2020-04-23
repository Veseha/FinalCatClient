import json
from flask import Flask, render_template, url_for


app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<titel>')
@app.route('/index/<titel>')
def index(titel):
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title=titel,
                           username=user, name_header='Миссия Колонизация Марса', name_header_2='Mars one')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')