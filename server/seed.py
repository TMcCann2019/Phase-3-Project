from config import app
from models import db, Trainer, Pet, Training

if __name__ == "__main__":
  with app.app_context():
    Trainer.query.delete()
    Pet.query.delete()
    Training.query.delete()

    trainer_1 = Trainer(
      name="Pete",
      specialization="Owner and head trainer"
    )

    db.session.add(trainer_1)

    trainer_2 = Trainer(
      name="Kayla",
      specialization="Trainer and Groomer"
    )

    db.session.add(trainer_2)

    trainer_3 = Trainer(
      name="James",
      specialization="Trainer"
    )

    db.session.add(trainer_3)

    trainer_4 = Trainer(
      name="John",
      specialization="Groomer"
    )
  
    db.session.add(trainer_4)

    trainer_5 = Trainer(
      name="Anthony",
      specialization="Groomer"
    )

    db.session.add(trainer_5)

    trainer_6 = Trainer(
      name="Tim",
      specialization="Aggressive"
    )

    db.session.add(trainer_6)

    trainer_7 = Trainer(
      name="Jane",
      specialization="Muzzle"
    )

    db.session.add(trainer_7)
    db.session.commit()

    pet_1 = Pet(
      name = "Milo",
      species = "Pitbull",
      temperament = "Aggressive",
      muzzle = "Yes",
    )

    db.session.add(pet_1)

    pet_2 = Pet(
      name = "Rio",
      species = "Pitbull",
      temperament = "Friendly",
      muzzle = "No",
    )

    db.session.add(pet_2)

    pet_3 = Pet(
      name = "Bailey",
      species = "Heeler",
      temperament = "Hyper",
      muzzle = "No",
    )

    db.session.add(pet_3)

    pet_4 = Pet(
      name = "Ceasar",
      species = "Shepard",
      temperament = "Friendly",
      muzzle = "No",
    )

    db.session.add(pet_4)

    pet_5 = Pet(
      name = "Bruce",
      species = "Shepard",
      temperament = "Friendly",
      muzzle = "No",
    )

    db.session.add(pet_5)

    pet_6 = Pet(
      name = "Jelly Bean",
      species = "Poodle",
      temperament = "Reactive",
      muzzle = "Yes",
    )

    db.session.add(pet_6)

    pet_7 = Pet(
      name = "Shep",
      species = "Belgian Malinous",
      temperament = "Aggressive",
      muzzle = "No",
    )

    db.session.add(pet_7)
    db.session.commit()

    training_1 = Training(
      name = "In-Home Lesson",
      date = "02-14-24 09:00",
      trainer_id = trainer_1.id,
      pet_id = pet_1.id
    )

    db.session.add(training_1)

    training_2 = Training(
      name = "Facility Lesson",
      date = "02-14-24 12:00",
      trainer_id = trainer_5.id,
      pet_id = pet_2.id
    )

    db.session.add(training_2)

    training_3 = Training(
      name = "Nail Trim",
      date = "02-14-24 18:00",
      trainer_id = trainer_2.id,
      pet_id = pet_3.id
    )

    db.session.add(training_3)

    training_4 = Training(
      name = "Bath",
      date = "02-20-24 09:00",
      trainer_id = trainer_5.id,
      pet_id = pet_2.id
    )

    db.session.add(training_4)

    training_5 = Training(
      name = "In-Home Lesson",
      date = "02-25-24 09:00",
      trainer_id = trainer_6.id,
      pet_id = pet_3.id
    )

    db.session.add(training_5)

    training_6 = Training(
      name = "In-Home Lesson",
      date = "02-10-24 09:00",
      trainer_id = trainer_7.id,
      pet_id = pet_4.id
    )

    db.session.add(training_6)

    training_7 = Training(
      name = "In-Home Lesson",
      date = "03-14-24 09:00",
      trainer_id = trainer_4.id,
      pet_id = pet_5.id
    )

    db.session.add(training_7)
    db.session.commit()

    training_8 = Training(
      name = "Bath",
      date = "03-01-24 09:00",
      trainer_id = trainer_1.id,
      pet_id = pet_6.id
    )

    db.session.add(training_8)
    db.session.commit()