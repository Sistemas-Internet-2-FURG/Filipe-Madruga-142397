from sqlite3 import IntegrityError
from models import base

class users(base):
  def __init__(self) -> None:
    super().__init__("users")
    
  def create_table(self):
    with self.connect() as conn:
      conn.execute("""CREATE TABLE IF NOT EXISTS users(userid TEXT,
                                                       username TEXT NOT NULL, 
                                                       useremail TEXT, 
                                                       userpassw TEXT NOT NULL,
                                                       PRIMARY KEY (userid, useremail))""")
    
  def create_user(self, userid, username, useremail, userpassw):
    with self.connect() as conn:
      try:
        conn.execute("INSERT INTO users(userid, username, useremail, userpassw) VALUES (?, ?, ?, ?)", (userid.strip(), username.strip(), useremail.strip(), userpassw.strip()))
      except IntegrityError:
        return False
    return True
  
  def fetch_userid(self, userid):
    with self.connect() as conn:
      user = conn.execute("SELECT * FROM users WHERE userid == ?", (userid.strip(),))
    return user.fetchone()
  
  def fetch_useremail(self, useremail):
    with self.connect() as conn:
      user = conn.execute("SELECT * FROM users WHERE useremail == ?", (useremail.strip(),))
    return user.fetchone()
  
  def remove_user(self, useremail):
    with self.connect() as conn:
      try:
        conn.execute("DELETE FROM users WHERE useremail == ?", (useremail.strip(),))
      except IntegrityError:
        return False
    return True
