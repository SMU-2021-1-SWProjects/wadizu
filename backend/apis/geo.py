from typing_extensions import Required
from flask_restx import Namespace, Resource, fields

api = Namespace('trajectory', description='Trajectory related operations')

trajectory = api.model('Trajectory', {
    'latitude': fields.String(Required=True),
    'longtitude': fields.String(Required=True),
    'zero': fields.String(Required=False),
    'altitude': fields.String(Required=False),
    'timestamp': fields.String(Required=True),
    'date': fields.String(Required=False),
    'time': fields.String(Required=False),
})

TRAJECTORY = []

@api.route('/')
class GeoList(Resource):
    @api.doc('list trajectory')
    @api.marshal_list_with(trajectory)
    def get(self):
        return TRAJECTORY