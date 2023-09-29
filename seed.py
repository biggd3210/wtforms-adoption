from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

pet1 = Pet(name="Cheeseball",
           species="cat",
           age=5,
           notes="Very lovely and cuddly however when ignored, he can become disruptive",
           photo_url="https://res.cloudinary.com/petrescue/image/upload/b_auto:predominant,f_auto,c_pad,h_638,w_638/v1659773078/hlt3fmksmg5v9l93bjll.jpg",
           available=False)

pet2 = Pet(name="Minverva",
           species="cat",
           age=4,
           photo_url="https://media-cldnry.s-nbcnews.com/image/upload/rockcms/2022-07/220726-cat-theo-elise-ew-636p-6cd3b0.jpg",
           notes="Shy but sweet and gentle",
           available=False)

pet3 = Pet(name="Gordo",
           species="dog",
           age=2)

pet4 = Pet(name="Crico",
           species="Hedgehog",
           photo_url="https://gregrichdvm.com/wp-content/uploads/2022/09/hedgehog.jpg",
           age=8)

db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)
db.session.add(pet4)

db.session.commit()