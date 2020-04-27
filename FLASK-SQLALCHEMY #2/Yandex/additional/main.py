from flask import Flask, render_template, redirect
from temp.Tests_ex.web_10.tasks.no1_6.data import db_session
from temp.Tests_ex.web_10.tasks.no1_6.data.users import User
from temp.Tests_ex.web_10.tasks.no1_6.data.jobs import Jobs, Category
from temp.Tests_ex.web_10.tasks.no1_6.data.departments import Department
from temp.Tests_ex.web_10.tasks.no1_6.data.register import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    session = db_session.create_session()

    cat = Category()
    cat.job = "preventive vaccinations of the crew"
    job.team_leader = 7
    job.work_size = 7
    job.collaborators = "3"
    job.is_finished = True

    # department = Department()
    # department.title = "Department of construction"
    # department.chief = 6
    # department.email = "build@mars.org"
    # department.members = "16, 17, 28"

    # department = Department()
    # department.title = "Department of of construction"
    # department.chief = 6
    # department.email = "build@mars.org"
    # department.members = "9, 13, 18"

    # department = Department()
    # department.title = "Department of biological research"
    # department.chief = 3
    # department.email = "bio@mars.org"
    # department.members = "7, 10, 11"

    # department = Department()
    # department.title = "Department of geological exploration"
    # department.chief = 2
    # department.email = "geo@mars.org"
    # department.members = "6, 8, 12"

    session.add(job)
    session.commit()

    # app.run()


if __name__ == '__main__':
    main()
