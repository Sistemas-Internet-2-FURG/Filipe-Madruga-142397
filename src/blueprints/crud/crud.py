from flask import Blueprint, views

from .views import *

crud = Blueprint("crud", __name__, static_folder = "static", template_folder = "templates", url_prefix = "/crud")
crud.add_url_rule("/", "index", alunos_view.as_view("index"))
crud.add_url_rule("/home", "home", turmas_view.as_view("index"))