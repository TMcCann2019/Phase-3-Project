from models import db, Pet, Trainer, Training

def get_all_trainers():
  return db.session.query(Trainer).all()

def get_all_pets():
  return db.session.query(Pet).all()

def get_all_trainings():
  return db.session.query(Training).all()

def find_trainer_by_id(id):
  return db.session.get(Trainer, id)

def find_pet_by_id(id):
  return db.session.get(Pet, id)