from flask import Blueprint, render_template

error = Blueprint('error', __name__, static_folder = 'static', template_folder = 'templates')

@error.app_errorhandler(404)
def notFound(error):
  return {"message:" "Not Found"}, 404

@error.app_errorhandler(500)
def internalServerError(error):
  return {"message:" "Internal Server Error"}, 500