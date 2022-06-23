import time 

def intro():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")  
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) dagger. \n ")

def print_pause(message_to_display):
    print(message_to_display)
    time.sleep(1)

def choose_option():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.") 
    print_pause("What would you like to do?")
    val = input("Please enter 1 or 2.")
    if val == '1': 
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens and out steps a troll.")
        print_pause("Eep! This is the troll's house!")
        print_pause("The troll attacks you!")
        print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.")
        face_troll()
    elif val == '2':
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword with you.")
        print_pause("You walk back out to the field.")
        choose_option()
    else:
        print_pause("Invalid option. Please try again")
        choose_option()


def face_troll():
        val = input("Would you like to (1) fight or (2) run away?")
        if val == '1': 
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the troll.")
            print_pause("You have been defeated!")
            play_exit()
        elif val == '2': 
            print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
            choose_option()
        else: 
            print_pause("Invalid option. Please try again")
            face_troll()


def play_exit():
    val = input("Would you like to play again? (y/n)").lower()
    if val == 'y': 
        play_game()
    if val == 'n':
        exit()

def play_game():
    intro()
    choose_option()


play_game()