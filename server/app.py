from config import app, migrate
from rich import print
from models import db, Training
from db_utils import get_all_pets, get_all_trainers, find_trainer_by_id, find_pet_by_id, display_add_training_to_pet_submenu, add_new_pet, add_new_trainer

def display_welcome():
  print("[cyan]Welcome to Fido Training and Grooming[/cyan]")
    
def display_main_menu():
  print("[magenta]Main Menu[/magenta]")
  print("1. Show all Trainers")
  print("2. Add a new Trainer")
  print("3. Show all Pets")
  print("4. Add a new Pet")
  print("5. Exit")

def get_main_menu_choice():
  return input("Which one would you like to do? ")

def display_all_trainers():
  trainers = get_all_trainers()
  for trainer in trainers:
    print(f"{trainer.id} | {trainer.name} | {trainer.specialization}")
  print("What do you want to do now?")
  print("1. See more about the trainer")
  print("2. Remove a Trainer")
  print("3. Exit")
  choice = input()
  if choice == "1":
    choose_trainer_by_id()
  elif choice == "2":
    remove_trainer_by_id()
  elif choice == "3":
    return
  else:
    print("Invalid input. Please choose a number above")
    display_all_trainers()

def remove_trainer_by_id():
  search_id = input("Enter the id of the trainer you would like to remove: ")
  trainer = find_trainer_by_id(search_id)
  if trainer is None:
    print("Trainer not found")
    remove_trainer_by_id()
  else:
    db.session.delete(trainer)
    db.session.commit()
    display_all_trainers()

def choose_trainer_by_id():
  search_id = input("Enter the id of the trainer: ")
  trainer = find_trainer_by_id(search_id)
  if trainer is not None:
    print(
      f"Id: {trainer.id}, Name: {trainer.name}, Specialization: {trainer.specialization}"
    )
  else:
    print("Trainer not found")
    choose_trainer_by_id()
  display_trainer_submenu(trainer)

def display_trainer_submenu(trainer):
  print("1. See a trainers trainings")
  print("2. Update a training")
  print("3. Exit")
  choice = input()
  handle_trainer_choice(choice, trainer)

def handle_trainer_choice(choice, trainer):
  if choice == "1":
    show_trainer_trainings(trainer)
  elif choice == "2":
    update_trainings(trainer)
  elif choice == "3":
    return
  else:
    print("Invalid input.")
    display_trainer_submenu(trainer)

def show_trainer_trainings(trainer):
  trainings = trainer.trainings
  for training in trainings:
    print(f"{training.id} | {training.name}")

def update_trainings(trainer):
  print("Update Training Information:")
  trainings = trainer.trainings
  if not trainings:
    print("No trainings to update")
    return
  print("Current Trainings:")
  for training in trainings:
    print(f"{training.id} | {training.name}")
  training_id = input("Enter the ID of the training to update: ")
  training = Training.query.get(training_id)
  if not training:
    print("Training not found")
    update_trainings(trainer)
  new_name = input(f"New Name ({training.name}): ")
  training.name = new_name
  db.session.commit()

def display_all_pets():
  pets = get_all_pets()
  for pet in pets:
    print(f"{pet.id} | {pet.name} | {pet.species}")
  print("What do you want to do now?")
  print("1. See more about the pets")
  print("2. Remove a pet")
  print("3. Add a new training")
  print("4. Exit")
  choice = input()
  if choice == "1":
    choose_pet_by_id()
  elif choice == "2":
    remove_pet_by_id()
  elif choice == "3":
    add_new_training_to_pet_by_id()
  elif choice == "4":
    return
  else:
    print("Unknown choice. Pleae choose a number between 1 and 4")
    display_all_pets()

def add_new_training_to_pet_by_id():
  search_id = input("Enter the id of the pet you would like to add a training too: ")
  pet = find_pet_by_id(search_id)
  if pet is None:
    print("Pet not found")
    add_new_training_to_pet_by_id()
  else:
    display_add_training_to_pet_submenu(pet)

def remove_pet_by_id():
  search_id = input("Enter the id of the pet you want to remove: ")
  pet = find_pet_by_id(search_id)
  if pet is None:
    print("Pet not found")
    remove_pet_by_id()
  else:
    db.session.delete(pet)
    db.session.commit()
    display_all_pets()

def choose_pet_by_id():
  search_id = input("Enter the id of the pet: ")
  pet = find_pet_by_id(search_id)
  if pet is not None:
    print(
      f"Id: {pet.id}, Name: {pet.name}, Species: {pet.species}, Temperament: {pet.temperament}, Muzzle: {pet.muzzle}"
    )
  else:
    print("Pet not found")
    choose_pet_by_id()
  display_pet_submenu(pet)

def display_pet_submenu(pet):
  print("1. See a pets trainings")
  print("2. Exit")
  choice = input()
  handle_pet_choice(choice, pet)

def handle_pet_choice(choice, pet):
  if choice == "1":
    show_pet_trainings(pet)
  elif choice == "2":
    return
  else:
    print("Choice can only be 1 or 2")
    display_pet_submenu(pet)

def show_pet_trainings(pet):
  trainings = pet.trainings
  for training in trainings:
    print(f"{training.id} | {training.name}")

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    display_welcome()
    while True:
      display_main_menu()
      choice = get_main_menu_choice()
      if choice == "1":
        display_all_trainers()
      elif choice == "2":
        add_new_trainer()
      elif choice == "3":
        display_all_pets()
      elif choice == "4":
        add_new_pet()
      elif choice == "5":
        break
      else:
        print("Can only be between 1 and 5. No letters as well")
      