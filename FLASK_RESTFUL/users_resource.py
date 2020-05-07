from flask import jsonify
from flask_restful import Resource, abort
from data import db_session
from data.jobs import Jobs
from data.reqparse_job import parser


def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(job_id)
    if not jobs:
        return jsonify({'error': 'invalidArgs'})


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(job_id)
        return jsonify({'jobs': jobs.to_dict(only=('job', 'work_size', 'collaborators', 'team_leader',
                                                   'category', 'is_finished'))})

    def delete(self, id):
        abort_if_job_not_found(id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(id)
        session.delete(jobs)
        session.commit()
        return jsonify({'error': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(only=('job', 'work_size', 'collaborators', 'team_leader',
                                                    'category', 'is_finished')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            team_leader=args['team_leader'],
            category=args['category'],
            is_finished=args['is_finished']
        )
        session.add(jobs)
        session.commit()
        return jsonify({'error': 'OK'})