from flask import Blueprint, request, jsonify
from app import db

from app.mod_dictionary.service import DescriptionService


mod_dictionary = Blueprint('dictionary', __name__, url_prefix='/rae')


@mod_dictionary.route('/', methods=['GET', 'POST'])
def get_index():
    return "RAE Service API: /desc/word"


@mod_dictionary.route('/desc/<word>', methods=['GET', 'POST'])
def describe(word):
    description_service = DescriptionService()
    resp = jsonify(description_service.get_description(word))
    description_service.close_service()
    return resp

