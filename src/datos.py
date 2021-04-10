from models import GenderCat

me = GenderCat('Prueba 1')
db.session.add(me)
db.session.commit()