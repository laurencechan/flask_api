# coding=utf-8
__author__ = 'laurencechan'
__doc__ = '测试接口'

from flask import Blueprint
from flask_restplus import Api
from the_one import TheOne

my_api = Blueprint('InterFace', __name__, url_prefix='/api')

one_api = Api(app=my_api, version='1.0')

one_api.add_namespace(TheOne)
