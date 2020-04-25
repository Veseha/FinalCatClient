from flask import Flask
# from . import global_init
# from . import create_session
# from . import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
global_init(input())
session = create_session()
for user in session.query(User).filter((User.position.like("%chief%")) | (User.position.like("%middle%"))):
    print(user, user.position)

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
