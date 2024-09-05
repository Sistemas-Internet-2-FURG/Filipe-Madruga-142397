from flask import Blueprint, render_template

error = Blueprint('error', __name__, static_folder = 'static', template_folder = 'templates')

@error.app_errorhandler(404)
def notFound(error):
  return render_template('public/not_found.html'), 404

@error.app_errorhandler(500)
def internalServerError(error):
  return render_template('public/internal_server_error.html'), 500