from config import db

class Trainer(db.Model):
    __tablename__ = "trainers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    specialization = db.Column(db.String(255))

class Pet(db.Model):
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    species = db.Column(db.String(255))
    temperament = db.Column(db.String(255))
    muzzle = db.Column(db.String(3))

class Training(db.Model):
    __tablename__ = "trainings"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date = db.Column(db.String(255))
    trainer_id = db.Column(db.Integer, db.ForeignKey("trainers.id"))
    trainer = db.relationship("Trainer", backref=db.backref("trainings", lazy="dynamic"))
    pet_id = db.Column(db.Integer, db.ForeignKey("pets.id"))
    pet = db.relationship("Pet", backref=db.backref("trainings", lazy="dynamic"))