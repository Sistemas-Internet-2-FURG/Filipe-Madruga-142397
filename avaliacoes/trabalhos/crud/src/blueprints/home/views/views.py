from flask import render_template
from flask.views import MethodView


class home_view(MethodView):
  def get(self):
    return render_template("public/home.html")