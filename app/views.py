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
from app.helpers import generate_post_content


PAGE_CONTENT = generate_page_content()
POST_CONTENT = generate_post_content()


class Main(MethodView):

    def get(self):
        return render_template('index.html')


class Page(MethodView):

    def get(self, page):
        if page not in [i.get('path') for i in PAGE_CONTENT]:
            abort(404)
        for i in PAGE_CONTENT:
            if page == i.get('path'):
                return render_template('page.html', vars=i)


class Post(MethodView):

    def get(self, post):
        if post not in [i.get('path') for i in POST_CONTENT]:
            abort(404)
        for i in POST_CONTENT:
            if post == i.get('path'):
                return render_template('post.html', vars=i)


class Posts(MethodView):

    def get(self):
        return render_template(
            'posts.html',
            content=sorted(POST_CONTENT, key=lambda x: x.get('published'), reverse=True)
        )
