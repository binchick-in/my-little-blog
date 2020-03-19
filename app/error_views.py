from flask import render_template


def error_404(err):
    return render_template('error.html', error_message=err), 404


def error_500(err):
    return render_template('error.html', error_message=err), 500
