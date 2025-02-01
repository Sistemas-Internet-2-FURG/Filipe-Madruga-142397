import datetime, os

CONFIG = {
  "flask": {
    "DEBUG": True,
    "SECRET_KEY": "LfGzP*fnf4GXF3rv$6Hd2BVhgMothj$b22Y8a$MQUjP*9Bn!xwOrBbffDC&PLzXFM^FUOTA6LTK&Fi6PbIXM9CAbRi@dqxQ$4Wh$JrCuGvyvxS8T5vg7M3*%DDfOwfG%",
    "SESSION_COOKIE_SECURE": os.getenv("FLASK_SESSION_COOKIE_SECURE"),
    "SESSION_COOKIE_NAME": "flask_session",
    "PERMANENT_SESSION_LIFETIME": datetime.timedelta(days = 1),
    "SESSION_REFRESH_EACH_REQUEST": False,
  }
}