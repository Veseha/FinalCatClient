import json
from flask import Flask, render_template, url_for
from random import choice


app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


with open("templates/info.json", "rt", encoding="utf8") as f:
    news_list = json.loads(f.read())['info']


@app.route('/member')
def index():
    print(news_list)
    a = choice(news_list)
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='info',
                           username=user, name_header='Миссия Колонизация Марса', name_header_2='Mars one',
                           list=a)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')