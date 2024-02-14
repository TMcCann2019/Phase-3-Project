from config import app, migrate
from rich import print
from models import db, Training
from db_utils import (
    get_all_pets,
    get_all_trainers,
    find_trainer_by_id,
    find_pet_by_id,
    display_add_training_to_pet_submenu,
    add_new_pet,
    add_new_trainer,
    search_trainer_by,
    search_pet_by_species,
    search_pet_by_temperament,
    search_pet_by_muzzle
)


def display_welcome():
    print(
        """
    OOOOOOO0o.   ...'.....          ...............'.,
    OOOOOOkkl......   .,,'...        ..............'';
    Oko::;,,'.....     .:llc:;'..... ..............,'.
    Ox,                .';:coxxdl,.    ............,;.
    Ok;              .',;:coxxxo:.      ...... ...';cl
    OOx,          ..,:odolddollc:'.      ......  ...'c
    OO0k,        .':ccc:;,,;;;;;'.....   ..''... ....;
    0000d::,     .,::::,'..',,,.   ...     .........,;
    0000000Oc   .......'''''',.     ...    ....  ..;;;
    00000000d' ..     .,:;;,..              ... ..','.
    00000000x;....   .':lll:..              ....',,,..
    KKK00000x:'......;:lolclooc.        ........',,,,'
    KKKKKKK0xc,'',',:cooc:ldxOkc..     .,;;'. ...''',,
    XXNNNXXXkl:;;;;;;;:;;;loxOOd:,'.....;co:. .....'''
    NNXXKKXKxlcc:;'.   ..,,,cdxxl;;:;;,,cdo,........''
    KKKXK00Oo::c;,.       .,cloddc::;:ccod;.';;.......
    K000KKKOd:;:,...      .':ccodl:::clodl;,:;,'......
    kOOkkOOkd:;,;,.... . ....',::,;cccoddc,'',:,......
    kkkxdoooc;,'',,'..   ..'''''..;ccloll:,''','......
    odxxxoc:;;;'..''..  ...'...',:cclllll;'.',::'.....
    lloxxdl,',''...'..   ...,;;::::cc:coxc..':loc;'..,
    cllll:'..''''........',:::::::c::;:lkk:',;:::c;,;c
    oolc:;'.,;,'... ...',;;:::::::;;,';lkOl'',;;;;,,,,
    kxdoc:,',;'..........',;;;;;;,''.';coxd,..',;;;;::
    xdol:;'.';,............'....''..';:ccokc....',;;::
    dol:;,'...''''............ .....';:clxOd,.'''''',,
    lc:;,'... .'''',,'..... ... ....,:ccloxkxc::ccclod
    c:;,,'... ....,,,,,,........ ...,:::;;okKKOdddxk0K
    c:,,''''.  .....'',,,'''''......','.',cdk0KK0O000K
    c:;,,'''..  .,'.....''''','.......'',:cldxOKOkk0K0
    ::;,''''..  .,,'........''''...''',,;;:cldxkOOkk0K
    ;;,,,'''....',,''''',,'''',,,'',,,,,,;;::lodkkxxkK
    ;,,,'.......,,,,',,,,,,,,;;;;,,,,,'''',,,;;:ldoloO
    :;,'''......',,''''''''''',,,,'''..........':oxoco
    ;,,,','......'''.'''....'',;;;;,,......'....';ll::
  """
    )
    print("[cyan]Welcome to [red]Fido Training and Grooming[/red][/cyan]")


def display_main_menu():
    print("[magenta]Main Menu[/magenta]")
    print("1. [purple]Show all Trainers[/purple]")
    print("2. [yellow]Add a new Trainer[/yellow]")
    print("3. [green]Show all Pets [/green]")
    print("4. [sandy_brown]Add a new Pet [/sandy_brown]")
    print("5. [light_pink1]Exit [/light_pink1]")


def get_main_menu_choice():
    return input("Which one would you like to do? ")


