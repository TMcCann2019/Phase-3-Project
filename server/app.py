from config import app, migrate
from rich import print
from models import db

def display_welcome():
  print("[cyan]Welcom to Fido Training and Stuff[/cyan]")
    
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
  pass

def add_new_trainer():
  pass

def display_all_pets():
  pass

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