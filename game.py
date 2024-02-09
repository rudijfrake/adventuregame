game_running = True


def end_game():
    global game_running
    print()
    continue_adventure_choice = input("You didn't choose a valid response. Continue Adventure? Type 'yes' or 'no'. ")
    if continue_adventure_choice == "no":
        print()
        print("You are now exiting the game.")
        game_running = False
    elif continue_adventure_choice == "yes":
        pass
    else:
        print()
        print("You are now exiting the game.")
        game_running = False


# Beginning of game message
print()
print("Welcome to our text-based adventure game! ")


# Get player's name to start the adventure
print()
player_name = input("What is your name? ")
print()
print("Hello, " + player_name + "! Let's start our adventure.")


inventory = []  # This creates an empty list named 'inventory'


while game_running:

    # Player is at beginning crossroad in game
    print()
    choice = input("You're at a crossroad. Do you want to go 'left' or 'right'? ")

    # Leads to Golden Key
    if choice == "left":

        # Player already has the Golden Key
        if "Golden Key" in inventory:
            print()
            print("You already have the Golden Key. There's nothing else to discover here. You go back to the "
                  "crossroads from before.")

        # Adds Golden Key to player's inventory
        else:
            print()
            print("You decide to go left and find a treasure chest!")
            inventory.append("Golden Key")
            print("Inside of the chest, you find a Golden Key! \n\nGolden Key has been added to your inventory.")
            print("There is nothing else to discover here. You go back to the crossroads from before.")

    # Leads to locked door
    elif choice == "right":
        print()
        print("You go right and encounter an abandoned stone structure. There is a door with a golden doorknob and "
              "keyhole.")
        door_locked = True

        # Allows player to approach the locked door
        player_locked_door_choice = input("Do you approach the door? Type 'yes' or 'no'? ")

        # Player chooses to approach the locked door
        if player_locked_door_choice == "yes":
            print()
            print("The door is locked.")

            # Player has Golden Key
            if "Golden Key" in inventory:
                use_golden_key = input("Would you like to unlock the door with the Golden Key? Type 'yes' or 'no'. ")

                # Player chooses to unlock door with Golden Key
                if use_golden_key == "yes":
                    print()
                    print("Door unlocked with Golden Key.")
                    inventory.remove("Golden Key")     # This line removes the Golden Key from the inventory
                    print("Golden Key removed from inventory.")
                    door_locked = False
                    print("You open the door and enter into the dark room behind it.")
                    print("Congrats! You made it through the level. Game over.")

                    # Player has completed game; game ends
                    game_running = False

                # Player chooses not to unlock door with Golden Key
                elif use_golden_key == "no":
                    print()
                    print("There is nothing left to discover here. You go back to the crossroads from before.")

                # Player does not give a valid response
                else:
                    end_game()

            # Player does not have the Golden Key in their inventory
            elif "Golden Key" not in inventory:
                unlock_without_key = input("Would you like to use a key to unlock this door? Type 'yes' or 'no'. ")
                if unlock_without_key == "yes":
                    print()
                    print("You do not have a key to unlock this door.")
                    print("Without a key to unlock the door, you look around and decide there is nothing else to "
                          "discover in this area. You go back to the crossroads from before.")
                elif unlock_without_key == "no":
                    print()
                    print("Other than this door, there is nothing else to discover here. You go back to the crossroads "
                          "from before.")

            # Player does not give a valid response
            else:
                end_game()

        # Player chooses not to approach the door
        elif player_locked_door_choice == "no":
            print()
            print("Other than the structure's door, you look around the area and decide there is nothing else to "
                  "discover in this area. You go back to the crossroads from before.")

        # Player does not give a valid response
        else:
            end_game()

    # Player does not give a valid response
    else:
        end_game()
