from flask import Flask
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/blogs.sqlite")


def main():
    # ---------------------- тестирование системы --------------------
    # ----------- добавление пользователя -------------
    # user = User()
    # user.name = "Пользов3атель 2"
    # user.about = "биография пользователя 3"
    # user.email = "ema2i4l@email.ru"

    # --------- создание сесии ------------------------
    session = db_session.create_session()
    # session.add(user) # ------- добавление инфы
    session.commit()

    # --------- вывод инфы ----------------------------
    user = session.query(User).first()
    print(user.name)

    for user in session.query(User).all():
        print(user)


    app.run()




if __name__ == '__main__':
    main()