from flask import Blueprint
from .views import *

crud = Blueprint("crud", __name__, static_folder = "static", template_folder = "templates", url_prefix = "/crud")
crud.add_url_rule("/", "crud", crud_view.as_view("crud"))
crud.add_url_rule("/register/tables/<string:userid>", "register_tables", register_tables.as_view("register_tables"))
crud.add_url_rule("/register/student", "register_student", register_student.as_view("register_student"))
crud.add_url_rule("/register/class", "register_class", register_class.as_view("register_class"))
crud.add_url_rule("/remove/student", "remove_student", remove_student.as_view("remove_student"))
crud.add_url_rule("/remove/class", "remove_class", remove_class.as_view("remove_class"))
crud.add_url_rule("/update/student", "update_student", update_student.as_view("update_student"))