import datetime, os

CONFIG = {
  "flask": {
    "DEBUG": os.getenv("FLASK_DEBUG"),
    "SECRET_KEY": os.getenv("FLASK_SECRET_KEY"),
    "SESSION_COOKIE_SECURE": os.getenv("FLASK_SESSION_COOKIE_SECURE"),
    "SESSION_COOKIE_NAME": "flask_session",
    "PERMANENT_SESSION_LIFETIME": datetime.timedelta(days = 1),
    "SESSION_REFRESH_EACH_REQUEST": False
  }
}