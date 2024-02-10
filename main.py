# main.py

from models import Game, Player
from scenes import CrossroadsScene, TreasureScene, EnterLockedDoorScene


# Sets up the game
def main():
    print("Welcome to the Adventure Game! What is your name? ")
    player_name = input("> ")

    # Create a new player with the input name
    player = Player(player_name)

    # Initialize the game with the player
    game = Game(player)

    # Add scenes to the game
    game.add_scene("crossroads_scene", CrossroadsScene())
    game.add_scene("treasure_scene", TreasureScene())
    game.add_scene("locked_door_scene", EnterLockedDoorScene())

    # Set starting scene
    game.set_starting_scene("crossroads_scene")

    # Start the game
    game.start()


if __name__ == "__main__":
    main()
