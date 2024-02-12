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
      specialization="Aggressive dog training"
    )

    db.session.add(trainer_6)

    trainer_7 = Trainer(
      name="Jane",
      specialization="Muzzle conditioning"
    )

    db.session.add(trainer_7)
    db.session.commit()