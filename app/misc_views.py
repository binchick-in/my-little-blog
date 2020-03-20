from flask import jsonify
from flask import render_template

from app.models import InboundRequest
from app.models import db


def error_404(err):
    return render_template('error.html', error_message=err), 404


def error_500(err):
    return render_template('error.html', error_message=err), 500


def health():
    try:
        db.session.query(InboundRequest).count()
        return jsonify({'status': 'ok'})
    except Exception as e:
        print(e)
        return jsonify({'status': 'not ok'}), 500
