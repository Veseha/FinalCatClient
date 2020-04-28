from flask import Flask, render_template, redirect, request, make_response, session, abort, Blueprint, jsonify
from data import db_session
from data.news import Jobs


blueprint = Blueprint('news_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs', methods=['POST'])
def create_news():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['title', 'content', 'user_id', 'is_private']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    news = Jobs(
        job=request.json['job'],
        team_leader=request.json['team_leader'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        start_date=request.json['start_date'],
        end_date=request.json['end_date'],
        is_finished=request.json['is_finished'],
        category=request.json['category'],

    )
    session.add(news)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>',  methods=['GET'])
def get_one_news(jobs_id):
    session = db_session.create_session()
    news = session.query(Jobs).get(jobs_id)
    if not news:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'news': news.to_dict(only=('id', 'job', 'team_leader', 'work_size', 'collaborators',
                                       'start_date', 'end_date', 'is_finished', 'category'))
        }
    )


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