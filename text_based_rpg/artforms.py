""" Our Character Artform
"""



class Artforms:
    def __init__(self, artform):
        self.artform = artform
        self.weapon = ""
        self.shield = ""
        self.set_attributes()
    
    def set_attributes(self):
        """ gets artform from user and assigns weapon and shield based upon it """
        if self.artform == "musician":
            self.weapon = "Guitar: 8 attack"
            self.shield = "Sheet Music: 2 defense"
            print("You have chosen the power of sound, Music.\n")
            
        elif self.artform == "dancer":
            self.weapon = "Tutu: 3 attack"
            self.shield = "Ballet Bar: 7 defense"
            print("You have chosen the power of movement, Dance.\n")
            
        elif self.artform == "artist":
            self.weapon = "Paint-brush: 5 attack"
            self.shield = "Paint Palette: 5 defense"
            print("You have chosen the power of visuals, Painting.\n")
            
        elif self.artform == "actor":
            self.weapon = "Acting, the ability to mimic enemies' weapons"
            self.shield = "Tragedy and Comedy masks: 5 defense"
            print("You have chosen the power of performance, Acting.\n")
            
        elif self.artform == "sculptor":
            self.weapon = "Chisel Hammer: 9 attack"
            self.shield = "Statue: 1 defense"
            print("You have chosen the power of building, Sculpting.\n")
            
        else:
            print("That is not an art form listed, please retry")
            self.weapon = None
            self.shield = None

    def __str__(self) -> str:
        """returns a formatted display of character details"""
        repr = ""
        repr += f"Weapon: {self.weapon}\n"
        repr += f"Shield: {self.shield}\n"
        return repr
