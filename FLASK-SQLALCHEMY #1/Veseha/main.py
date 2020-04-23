from flask import Flask
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/blogs.sqlite")


def main():
    user = User()
    user.name = "Пользователь 2"
    user.about = "биография пользователя 3"
    user.email = "ema2il@email.ru"
    print(user)
    print('----------------------------------------')
    session = db_session.create_session()
    session.add(user)
    session.commit()

    app.run()


if __name__ == '__main__':
    main()