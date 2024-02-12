from config import app, migrate
from rich import print
from models import db
from db_utils import get_all_pets, get_all_trainers, get_all_trainings, find_trainer_by_id, find_pet_by_id

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
  else:
    return

def choose_trainer_by_id():
  search_id = input("Enter the id of the trainer")
  trainer = find_trainer_by_id(search_id)
  print(
    f"Id: {trainer.id}, Name: {trainer.name}, Specialization: {trainer.specialization}"
  )
  display_trainer_submenu(trainer)

def display_trainer_submenu(trainer):
  print("1. See a trainers trainings")
  print("2. Update a training")
  print("3. Exit")
  choice = input()

def add_new_trainer():
  pass

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
  else:
    return

def choose_pet_by_id():
  search_id = input("Enter the id of the pet")
  pet = find_pet_by_id(search_id)
  print(
    f"Id: {pet.id}, Name: {pet.name}, Species: {pet.species}, Temperament: {pet.temperament}, Muzzle: {pet.muzzle}"
  )
  display_pet_submenu(pet)

def display_pet_submenu(pet):
  print("1. See a pets trainings")
  print("3. Exit")
  choice = input()

def add_new_pet():
  pass

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
      else:
        break
      break