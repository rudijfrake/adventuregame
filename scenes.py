# scenes.py

import time


# Serves as a base class for all scenes
class Scene:
    def enter(self, player):
        pass


class CrossroadsScene(Scene):
    def enter(self, player):
        print("\nYou're at a crossroad. Where do you want to go? Type 'right' or 'left'")
        choice = input("> ")

        if choice == "left":
            # Return the key for the next scene
            return "treasure_scene"
        elif choice == "right":
            return "locked_door_scene"
        else:
            # Return to the same scene for invalid input
            print("Not a valid direction.")
            return "crossroads_scene"


class TreasureScene(Scene):
    def enter(self, player):
        print("\nYou've found a treasure chest!")
        # Add logic for treasure and possibly updating the player's inventory

        # Return to the crossroads after this scene
        return "crossroads_scene"


class EnterLockedDoorScene(Scene):
    def enter(self, player):
        print("\nYou go right.")
        time.sleep(2)
        print("\nYou come across an abandoned stone structure that has a single door with a golden keyhole.")
        time.sleep(2)

        door_unlocked = False  # Keep track of the door's state

        while True:  # This loop will ensure the player makes a valid choice
            if not door_unlocked:
                print("\nWould you like to approach the door? Type 'yes' or 'no'.")
                choice = input("> ")

                if choice == "yes":
                    print("\nYou approach the door and try to open it, but the door is locked.")
                    if "Golden Key" in player.inventory:
                        player.inventory.remove("Golden Key")  # Remove the key from the inventory
                        print("\"Golden Key\" removed from inventory.")
                        door_unlocked = True  # Update the door's state to unlocked

                        print("\nThe door is now unlocked. Would you like to enter? Type 'yes' or 'no'.")
                        enter_door_choice = input("> ")
                        if enter_door_choice == "yes":
                            # Assuming 'secret_room_scene' is the key for the next scene
                            return "secret_room_scene"
                        elif enter_door_choice == "no":
                            # They choose not to enter, so they're taken back to the decision point about the door
                            continue
                        else:
                            print("Not a valid choice. Please type 'yes' or 'no'.")
                    else:
                        print("\nYou do not have the key to unlock this door.")
                        # No key in the inventory, so offer to return to the crossroads
                        return "crossroads_scene"

                elif choice == "no":
                    print(
                        "\nAfter taking a look around, you decide there is nothing to discover in this area other than "
                        "the door.")
                    time.sleep(2)
                    return "crossroads_scene"  # Return to the crossroads scene

                else:
                    print("Not a valid choice. Please type 'yes' or 'no'.")
                    # Invalid input, so the loop will repeat, asking the player again
            else:
                # If the door is already unlocked, ask if they want to enter
                print("\nThe door is unlocked. Would you like to enter? Type 'yes' or 'no'.")
                enter_door_choice = input("> ")
                if enter_door_choice == "yes":
                    return "secret_room_scene"
                elif enter_door_choice == "no":
                    return "crossroads_scene"
                else:
                    print("Not a valid choice. Please type 'yes' or 'no'.")

        # Return to the crossroads if the door cannot be opened
        return "crossroads_scene"
