from flask import g, redirect, url_for
from functools import wraps

def login_required(func):
  @wraps(func)
  def authenticate(*args, **kwargs):
    if g.user is None:
      return redirect(url_for('auth.login'))
    return func(*args, **kwargs)
  return authenticate