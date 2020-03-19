from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class InboundRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_addr = db.Column(db.String(255))
    user_agent = db.Column(db.String(255))
    referer = db.Column(db.String(255))
    url_path = db.Column(db.String(255))
    request_args = db.Column(db.String(255))
    time_of_request = db.Column(db.DateTime, default=datetime.today())
