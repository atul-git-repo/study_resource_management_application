from flask_restful import Resource, Api, reqparse, marshal_with, fields
from .models import StudyResource, db

api = Api(prefix='/api')

parser = reqparse.RequestParser()
parser.add_argument('topic', type=str, help = 'topic is required and should be a string data type', required = True)
parser.add_argument('description', type=str, help = 'description is required and should be a string data type', required = True)
parser.add_argument('resource_link', type=str, help = 'resource_link is required and should be a string data type', required = True)

study_material_fields = {
    'id': fields.Integer,
    'topic': fields.String,
    'description': fields.String,
    'resource_link': fields.String
}


class StudyMaterial(Resource):
    @marshal_with(study_material_fields)
    def get(self):
        all_study_material = StudyResource.query.all()
        return all_study_material
    
    def post(self):
        args = parser.parse_args()
        study_resource = StudyResource(**args)
        db.session.add(study_resource)
        db.session.commit()
        return {"message": " Resource added successfully."}


api.add_resource(StudyMaterial, '/study_material')