def display_all_trainers():
    trainers = get_all_trainers()
    for trainer in trainers:
        print(f"{trainer.id} | {trainer.name} | {trainer.specialization}")
    print("[magenta]What do you want to do now? [/magenta]")
    print("1. [sandy_brown]See more about the trainer[/sandy_brown]")
    print("2. [green]Remove a Trainer[/green]")
    print("3. [red]Search for a Trainer[/red]")
    print("4. [light_pink1]Exit[/light_pink1]")
    choice = input("Your choice for the trainers?: ")
    if choice == "1":
        choose_trainer_by_id()
    elif choice == "2":
        remove_trainer_by_id()
    elif choice == "3":
        search_trainer_by()
    elif choice == "4":
        return
    else:
        print("Invalid input. Please choose a number above")
        display_all_trainers()


def remove_trainer_by_id():
    search_id = input("Enter the number of the trainer you would like to remove: ")
    trainer = find_trainer_by_id(search_id)
    if trainer is None:
        print("Trainer not found")
        remove_trainer_by_id()
    else:
        db.session.delete(trainer)
        db.session.commit()
        display_all_trainers()


def choose_trainer_by_id():
    search_id = input("Enter the number of the trainer: ")
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
    print("1. [sandy_brown]See a trainers trainings[/sandy_brown]")
    print("2. [green]Update a training[/green]")
    print("3. [light_pink1]Exit[/light_pink1]")
    choice = input("What would you like to do now?: ")
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
    trainings = trainer.trainings
    if not trainings:
        print("No trainings to update")
        return
    print("[magenta]Current Trainings[/magenta]:")
    for training in trainings:
        print(f"{training.id} | {training.name}")
    training_id = input("Enter the number of the training to update: ")
    training = Training.query.get(training_id)
    if training and training in trainer.trainings:
        new_name = input(f"New Training: ").capitalize()
        training.name = new_name
        db.session.commit()
        display_trainer_submenu(trainer)
    else:
        print("Training not found")
        update_trainings(trainer)


def display_all_pets():
    pets = get_all_pets()
    for pet in pets:
        print(f"{pet.id} | {pet.name} | {pet.species}")
    print("[magenta]What do you want to do now?[/magenta]")
    print("1. [sandy_brown]See more about the pets[/sandy_brown]")
    print("2. [green]Remove a pet[/green]")
    print("3. [violet]Add a new training [/violet]")
    print("4. [red]Search for a Pet[/red]")
    print("5. [light_pink1]Exit[/light_pink1]")
    choice = input("Choice?: ")
    if choice == "1":
        choose_pet_by_id()
    elif choice == "2":
        remove_pet_by_id()
    elif choice == "3":
        add_new_training_to_pet_by_id()
    elif choice == "4":
        search_pet_by()
    elif choice == "5":
        return
    else:
        print("Unknown choice. Pleae choose a number between 1 and 4")
        display_all_pets()

def search_pet_by():
    print("How would you like to search for the pet?")
    print("1. [sandy_brown]Species?[/sandy_brown]")
    print("2. [light_pink1]Temperament?[/light_pink1]")
    print("3. [red]Do they need a muzzle?[/red]")
    print("4. [green]Exit[/green]")
    choice = input("Your choice?: ")
    if choice == "1":
        search_pet_by_species()
    elif choice == "2":
        search_pet_by_temperament()
    elif choice == "3":
        search_pet_by_muzzle()
    elif choice == "4":
        return
    else:
        print("Unknown choice. Pleae choose a number between 1 and 4")
        search_pet_by()

def add_new_training_to_pet_by_id():
    search_id = input(
        "Enter the number of the pet you would like to add a training too: "
    )
    pet = find_pet_by_id(search_id)
    if pet is None:
        print("Pet not found")
        add_new_training_to_pet_by_id()
    else:
        display_add_training_to_pet_submenu(pet)


def remove_pet_by_id():
    search_id = input("Enter the number of the pet you want to remove: ")
    pet = find_pet_by_id(search_id)
    if pet is None:
        print("Pet not found")
        remove_pet_by_id()
    else:
        db.session.delete(pet)
        db.session.commit()
        display_all_pets()


def choose_pet_by_id():
    search_id = input("Enter the number of the pet: ")
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
    print("1. [sandy_brown]See a pets trainings[/sandy_brown]")
    print("2. [light_pink1]Exit[/light_pink1]")
    choice = input("Your next choice?: ")
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
