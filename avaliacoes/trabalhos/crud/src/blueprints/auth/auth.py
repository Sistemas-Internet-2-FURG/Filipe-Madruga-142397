from flask import Blueprint, session, g
from blueprints.auth.models import users
from .views import *

auth = Blueprint("auth", __name__, static_folder = "static", template_folder = "templates", url_prefix = "/auth")
auth.add_url_rule("/login", "login", login.as_view("login"))
auth.add_url_rule("/register", "register", register.as_view("register"))
auth.add_url_rule("/logout", "logout", logout.as_view("logout"))

@auth.before_app_request
def load_user():
  conn = users()
  conn.create_table()
  userid = session.get('userid')
  if userid is None:
   g.user = None
  else:
    g.user = conn.fetch_user(userid = userid)