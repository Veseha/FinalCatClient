from flask import Flask
from data import db_session
from .data.users import User



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/blogs.sqlite")


def main():
    app.run()
    user = User()
    user.name = "Пользователь 1"
    user.about = "биография пользователя 1"
    user.email = "email@email.ru"
    session = db_session.create_session()
    session.add(user)
    session.commit()


if __name__ == '__main__':
    main()