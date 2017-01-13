# coding=utf-8

__author__ = 'laurencechan'
__doc__ = 'one'

from flask_restplus import Namespace, fields, Resource, marshal
from tool.conn import mongo_conn
from flask import request
import json
from bson import ObjectId
from werkzeug.datastructures import FileStorage

db = mongo_conn()

TheOne = Namespace('TheOne', description='他强任他强', default_mediatype='text/html')

todo = TheOne.model('xxx', {
    'id': fields.String(readOnly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details'),
    "nba": fields.String(required=True, descripttion='nbaallstar')
})


@TheOne.route('/one')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''

    # @TheOne.doc('list_todos')
    @TheOne.marshal_with(todo)
    def get(self):
        """List all tasks"""
        todo = dict(id=675912623, task='pythoncoding', nba='stephencurry')
        return todo


user_update_parser = TheOne.parser()
# user_update_parser = reqparse.RequestParser()
user_update_parser.add_argument('name', type=str, required=True, help='username', location='form')
user_update_parser.add_argument('password', type=str, required=True, help='password', location='form')

insertdb = TheOne.model('insertdb11', {
    'name': fields.String(required=True, description='用户名', example="rhewitt"),
    'password': fields.String(required=True, description='密码', example="123456"),
    'test': fields.String(description='我只是一个测试的', default='测试测试')
})


@TheOne.route('/two')
@TheOne.response(201, '操作成功')
@TheOne.response(406, '验证失败')
# @TheOne.expect(user_update_parser)
class InsertDb(Resource):
    @TheOne.doc('添加用户', parser=user_update_parser)
    @TheOne.marshal_with(insertdb, code=201)
    def post(self):
        """
        添加用户

        """
        data = json.loads(json.dumps(request.form))
        db.the_one.insert_one(data)
        print data
        return data


query11 = TheOne.parser()
# query11.add_argument("ObjectId", type=str, help="objectid", location="args")

query_model = TheOne.model("stest", {
    "name": fields.String(required=True, description="用户名", example="Rhewitt"),
    "password": fields.String(required=True, description="密码", example="123456"),
    "ObjectId": fields.String(required=True, description="OJID", example="58730bc420c01135f8aa177b")
})


@TheOne.route('/Three/<id>')
@TheOne.param("id", "OBJECTID", default="")
@TheOne.response(201, '查询成功')
@TheOne.response(406, '查询失败')
class Theree(Resource):
    @TheOne.marshal_with(query_model, 201)
    def get(self,id):
        data = json.loads(json.dumps(request.args))
        print data
        result = db.find_one({"_id": ObjectId(data)})
        return result


if __name__ == '__main__':
    pass
