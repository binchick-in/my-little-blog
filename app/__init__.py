from flask import Flask

from app.views import Main
from app.views import Page
from app.views import Post
from app.error_views import general_error


def create_app():
    app = Flask(__name__)
    app.add_url_rule('/', view_func=Main.as_view('home'))  # Home page of the blog
    app.add_url_rule('/<string:page>', view_func=Page.as_view('page'))  # Page route
    app.add_url_rule('/post/<string:post>', view_func=Post.as_view('post'))  
    app.register_error_handler(404, general_error)
    return app
