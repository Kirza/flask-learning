from project import db
from project.models import BlogPost, User

# create the database and the db table
db.create_all()

# insert data
db.session.add(User("webpage", "webpage@gmail.com", "letmein"))
db.session.add(User("superadmin", "no_email@ya.ru", "meininlet"))
db.session.add(User("testpage", "example@example.ru", "letmein"))

# insert data

# db.session.add(BlogPost("Good", "I\'m good."))
# db.session.add(BlogPost("Well", "I\'m well."))
# db.session.add(BlogPost("Postgres", "Its alive"))
# db.session.add(BlogPost("Postgres", "We setup a local postgres database"))


db.session.add(BlogPost("Grazd", "First step to answering nazi danger", "This is content # This is anouther line content # End of content $", "Politic", "1"))

# commit the changes
db.session.commit()
