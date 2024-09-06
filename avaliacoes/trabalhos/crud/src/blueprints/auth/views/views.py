from flask import render_template, request, session, url_for, flash, redirect
from flask.views import MethodView
from werkzeug.security import check_password_hash, generate_password_hash
from blueprints.auth.models import users
import uuid

class login(MethodView):
  def get(self):
    return render_template("public/login.html")
  
  def post(self):
    useremail= request.form["useremail"] or request.args.get("useremail")
    userpassw = request.form["password"] or request.args.get("password")
    error = None
    conn = users()
    user = conn.fetch_user(useremail = useremail)
    if user is None or not check_password_hash(user[3], userpassw):
      error = "Incorrect E-mail or Password"
    if error is None:
      session.clear()
      session["userid"] = user[0]
      session.permanent = True
      return redirect(url_for("crud.crud"))
    flash(error)
    return redirect(url_for("auth.login"))
  
class register(MethodView):
  def get(self):
    return render_template("public/register.html")
  
  def post(self):
    username = request.form["username"] or request.args.get("username")
    useremail = request.form["useremail"] or request.args.get("useremail")
    userconfirmemail = request.form["userconfirmemail"] or request.args.get("userconfirmemail")
    userpassw = request.form["password"] or request.args.get("password")
    userconfirmpassw = request.form["confirm_password"] or request.args.get("confirm_password")
    error = None
    conn = users()
    if not username:
      error = "Username is required."
    elif not userpassw:
      error = "Password is required."
    elif userpassw != userconfirmpassw:
      error = "Passwords do not match"
    elif useremail != userconfirmemail:
      error = "E-mail do not match"
    if error is None:
      userid = str(uuid.uuid4())
      conn.create_user(userid, username, useremail, generate_password_hash(userpassw))
      return redirect(url_for("crud.register_tables", userid = userid))
    flash(error)
    return redirect(url_for("auth.register"))
  
class logout(MethodView):
  def get(self):
    session.clear()
    return redirect(url_for("auth.login"))