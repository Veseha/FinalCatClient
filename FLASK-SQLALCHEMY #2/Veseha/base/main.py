from flask import Flask, render_template, redirect, request, make_response, session, abort
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,  BooleanField, SubmitField, TextAreaField,\
    SubmitField, ValidationError, TextField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
from data import db_session
from data.users import User
from data.news import News
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/blogs.sqlite")
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)

login_manager = LoginManager()
login_manager.init_app(app)


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    about = TextAreaField("Немного о себе")
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField("Содержание")
    is_private = BooleanField("Личное")
    submit = SubmitField('Применить')


def main():
    # # ---------------------- тестирование системы --------------------
    # # ----------- добавление пользователя -------------
    # # user = User()
    # # user.name = "Пользов3атель 2"
    # # user.about = "биография пользователя 3"
    # # user.email = "ema2i4l@email.ru"
    #
    # # --------- создание сесии ------------------------
    # session = db_session.create_session()
    # # session.add(user) # ------- добавление инфы
    # session.commit()
    #
    # # --------- вывод инфы ----------------------------
    # print('------------- запрос инфы об об определенном параметре')
    # user = session.query(User).first()
    # print(user.name)
    #
    # print('------------- вывод всего и вся')
    # for user in session.query(User).all():
    #     print(user)
    #
    # print('------------- фильтр с операцией AND')
    # for user in session.query(User).filter(User.id > 1, User.email.notilike("%1%")):
    #     print(user)
    #
    # print('------------- фильтр с операцией OR')
    # for user in session.query(User).filter((User.id > 1) | (User.email.notilike("%1%"))):
    #     print(user)
    #
    # print('--------- изменение инфы')
    # user = session.query(User).filter(User.id == 1).first()
    # print(user)
    # user.name = "Измененное имя пользователя"
    # user.created_date = datetime.datetime.now()
    # session.commit()
    #
    # print('---------- удаление инфы по фильтру')
    # session.query(User).filter(User.id >= 999).delete()
    # session.commit()
    #
    # print('---------- удаление инфы определенного элемента')
    # # user = session.query(User).filter(User.id == 2).first()
    # # session.delete(user)
    # # session.commit()
    #
    # print(" ---------- Добавление записи юзеру")
    # news = News(title="Первая новость", content="Привет блог!",
    #             user_id=1, is_private=False)
    # # session.add(news)
    # session.commit()
    #
    # print('----------- Добавление записи вот так')
    # user = session.query(User).filter(User.id == 1).first()
    # news = News(title="Вторая новость", content="Уже вторая запись!",
    #             user=user, is_private=False)
    # # session.add(news)
    # session.commit()
    #
    # print('----------- посмотри код, здесь один из лучших спопосбов добавления записи')
    # user = session.query(User).filter(User.id == 1).first()
    # news = News(title="Личная запись", content="Эта запись личная",
    #             is_private=True)
    # # user.news.append(news)
    # session.commit()
    #
    # print('----------- тупо все новости юзера')
    # for news in user.news:
    #     print(news)      # ---------- надо бы добавить __repr__
    #
    # # ------------ запуск приложения
    app.run(port=8080, host='127.0.0.1')


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/news',  methods=['GET', 'POST'])
@login_required
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        news = News()
        news.title = form.title.data
        news.content = form.content.data
        news.is_private = form.is_private.data
        current_user.news.append(news)
        session.merge(current_user)
        session.commit()
        return redirect('/')
    return render_template('news.html', title='Добавление новости',
                           form=form)


@app.route('/news/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = NewsForm()
    print(current_user)
    if request.method == "GET":
        session = db_session.create_session()
        news = session.query(News).filter(News.id == id,
                                          News.user == current_user).first()
        print(news.title)
        if news:
            form.title.data = news.title
            form.content.data = news.content
            form.is_private.data = news.is_private
            print(form.title)
        else:
            abort(404)
    if form.validate_on_submit():
        session = db_session.create_session()
        news = session.query(News).filter(News.id == id,
                                          News.user == current_user).first()
        if news:
            news.title = form.title.data
            news.content = form.content.data
            news.is_private = form.is_private.data
            session.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('news.html', title='Редактирование новости', form=form)


@app.route('/news_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    session = db_session.create_session()
    news = session.query(News).filter(News.id == id,
                                      News.user == current_user).first()
    if news:
        session.delete(news)
        session.commit()
    else:
        abort(404)
    return redirect('/')


@app.route("/cookie_test")
def cookie_test():
    visits_count = int(request.cookies.get("visits_count", 0))
    if visits_count:
        res = make_response(f"Вы пришли на эту страницу {visits_count + 1} раз")
        res.set_cookie("visits_count", str(visits_count + 1),
                       max_age=20)
    else:
        res = make_response(
            "Вы пришли на эту страницу в первый раз за последние 2 года")
        res.set_cookie("visits_count", '1',
                       max_age=20)
    return res


@app.route('/session_test/')
def session_test():
    if 'visits_count' in session:
        session['visits_count'] = session.get('visits_count') + 1
    else:
        session['visits_count'] = 1
    return make_response(f'kolvo {session["visits_count"]}')
    # дальше - код для вывода страницы


@app.route("/")
def index():
    session = db_session.create_session()
    if current_user.is_authenticated:
        news = session.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
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