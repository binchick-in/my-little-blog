from flask import render_template


def general_error(err):
    return render_template('error.html', error_message=err)
