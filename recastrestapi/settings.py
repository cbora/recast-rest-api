import recastdb.models
from recastdb.database import db

from eve_sqlalchemy.decorators import registerSchema

from eve.utils import config
from recastrestapi.apiconfig import config as apiconf


DEBUG = True

SQLALCHEMY_DATABASE_URI =  apiconf['DBPATH']
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
PUBLIC_ITEM_METHODS = ['GET', 'POST']
HATEOAS = True
IF_MATCH = False
LAST_UPDATED = '_updated'
DATE_CREATED = '_created'

ID_FIELD = 'id'
ITEM_LOOKUP_FIELD = ID_FIELD
config.ID_FIELD = ID_FIELD
config.ITEM_LOOKUP_FIELD = ID_FIELD

XML = False
JSON = True


from recastrestapi.apiconfig import config as apiconf

registerSchema('users')(recastdb.models.User)
registerSchema('analysis')(recastdb.models.Analysis)
registerSchema('subscriptions')(recastdb.models.Subscription)
registerSchema('run_conditions')(recastdb.models.RunCondition)
registerSchema('models')(recastdb.models.Model)
registerSchema('requests')(recastdb.models.ScanRequest)
registerSchema('point_requests')(recastdb.models.PointRequest)
registerSchema('basic_requests')(recastdb.models.BasicRequest)
registerSchema('parameters')(recastdb.models.Parameters)
registerSchema('parameter_points')(recastdb.models.ParameterPoint)
registerSchema('lhe_files')(recastdb.models.LHEFile)
registerSchema('responses')(recastdb.models.ScanResponse)
registerSchema('point_responses')(recastdb.models.PointResponse)
registerSchema('basic_responses')(recastdb.models.BasicResponse)
registerSchema('histograms')(recastdb.models.Histogram)
registerSchema('access_tokens')(recastdb.models.AccessToken)



DEBUG = True

SQLALCHEMY_DATABASE_URI =  apiconf['DBPATH']

XML = True
JSON = False

DOMAIN = {
        'users': recastdb.models.User._eve_schema['users'],
        'analysis': recastdb.models.Analysis._eve_schema['analysis'],
        'subscriptions': recastdb.models.Subscription._eve_schema['subscriptions'],
        'run_conditions': recastdb.models.RunCondition._eve_schema['run_conditions'],
        'models': recastdb.models.Model._eve_schema['models'],
        'requests': recastdb.models.ScanRequest._eve_schema['requests'],
        'point_requests': recastdb.models.PointRequest._eve_schema['point_requests'],
        'basic_requests': recastdb.models.BasicRequest._eve_schema['basic_requests'],
        'parameters': recastdb.models.Parameters._eve_schema['parameters'],
        'parameter_points': recastdb.models.ParameterPoint._eve_schema['parameter_points'],
        'lhe_files': recastdb.models.LHEFile._eve_schema['lhe_files'],
        'responses': recastdb.models.ScanResponse._eve_schema['responses'],
        'point_responses': recastdb.models.PointResponse._eve_schema['point_responses'],
        'basic_responses': recastdb.models.BasicResponse._eve_schema['basic_responses'],
        'histograms': recastdb.models.Histogram._eve_schema['histograms'],
        'access_tokens': recastdb.models.AccessToken._eve_schema['access_tokens'],
        }

DOMAIN['users'].update({
        'item_lookup_field': 'id',
        'additional_lookup': {
            'url': 'regex("[0-9]+")',
            'field': 'id'
            },
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'resource_methods': ['GET', 'POST', 'DELETE'],
        'item_methods': ['GET', 'PUT', 'PATCH']
        })

DOMAIN['analysis'].update({
        'item_lookup_field': 'id',
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'collaboration'
            },
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'resource_methods': ['GET', 'POST', 'DELETE']
        })

DOMAIN['run_conditions'].update({
        'item_lookup_field': 'id',
        'additional_lookup': {
            'url': 'regex("[0-9]+")',
            'field': 'id'
            },
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'resource_methods': ['GET', 'POST', 'DELETE'],
        'item_methods': ['GET', 'PUT', 'PATCH'],
        'resource_methods': ['GET', 'POST', 'DELETE']
        })
