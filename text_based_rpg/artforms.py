""" Our Character Artform
"""


import character
import creator

class Artforms:
    
    def __init__(self, artform):
        print("Artist, Weapon: Paintbrush \n")
        print("Artist, Weapon: Paintbrush \n")
        print("Artist, Weapon: Paintbrush \n")
        self.artform = input("Pick one of the above artforms: ")

    def __str__(self) -> str:
        """returns a formatted display of character details"""
        repr = "Class Stats:\n"
        repr += f"Chosen Artform: {self.artform}\n"
        repr += f"Weapon assigned: {self.paintbrush}\n"
        return repr
