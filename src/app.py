from flask import Flask

from blueprints import *


def main():
  app = Flask(__name__)
  app.register_blueprint(home_bp)
  
  app.run(host = "0.0.0.0")

if __name__ == "__main__":
  main()