from flask import Flask, render_template, redirect, request, make_response, session, abort, Blueprint, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,  BooleanField, SubmitField, TextAreaField,\
    SubmitField, ValidationError, TextField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
from data import db_session
from data.users import User
from data.news import News
import news_api
from flask_restful import reqparse, abort, Api, Resource
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import datetime
from data import news_resources


app = Flask(__name__)
api = Api(app)

api.add_resource(news_resources.NewsListResource, '/api/v2/news')

# для одного объекта
api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')