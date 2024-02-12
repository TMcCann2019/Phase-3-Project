from config import db

class Trainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    specialization = db.Column(db.String(255))

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    species = db.Column(db.String(255))
    temperament = db.Column(db.String(255))
    trainer_id = db.Column(db.Integer, db.ForeignKey("trainer.id"))
    trainer = db.relationship("Trainer", backref=db.backref("pets", lazy="dynamic"))

class Training(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trainer_id = db.Column(db.Integer, db.ForeignKey("trainer.id"))
    trainer = db.relationship("Trainer", backref=db.backref("trainings", lazy="dynamic"))
    pet_id = db.Column(db.Integer, db.ForeignKey("pet.id"))
    pet = db.relationship("Pet", backref=db.backref("trainings", lazy="dynamic"))