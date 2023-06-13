def map_location(current_location, location, world_map):
    if location in world_map:
        return location
    """ If the player has chosen a location it is returned to them """
    
    print("This is not a location!")
    return current_location
""" Warns player and returns current location as they will not have moved """

# Methods
world_map = {
    "Statue of Creation": {
        "description": "You are at the starting point of life, and your journey.",
    },
    "North Artstoria": {
        "description": "You have reached the northern area of Artstoria.",
    },
    "East Artstoria": {
        "description": "You have reached the eastern area of Artstoria.",
    },
    "West Artstoria": {
        "description": "You find a chest with a note inside! The note reads:\n" "Thank you for playing!"
    },
    "South Artstoria": {
        "description": "You have reached the southern area of Artstoria.",
    }
}
""" The world_map is a dictionary of valid map locations to explore """