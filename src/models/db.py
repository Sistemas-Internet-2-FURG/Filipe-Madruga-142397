import pathlib
import sqlite3

class base:
  def __init__(self, db_name: str) -> None:
    self.__db_name = f"{db_name}.db"
  
  def __resolve_path(self):
    root = pathlib.Path(__file__)
    path = (root.parents[2]/"db").resolve()
    path.mkdir(exist_ok = True)
    return path
    
  def connect(self):
    conn = sqlite3.connect(self.__resolve_path()/self.__db_name)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn