from flask import Flask, render_template, redirect, request, make_response, session, abort, Blueprint, jsonify
from data import db_session
from data.news import Jobs


blueprint = Blueprint('news_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs',  methods=['GET'])
def get_news():
    session = db_session.create_session()
    news = session.query(Jobs).all()
    return jsonify(
        {
            'news':
                [item.to_dict(only=('id', 'job', 'team_leader', 'work_size', 'collaborators',
              'start_date', 'end_date', 'is_finished', 'category'))
                 for item in news]
        }
    )