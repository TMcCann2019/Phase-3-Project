from models import db, Pet, Trainer, Training
from pick import pick

def get_all_trainers():
    return db.session.query(Trainer).all()

def get_all_pets():
    return db.session.query(Pet).all()

def find_trainer_by_id(id):
    return db.session.get(Trainer, id)
    
def find_pet_by_id(id):
    return db.session.get(Pet, id)

def display_add_training_to_pet_submenu(pet):
    trainer_names = [trainer.name for trainer in db.session.query(Trainer).all()]
    title = "Which trainer do you want for this training?"
    trainer_name, index = pick(trainer_names, title)
    trainer = db.session.query(Trainer).filter(Trainer.name == trainer_name).first()
    req_type = "What type of training do you want?"
    request_choice, index = pick(["In-Home Lesson", "Facility Lesson", "Nail Trim", "Bath"], req_type)
    training = Training(
    request = request_choice,
    trainer_id = trainer.id,
    pet_id = pet.id
    )
    db.session.add(training)
    db.session.commit()

def add_new_pet():
    print("Enter the information for your pet here:")
    name = input("Name: ")
    species = input("Species: ")
    temperament = input("Temperament: ")
    muzzle = input("Muzzle: ")

    new_pet = Pet(
        name = name,
        species = species,
        temperament = temperament,
        muzzle = muzzle
    )

    db.session.add(new_pet)
    db.session.commit()

def add_new_trainer():
    print("Enter the information for your trainer here:")
    name = input("Name: ")
    specialization = input("Specialization: ")

    new_trainer = Trainer(
        name = name,
        specialization = specialization
    )

    db.session.add(new_trainer)
    db.session.commit()