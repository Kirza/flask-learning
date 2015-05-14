from app import db
from models import User

# insert data
db.session.add(User("showmewebpage", "kirzaru@gmail.com", "plz1let2me3in4"))
db.session.add(User("guest_invite", "no_email@ya.ru", "guestpassword"))

# commit the changes
db.session.commit()
