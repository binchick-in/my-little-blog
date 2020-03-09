import json
from flask import render_template
from flask import abort
from flask import request
from flask import session
from flask import make_response
from flask import jsonify
from flask.views import MethodView

from jinja2.exceptions import TemplateNotFound
from app.helpers import generate_page_content


PAGE_CONTENT = generate_page_content()


class Main(MethodView):

    def get(self):
        return render_template('index.html')


class Page(MethodView):

    def get(self, page):
        page_object = PAGE_CONTENT.get(page)
        if not page_object:
            abort(404)
        return render_template('page.html', vars=page_object)


class Post(MethodView):

    def get(self, post):
        return f'You requested the {post} post'
