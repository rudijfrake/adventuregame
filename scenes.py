# scenes.py

import time


# Serves as a base class for all scenes
class Scene:
    def enter(self):
        pass


class CrossroadsScene(Scene):
    def enter(self):
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
    def enter(self):
        print("\nYou've found a treasure chest!")
        # Add logic for treasure and possibly updating the player's inventory

        # Return to the crossroads after this scene
        return "crossroads_scene"


class LockedDoorScene(Scene):
    def enter(self):
        print("\nYou go right.")
        time.sleep(2)
        print("\nYou come across an abandoned stone structure that has a single door with a golden keyhole.")
        time.sleep(2)
        print("\nWould you like to approach the door? Type 'yes' or 'no'.")
        choice = input("> ")

        if choice == "yes":
            print("You approach the door and try to open it, but the door is locked.")
        elif choice == "no":
            # something
        else:
            #something

        # Return to the crossroads if the door cannot be opened
        return "crossroads_scene"
