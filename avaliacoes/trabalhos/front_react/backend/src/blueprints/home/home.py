from flask import Blueprint
from .views import *

home = Blueprint("home", __name__, static_folder = "static", template_folder = "templates", url_prefix = "/")
home.add_url_rule("/", "index", home_view.as_view("index"))
home.add_url_rule("/home", "home", home_view.as_view("home"))