from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user

from data import db_session
from data.add_job import AddJobForm
from data.login_form import LoginForm
from data.users import User
from data.jobs import Jobs
from data.register import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/mars_explorer.sqlite")

    @login_manager.user_loader
    def load_user(user_id):
        session = db_session.create_session()
        return session.query(User).get(user_id)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            session = db_session.create_session()
            user = session.query(User).filter(User.email == form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect("/")
            return render_template('login.html', message="Wrong login or password", form=form)
        return render_template('login.html', title='Authorization', form=form)

    @app.route("/")
    def index():
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        users = session.query(User).all()
        names = {name.id: (name.surname, name.name) for name in users}
        return render_template("index.html", jobs=jobs, names=names, title='Work log')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect("/")

    @app.route('/register', methods=['GET', 'POST'])
    def reqister():
        form = RegisterForm()
        if form.validate_on_submit():
            if form.password.data != form.password_again.data:
                return render_template('register.html', title='Register', form=form,
                                       message="Passwords don't match")
            session = db_session.create_session()
            if session.query(User).filter(User.email == form.email.data).first():
                return render_template('register.html', title='Register', form=form,
                                       message="This user already exists")
            user = User(
                name=form.name.data,
                surname=form.surname.data,
                age=form.age.data,
                position=form.position.data,
                email=form.email.data,
                speciality=form.speciality.data,
                address=form.address.data
            )
            user.set_password(form.password.data)
            session.add(user)
            session.commit()
            return redirect('/login')
        return render_template('register.html', title='Регистрация', form=form)

    @app.route('/addjob', methods=['GET', 'POST'])
    def addjob():
        print()
        add_form = AddJobForm()
        if add_form.validate_on_submit():
            session = db_session.create_session()
            jobs = Jobs(
                job=add_form.job.data,
                team_leader=add_form.team_leader.data,
                work_size=add_form.work_size.data,
                collaborators=add_form.collaborators.data,
                is_finished=add_form.is_finished.data
            )
            session.add(jobs)
            session.commit()
            return redirect('/')
        return render_template('addjob.html', title='Adding a job', form=add_form)

    app.run()


if __name__ == '__main__':
    main()