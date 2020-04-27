import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase

association_table = sqlalchemy.Table('association', SqlAlchemyBase.metadata,
                                     sqlalchemy.Column('jobs', sqlalchemy.Integer, sqlalchemy.ForeignKey('jobs.id')),
                                     sqlalchemy.Column('category', sqlalchemy.Integer,
                                                       sqlalchemy.ForeignKey('category.id'))
                                     )


class Category(SqlAlchemyBase):
    __tablename__ = 'category'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    # team_leader = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    category = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("categories.id"))

    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')
    categories = orm.relation("Category",
                              secondary="association",
                              backref="jobs")

    def __repr__(self):
        return f'<Job> {self.job}'
