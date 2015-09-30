from project import db
from project.models import BlogPost, User

# create the database and the db table
db.create_all()

# insert data
db.session.add(User("webpage", "webpage@gmail.com", "letmein"))
db.session.add(User("superadmin", "no_email@ya.ru", "meininlet"))
db.session.add(User("testpage", "example@example.ru", "letmein"))

# insert data

# db.session.add(BlogPost("Test header", "Test header long", "Test content lorepipsumX200", "Test tag", "111111", "http://ya.ru/123.png", "test author auto", "test author manual"))

# commit the changes
db.session.commit()
