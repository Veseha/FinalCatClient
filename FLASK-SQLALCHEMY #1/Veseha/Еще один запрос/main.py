<<<<<<< HEAD
from flask import Flask
# from . import global_init
# from . import create_session
# from . import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
global_init(input())
session = create_session()
a = session.query(Department).filter(Department.id == 1).first()
# print(a)
# print(a.members)
# print(type(a.members))
b = [str(i) for i in str(a.members).split(', ')]
# b.append(str(a.chief))

c = []
su = 0
g = {}
for i in b:
    g[i] = 0
# print(b, '---')
for i in session.query(Jobs).all():
    list_one = str(i.collaborators).split(', ')
    list_one.append(str(i.team_leader))
    # print(list_one)

    for j in list_one:
        if j in b:
            g[j] += int(i.work_size)
            # u = session.query(User).filter(User.id == j).first()
            # c.append(str(u.surname) + ' ' + str(u.name))
# print(g)
for i in g.keys():
    if g[i] > 25:
        u = session.query(User).filter(User.id == i).first()
        print(str(u.surname) + ' ' + str(u.name))
    # print('\n'.join(set(c)))

# for i in b:
#     job = session.query(Jobs).filter(Jobs.id == i).first()
#     u = session.query(User).filter(User.id == job.team_leader).first()
#     print(job.work_size, u.surname, u.name)
#     if job.work_size >= 25:
#         u = session.query(User).filter(User.id == job.team_leader).first()
#         c.append(str(u.surname) + ' ' + str(u.name))
# print('\n'.join(set(c)))


# session.commit()


# print('\n'.join(set(a)))

# fff
# def main():
#     # ---------------------- тестирование системы --------------------
#     # ----------- добавление пользователя -------------
#     # --------- создание сесии ------------------------
#     session = db_session.create_session()
#     # session.add(user) # ------- добавление инфы
#     # session.commit()
#     # session.add(jobs)
#     # session.commit()
#
#     # user = session.query(User).filter(User.id == 1).first()
#     # news = Jobs(title="Вторая новость", content="Уже вторая запись!",
#     #             user=user, is_private=False)
#     # # session.add(news)
#     # session.commit()
#
#     # --------- вывод инфы ----------------------------
#     # print('------------- запрос инфы об об определенном параметре')
#     # user = session.query(User).first()
#     # print(user.name)
#     #
#     # print('------------- вывод всего и вся')
#     for user in session.query(User).all():
#         print(user)
#     #
#     # print('------------- фильтр с операцией AND')
#     # for user in session.query(User).filter(User.id > 1, User.email.notilike("%1%")):
#     #     print(user)
#     #
#     # print('------------- фильтр с операцией OR')
#     # for user in session.query(User).filter((User.id > 1) | (User.email.notilike("%1%"))):
#     #     print(user)
#     #
#     # print('--------- изменение инфы')
#     # user = session.query(User).filter(User.id == 1).first()
#     # print(user)
#     # user.name = "Измененное имя пользователя"
#     # user.created_date = datetime.datetime.now()
#     # session.commit()
#     #
#     # print('---------- удаление инфы по фильтру')
#     # session.query(User).filter(User.id >= 999).delete()
#     # session.commit()
#     #
#     # print('---------- удаление инфы определенного элемента')
#     # # user = session.query(User).filter(User.id == 2).first()
#     # # session.delete(user)
#     # # session.commit()
#     #
#     # print(" ---------- Добавление записи юзеру")
#     # news = News(title="Первая новость", content="Привет блог!",
#     #             user_id=1, is_private=False)
#     # # session.add(news)
#     # session.commit()
#     #
#     # print('----------- Добавление записи вот так')
#
#     #
#     # print('----------- посмотри код, здесь один из лучших спопосбов добавления записи')
#     # user = session.query(User).filter(User.id == 1).first()
#     # news = News(title="Личная запись", content="Эта запись личная",
#     #             is_private=True)
#     # # user.news.append(news)
#     # session.commit()
#     #
#     # print('----------- тупо все новости юзера')
#     # for news in user.news:
#     #     print(news)      # ---------- надо бы добавить __repr__
#     #
#     # # ------------ запуск приложения
#     app.run(port=8080, host='127.0.0.1')


# @app.route("/")
# def index():
#     session = db_session.create_session()
#     news = session.query(News).filter(News.is_private != True)
#     return render_template("index.html", news=news)


# @app.route('/register', methods=['GET', 'POST'])
# def reqister():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         if form.password.data != form.password_again.data:
#             return render_template('register.html', title='Регистрация',
#                                    form=form,
#                                    message="Пароли не совпадают")
#         session = db_session.create_session()
#         if session.query(User).filter(User.email == form.email.data).first():
#             return render_template('register.html', title='Регистрация',
#                                    form=form,
#                                    message="Такой пользователь уже есть")
#         user = User(
#             name=form.name.data,
#             email=form.email.data,
#             about=form.about.data
#         )
#         user.set_password(form.password.data)
#         session.add(user)
#         session.commit()
#         return redirect('/login')
#     return render_template('register.html', title='Регистрация', form=for
=======
from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,  BooleanField, SubmitField, TextAreaField,\
    SubmitField, ValidationError, TextField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
from data import db_session
from data.users import User
from data.news import News
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/blogs.sqlite")


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    about = TextAreaField("Немного о себе")
    submit = SubmitField('Войти')


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
    print('------------- запрос инфы об об определенном параметре')
    user = session.query(User).first()
    print(user.name)

    print('------------- вывод всего и вся')
    for user in session.query(User).all():
        print(user)

    print('------------- фильтр с операцией AND')
    for user in session.query(User).filter(User.id > 1, User.email.notilike("%1%")):
        print(user)

    print('------------- фильтр с операцией OR')
    for user in session.query(User).filter((User.id > 1) | (User.email.notilike("%1%"))):
        print(user)

    print('--------- изменение инфы')
    user = session.query(User).filter(User.id == 1).first()
    print(user)
    user.name = "Измененное имя пользователя"
    user.created_date = datetime.datetime.now()
    session.commit()

    print('---------- удаление инфы по фильтру')
    session.query(User).filter(User.id >= 999).delete()
    session.commit()

    print('---------- удаление инфы определенного элемента')
    # user = session.query(User).filter(User.id == 2).first()
    # session.delete(user)
    # session.commit()

    print(" ---------- Добавление записи юзеру")
    news = News(title="Первая новость", content="Привет блог!",
                user_id=1, is_private=False)
    # session.add(news)
    session.commit()

    print('----------- Добавление записи вот так')
    user = session.query(User).filter(User.id == 1).first()
    news = News(title="Вторая новость", content="Уже вторая запись!",
                user=user, is_private=False)
    # session.add(news)
    session.commit()

    print('----------- посмотри код, здесь один из лучших спопосбов добавления записи')
    user = session.query(User).filter(User.id == 1).first()
    news = News(title="Личная запись", content="Эта запись личная",
                is_private=True)
    # user.news.append(news)
    session.commit()

    print('----------- тупо все новости юзера')
    for news in user.news:
        print(news)      # ---------- надо бы добавить __repr__

    # ------------ запуск приложения
    app.run(port=8080, host='127.0.0.1')


@app.route("/")
def index():
    session = db_session.create_session()
    news = session.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    main()
>>>>>>> flask wtf lunar 2
