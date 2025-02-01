from flask import g, redirect, url_for, request
from functools import wraps
from config import CONFIG
import jwt
from blueprints.auth.models import users

def login_required(func):
  @wraps(func)
  def authenticate(*args, **kwargs):
    try:
      token = request.headers.get('Authorization')
      user = jwt.decode(token, CONFIG["flask"]["SECRET_KEY"], algorithms = ["HS256"])
      conn = users()
      conn.create_table()
      if user is None:
        g.user = None
      else:
        g.user = conn.fetch_userid(user["userid"])
    except:
      return {"message": "Unauthorized"}, 401
    return func(*args, **kwargs)
  return authenticate