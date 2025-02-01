from flask import config, render_template, request, session, url_for, flash, redirect
from flask.views import MethodView
from werkzeug.security import check_password_hash, generate_password_hash
from blueprints.auth.models import users
import uuid
import jwt
import datetime
from config import CONFIG

class login(MethodView):
  def post(self):
    auth_data = request.get_json()
    print(auth_data)
    error = None
    conn = users()
    user = conn.fetch_useremail(auth_data["useremail"])
    if user is None or not check_password_hash(user[3], auth_data["userpassw"]):
      error = "Incorrect E-mail or Password"
    if error is None:
      token = jwt.encode({"userid": user[0], "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours = 1)}, CONFIG["flask"]["SECRET_KEY"], algorithm = "HS256")
      return {"token": token}, 200
    return {"message": error}, 401
  
class register(MethodView):
  def post(self):
    auth_data = request.get_json()
    error = None
    conn = users()
    if not auth_data["username"]:
      error = "Username is required."
    elif not auth_data["userpassw"]:
      error = "Password is required."
    elif auth_data["userpassw"] != auth_data["userconfirmpassw"]:
      error = "Passwords do not match"
    elif auth_data["useremail"] != auth_data["userconfirmemail"]:
      error = "E-mail do not match"
    if error is None:
      userid = str(uuid.uuid4())
      conn.create_user(userid, auth_data["username"], auth_data["useremail"], generate_password_hash(auth_data["userpassw"]))
      return {"message": "Registered user"}, 200
    flash(error)
    return {"message": error}, 400
  
class logout(MethodView):
  def get(self):
    session.clear()
    return redirect(url_for("auth.login"))