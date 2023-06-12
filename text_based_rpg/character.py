""" Our Character Class
"""

import random
import creator

class Character:
    
    # constructor
    def __init__(self, name):
        self.name = input("Enter name: ")
        self.strength = creator.choose_stats()
        self.stamina = creator.choose_stats()
        self.talent = creator.choose_stats()
        self.health = creator.choose_stats()
        self.attack_modifier = creator.get_modifier(self.strength)

    # methods
    # when printing the character
    def __str__(self) -> str:
        """returns a formatted display of character details"""
        repr = "Character Stats:\n"
        repr += f"Name: {self.name}\n"
        repr += f"Strength: {self.strength}\n"
        repr += f"Stamina: {self.stamina}\n"
        repr += f"AM: {self.attack_modifier}"
        return repr
    
