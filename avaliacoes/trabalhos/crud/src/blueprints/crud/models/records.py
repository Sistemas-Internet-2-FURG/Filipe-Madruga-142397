from sqlite3 import IntegrityError
from models import base

class records(base):    
  def create_table(self):
    with self.connect() as conn:
      conn.execute("CREATE TABLE IF NOT EXISTS classes(classcode TEXT PRIMARY KEY, classname TEXT NOT NULL)")
      conn.execute("CREATE TABLE IF NOT EXISTS students(registration TEXT PRIMARY KEY, studentname TEXT NOT NULL)")
      conn.execute("""CREATE TABLE IF NOT EXISTS classes_students(class TEXT,
                                                                  registration TEXT, 
                                                                  PRIMARY KEY (class, registration),
                                                                  FOREIGN KEY (class) REFERENCES classes(classcode) ON DELETE CASCADE,
                                                                  FOREIGN KEY (registration) REFERENCES students(registration) ON DELETE CASCADE)""")
    
  def create_class(self, classcode, classname):
    with self.connect() as conn:
      try:
        conn.execute("INSERT INTO classes(classcode, classname) VALUES (?, ?)", (classcode.strip(), classname.strip()))
      except IntegrityError:
        return False
    return True
  
  def fetchall_classes(self):
    with self.connect() as conn:
      classes = conn.execute("SELECT * FROM classes")
    return classes.fetchall()
  
  def fetchone_class(self, classcode):
    with self.connect() as conn:
      classes = conn.execute("SELECT * FROM classes WHERE classcode == ?", (classcode.strip(),))
    return classes.fetchone()
  
  def remove_class(self, classcode):
    with self.connect() as conn:
      try:
        conn.execute("DELETE FROM classes WHERE classcode == ?", (classcode.strip(),))
      except IntegrityError:
        return False
    return True
  
  def classes_exists(self):
    if len(self.fetchall_classes()) == 0:
      return False
    return True
  
  def create_student(self, registration, studentname):
    with self.connect() as conn:
      try:
        conn.execute("INSERT INTO students(registration, studentname) VALUES (?, ?)", (registration.strip(), studentname.strip()))
      except IntegrityError:
        return False
    return True
  
  def fetchall_students(self):
    with self.connect() as conn:
      students = conn.execute("SELECT * FROM students")
    return students.fetchall()
  
  def fetchone_student(self, registration):
    with self.connect() as conn:
      students = conn.execute("SELECT * FROM students WHERE registration == ?", (registration.strip(),))
    return students.fetchone
  
  def remove_student(self, registration):
    with self.connect() as conn:
      try:
        conn.execute("DELETE FROM students WHERE registration == ?", (registration.strip(),))
      except IntegrityError:
        return False
    return True
  
  def create_classes_students(self, classcode, registration):
    with self.connect() as conn:
      try:
        conn.execute("INSERT INTO classes_students(class, registration) VALUES (?, ?)", (classcode.strip(), registration.strip()))
      except IntegrityError:
        return False
    return True
  
  def remove_classes_students(self, classcode, registration):
    with self.connect() as conn:
      try:
        conn.execute("DELETE FROM classes_students WHERE class == ? AND registration == ?", (classcode.strip(), registration.strip()))
      except IntegrityError:
        return False
    return True

  def fetchone_classes_students(self, classcode = None, registration = None):
    if classcode is not None:
      classcode = classcode.strip()
    if registration is not None:
      registration = registration.strip()
    with self.connect() as conn:
      classes_students = conn.execute("SELECT * FROM classes_students WHERE classcode == ? OR registration == ?", (classcode, registration))
    return classes_students.fetchone()
  
  def fetchall_classes_students(self):
    with self.connect() as conn:
      classes_students = conn.execute("SELECT * FROM classes_students")
    return classes_students.fetchall()