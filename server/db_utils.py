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
    date_choice = input("When would you like to do this training?(Please use MM-DD-YY format and time in HH:MM format): ")
    training = Training(
        name = request_choice,
        date = date_choice,
        trainer_id = trainer.id,
        pet_id = pet.id
    )
    db.session.add(training)
    db.session.commit()

def add_new_pet():
    print("Enter the information for your pet here:")
    name = input("Name: ").capitalize()
    species = input("What species are they?: ").capitalize()
    temperament = input("What kind of temperament do they have(ex. aggressive, happy, friendly)?: ").capitalize()
    muzzle = input("Do they need a Muzzle (Yes or No only)?: ").capitalize()

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
    name = input("Name: ").capitalize()
    specialization = input("What do they specialize in (ex. Grooming, Muzzle, Trainer, Agressive)?: ").capitalize()

    new_trainer = Trainer(
        name = name,
        specialization = specialization
    )

    db.session.add(new_trainer)
    db.session.commit()

def search_trainer_by():
    pass

def search_pet_by_species():
    print("What species are you looking for?")
    species = input("Species: ").capitalize()
    pets = db.session.query(Pet).filter(Pet.species == species).all()
    if len(pets) > 0:
        for pet in pets:
            print(f"{pet.id} | {pet.name} | {pet.species}")
    else:
        print("No pets found with that species")
        search_pet_by_species()

def search_pet_by_temperament():
    print("What temperament are you looking for?")
    temperament = input("Temperament: ").capitalize()
    pets = db.session.query(Pet).filter(Pet.temperament == temperament).all()
    if len(pets) > 0:
        for pet in pets:
            print(f"{pet.id} | {pet.name} | {pet.temperament}")
    else:
        print("No pets found with that temperament")
        search_pet_by_temperament()

def search_pet_by_muzzle():
    print("Are you looking for dogs that need a muzzle or no?")
    muzzle = input("Muzzle(Yes or No): ").capitalize()
    pets = db.session.query(Pet).filter(Pet.muzzle == muzzle).all()
    if len(pets) > 0:
        for pet in pets:
            print(f"{pet.id} | {pet.name} | {pet.muzzle}")
    else:
        print("No pets found")
        search_pet_by_muzzle()