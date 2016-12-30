import datetime

from flask.ext.restful import Api
from flask.ext.restful import Resource
from flask.ext.restful import reqparse

from app import app
from app import get_db


api = Api(app)


class FeedingAdd(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('time', type=str, location='json', required=False, help='Time of the feeding')
        self.reqparse.add_argument('side', type=str, location='json', required=True, help='Left or right')
        super(FeedingAdd, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        doc = {}
        for k, v in args.items():
            if k == 'side' and v not in ['left', 'right']:
                abort(400)
            doc[k] = v
        if not doc['time']:
            d = datetime.datetime.now() - datetime.timedelta(hours=4)
            doc['time'] = d.strftime('%Y-%m-%d %H:%M')
        db = get_db()
        db.feedings.insert(doc)
        return {'info': 'added'}
    

class DiaperAdd(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('time', type=str, location='json', required=False, help='Time of the diaper change')
        self.reqparse.add_argument('type', type=str, location='json', required=True, help='Wet or stinky')
        super(DiaperAdd, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        doc = {}
        for k, v in args.items():
            if k == 'type' and v not in ['wet', 'stinky']:
                abort(400)
            doc[k] = v
        if not doc['time']:
            d = datetime.datetime.now() - datetime.timedelta(hours=4)
            doc['time'] = d.strftime('%Y-%m-%d %H:%M')
        db = get_db()
        db.bathroom.insert(doc)
        return {'info': 'added'}

# TODO: add methods for updating, deleting, getting all, getting one


api.add_resource(FeedingAdd, '/api/feeding/add', endpoint='feeding_add')
api.add_resource(DiaperAdd, '/api/diaper/add', endpoint='diaper_add')
