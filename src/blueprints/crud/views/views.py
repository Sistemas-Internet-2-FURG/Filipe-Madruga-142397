from flask import flash, redirect, render_template, url_for, request, g
from flask.views import MethodView
from blueprints.crud.models import records
from middleware import login_required


class crud_view(MethodView):
  decorators = [login_required]
  def get(self):
    user = g.user
    conn = records(user[0])
    students = conn.fetchall_students()
    classes = conn.fetchall_classes()
    classes_students = conn.fetchall_classes_students()
    return render_template("public/crud.html", students = students, classes = classes, classes_students = classes_students)
  
class register_student(MethodView):
  decorators = [login_required]
  def post(self):
    registration = request.form["registration"] or request.args.get("registration")
    studentname = request.form["studentname"] or request.args.get("studentname")
    classcode = request.form["classcode"] or request.args.get("classcode")
    error = None
    conn = records(g.user[0])
    if registration is None:
      error = "Registration is required"
    elif studentname is None:
      error = "Student is required"
    elif classcode is None:
      error = "The student must be in at least one class"
    elif not conn.classes_exists():
      error = "You need to register a class first"
    if error is None:
      conn.create_student(registration, studentname)
      for classes in classcode.split(";"):
        conn.create_classes_students(classes, registration)
      return redirect(url_for("crud.crud"))
    flash(error)
    return redirect(url_for("crud.crud"))
  
class register_class(MethodView):
  decorators = [login_required]
  def post(self):
    classcode = request.form["classcode"] or request.args.get("classcode")
    classname = request.form["classname"] or request.args.get("classname")
    error = None
    conn = records(g.user[0])
    if classcode is None:
      error = "Class Code is required"
    elif classname is None:
      error = "Class Name is required"
    if error is None:
      conn.create_class(classcode, classname)
      return redirect(url_for("crud.crud"))
    flash(error)
    return redirect(url_for("crud.crud"))
  
class remove_student(MethodView):
  decorators = [login_required]
  def post(self):
    registration = request.form["registration"] or request.args.get("registration")
    error = None
    conn = records(g.user[0])
    if registration is None:
      error = "Registration is required"
    if error is None:
      conn.remove_student(registration)
      return redirect(url_for("crud.crud"))
    flash(error)
    return redirect(url_for("crud.crud"))

class remove_class(MethodView):
  decorators = [login_required]
  def post(self):
    classcode = request.form["classcode"] or request.args.get("classcode")
    error = None
    conn = records(g.user[0])
    if classcode is None:
      error = "Class Code is required"
    if error is None:
      conn.remove_class(classcode)
      return redirect(url_for("crud.crud"))
    flash(error)
    return redirect(url_for("crud.crud"))
  
class update_student(MethodView):
  decorators = [login_required]
  def post(self):
    registration = request.form["registration"] or request.args.get("registration")
    classcode = request.form["classcode"] or request.args.get("classcode")
    action = request.form["action"] or request.args.get("action")
    error = None
    conn = records(g.user[0])
    if registration is None:
      error = "Registration is required"
    elif classcode is None:
      error = "Class Code is required"
    if error is None:
      match action:
        case "insert":
          for classes in classcode.split(";"):
            conn.create_classes_students(classes, registration)
        case "remove":
          for classes in classcode.split(";"):
            conn.remove_classes_students(classes, registration)
      return redirect(url_for("crud.crud"))
    flash(error)
    return redirect(url_for("crud.crud"))
  
class register_tables(MethodView):
  def get(self, userid):
    conn = records(userid)
    conn.create_table()
    return redirect(url_for("auth.login"))