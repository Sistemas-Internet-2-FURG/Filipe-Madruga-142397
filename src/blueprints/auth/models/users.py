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
  
  def fetch_user(self, userid = None, useremail = None):
    if userid is not None:
      userid = userid.strip()
    if useremail is not None:
      useremail = useremail.strip()
    with self.connect() as conn:
      user = conn.execute("SELECT * FROM users WHERE userid == ? OR useremail == ?", (userid, useremail))
    return user.fetchone()
  
  def remove_user(self, useremail):
    with self.connect() as conn:
      try:
        conn.execute("DELETE FROM users WHERE useremail == ?", (useremail.strip(),))
      except IntegrityError:
        return False
    return True
