from flask import Flask

from app.views import Main
from app.views import Page
from app.views import Post
from app.views import Posts
from app.error_views import general_error
from app.helpers import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database/cache.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.add_url_rule('/', view_func=Main.as_view('home'))
    app.add_url_rule('/<string:page>', view_func=Page.as_view('page'))
    app.add_url_rule('/post/<string:post>', view_func=Post.as_view('post'))  
    app.add_url_rule('/posts', view_func=Posts.as_view('posts'))
    app.register_error_handler(404, general_error)
    app.register_error_handler(500, general_error)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    return app

