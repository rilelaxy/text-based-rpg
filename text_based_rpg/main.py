""" This is the main program for our game. """

from character import Character
from artforms import Artforms
from world import map_location
from world import world_map

if __name__ == "__main__":
    print("Hello, I am your creator.")
    print("Enter your name to see the stats I have given you.")

    hero = Character("Player")
    print(hero)
    """ Prints character stats """
    character_artform = None
    while character_artform is None or character_artform.weapon is None:
        artform = input("Choose one of the following art forms: Artist, Dancer, Musician, Actor, Sculptor: ")
        character_artform = Artforms(artform)
    """ The while loop ensures the player must choose a valid artform to continue """
print(character_artform)

if __name__ == "__main__":

    current_location = "Statue of Creation"
    print("You are currently at:", current_location)

    while True: 
        print("Where would you like to go?")
        location = input("Enter a location: North Artstoria, East Artstoria, West Artstoria, South Artstoria\n")
        current_location = map_location(current_location, location, world_map)
        print("You are now at:", current_location)
        print("Description:", world_map[current_location]["description"])
    """ The while loop allows player to keep exploring locations """