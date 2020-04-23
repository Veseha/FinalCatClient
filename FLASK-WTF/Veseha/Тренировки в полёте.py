import json
from flask import Flask, render_template, url_for


app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/training/<prof>')
def index(prof):
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='GoToMars',
                           username=user, name_header='Миссия Колонизация Марса',
                           name_header_2='Mars one', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')