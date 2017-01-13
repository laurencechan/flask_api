# coding=utf-8
from flask import Flask,blueprints
from back_stage.index import index_page
from api import my_api
import sys
reload(sys)
sys.setdefaultencoding("utf8")


app = Flask(__name__)


app.register_blueprint(index_page)
app.register_blueprint(my_api)


if __name__ == '__main__':
    app.run(debug=True)
