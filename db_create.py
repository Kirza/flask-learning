from app import db
from models import BlogPost

# create the database and the db table
db.create_all()

# insert data
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))
db.session.add(BlogPost("Postgres", "Its alive"))
db.session.add(BlogPost("Postgres", "We setup a local postgres database"))

# commit the changes
db.session.commit()
