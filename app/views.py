import json
from flask import render_template
from flask import abort
from flask import request
from flask import session
from flask import make_response
from flask import jsonify
from flask.views import MethodView

from jinja2.exceptions import TemplateNotFound


class Main(MethodView):

    def get(self):
        return render_template('index.html')


class Page(MethodView):

    def get(self, page):
        the_page = f'{page}.html'
        try:
            return render_template(the_page)
        except TemplateNotFound:
            abort(404)


class Post(MethodView):

    def get(self, post):
        return f'You requested the {post} post'
