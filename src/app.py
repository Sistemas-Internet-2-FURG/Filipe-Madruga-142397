from flask import Flask

import blueprints as bp
from config import CONFIG

def main():
  app = Flask(__name__)
  app.config.update(**CONFIG["flask"])
  app.register_blueprint(bp.home)
  app.register_blueprint(bp.crud)
  app.run(host = "0.0.0.0")

if __name__ == "__main__":
  main()