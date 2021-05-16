from flask_restx import Api

from . import geo

api = Api(
    title='wadizu api',
    version='1.0',
    description='wadizu api with geo data'
)

api.add_namespace(geo.api, path='/api/geo')