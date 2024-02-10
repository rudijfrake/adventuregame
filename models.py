# models.py


# Class that represents a player in the game
class Player:
    def __init__(self, name):
        # Store the player's name
        self.name = name

        # Initialize an empty inventory list for the player
        self.inventory = []

    # Add an item to the inventory
    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory.")

    # Remove an item from the inventory
    def remove_item(self, item):
        self.inventory.remove(item)
        print(f"{item} has been removed from your inventory.")


# Manages the flow of the game, including scenes and the game loop
class Game:
    def __init__(self, player):
        # The player participating in the game
        self.player = player

        # A dictionary to store the different scenes
        self.scenes = {}

        # Tracks the current scene
        self.current_scene = None

        # Flag to keep the game running
        self.game_running = True

    # Add a scene to the dictionary
    def add_scene(self, scene_name, scene):
        self.scenes[scene_name] = scene

    # Set the starting scene
    def set_starting_scene(self, scene_name):
        self.current_scene = self.scenes.get(scene_name, None)

    # Move to the next scene
    def next_scene(self, scene_name):
        self.current_scene = self.scenes.get(scene_name, None)

    def start(self):
        while self.game_running and self.current_scene:
            # Enter the current scene and get the next scene's name
            next_scene_name = self.current_scene.enter(self.player)

            # Change to the next scene
            self.next_scene(next_scene_name)

    # End the game
    def end_game(self):
        self.game_running = False
