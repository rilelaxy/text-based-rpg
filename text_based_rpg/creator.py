"""creator.py - the creator of characters in the game.

Will handle tasks and functions related to stats and customization
"""

import random

def choose_stats() -> int:
    """gets stats for character's attribute from user"""

    return random.randint(6, 18)

def get_modifier(stat: int) -> int:
    """get a modifier based on value of stat"""
    # Check modifier table
    modifier = 0
    return stat + modifier

