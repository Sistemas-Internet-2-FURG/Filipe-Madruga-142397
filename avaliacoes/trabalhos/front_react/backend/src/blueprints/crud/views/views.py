from flask import flash, redirect, render_template, url_for, request, g
from flask.views import MethodView
from blueprints.crud.models import records
from middleware import login_required


class crud_view(MethodView):
  decorators = [login_required]
  def get(self):
    user = g.user
    conn = records(user[0])
    conn.create_table()
    students = conn.fetchall_students()
    classes = conn.fetchall_classes()
    classes_students = conn.fetchall_classes_students()
    print({"students": students, "classes": classes, "classes_students": classes_students})
    return {"students": students, "classes": classes, "classes_students": classes_students}, 200
  
class register_student(MethodView):
  decorators = [login_required]
  def post(self):
    data = request.get_json()
    error = None
    conn = records(g.user[0])
    if data["registration"] is None:
      error = "Registration is required"
    elif data["studentname"] is None:
      error = "Student is required"
    elif data["classcode"] is None:
      error = "The student must be in at least one class"
    elif not conn.classes_exists():
      error = "You need to register a class first"
    if error is None:
      conn.create_student(data["registration"], data["studentname"])
      for classes in data["classcode"].split(";"):
        conn.create_classes_students(classes, data["registration"])
      return {"message": "Ok"}, 200
    return {"message": error}, 401
  
class register_class(MethodView):
  decorators = [login_required]
  def post(self):
    data = request.get_json()
    error = None
    conn = records(g.user[0])
    if data["classcode"] is None:
      error = "Class Code is required"
    elif data["classname"] is None:
      error = "Class Name is required"
    if error is None:
      conn.create_class(data["classcode"], data["classname"])
      return {"message": "Ok"}, 200
    return {"message": error}, 401
  
class remove_student(MethodView):
  decorators = [login_required]
  def post(self):
    data = request.get_json()
    error = None
    conn = records(g.user[0])
    if data["registration"] is None:
      error = "Registration is required"
    if error is None:
      conn.remove_student(data["registration"])
      return {"message": "Ok"}, 200
    return {"message": error}, 401

class remove_class(MethodView):
  decorators = [login_required]
  def post(self):
    data = request.get_json()
    error = None
    conn = records(g.user[0])
    if data["classcode"] is None:
      error = "Class Code is required"
    if error is None:
      conn.remove_class(data["classcode"])
      return {"message": "Ok"}, 200
    return {"message": error}, 401
  
class update_student(MethodView):
  decorators = [login_required]
  def post(self):
    data = request.get_json()
    error = None
    conn = records(g.user[0])
    if data["registration"] is None:
      error = "Registration is required"
    elif data["classcode"] is None:
      error = "Class Code is required"
    if error is None:
      match data["action"]:
        case "insert":
          for classes in data["classcode"].split(";"):
            conn.create_classes_students(classes, data["registration"])
        case "remove":
          for classes in data["classcode"].split(";"):
            conn.remove_classes_students(classes, data["registration"])
      return {"message": "Ok"}, 200
    return {"message": error}, 401