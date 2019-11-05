from flask import Blueprint
from app import app
from services.MoviesService import MoviesService
from flask import jsonify
from flask import flash, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

movies_api = Blueprint('movies_api', __name__)

movies_service = MoviesService()

@movies_api.route('/movie', methods=['POST'])
def add_movie():
    try:
        _json = request.json
        _name = _json['name']
        _description = _json['description']
        _stars = _json['stars']
        _year = _json['year']
        # validate the received values
        if _name and request.method == 'POST':
            lastrowid = movies_service.add_movie(_name,_description,_stars,_year)
            resp = jsonify({'id': lastrowid})
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)

@movies_api.route('/movie', methods=['GET'])
@jwt_required
def get_all_movies():
    try:
        page = request.args.get('page', default = 1, type = int)
        name = request.args.get('name', default = None, type = str)
        app.logger.info("page: " + str(page))
        
        pagesize = 2
        rows = movies_service.get_all_movies(page, pagesize, name)
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(page, name)

@movies_api.route('/rol/<int:id>', methods=['GET'])
@jwt_required
def get_movie_by_id(id):
    try:
        row = movies_service.get_movie_by_id(id)
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@movies_api.route('/rol/<int:id>', methods=['PUT'])
def update_rol(id):
    try:
        _json = request.json
        _name = _json['name']		
        # validate the received values
        if _name and id and request.method == 'PUT':
            rows_affected = movies_service.update_movie(id, _name)
            app.logger.info("PUT update_movie, rows_affected: " + str(rows_affected))
            if rows_affected == 0:
                resp = jsonify({'message': 'Movie was not updated!'})
                resp.status_code = 200
            else:
                resp = jsonify({'message': 'Movie updated successfully!'})
                resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)

@movies_api.route('/rol/<int:id>', methods=['DELETE'])
def delete_rol(id):
    try:
        rows_affected = movies_service.delete_rol(id)
        if rows_affected == 0:
            resp = jsonify({'message': 'Rol was not deleted!'})
            resp.status_code = 200
        else:
            resp = jsonify({'message': 'Rol deleted successfully!'})
            resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@movies_api.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp