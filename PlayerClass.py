"""
Class for players.
@author: Chase Fleming
@date: 4/20/17
"""


class Player(object):
    """ Defines a player in the NHF.

        Attributes:
            name - Name of participant.
            seed - Character A to J that represents seat number.
            grade - Grade of player.
            schedule - Array of time blocks representing schedule.
            sides - Array representation of participating in side events.
            restrictions - Time blocks representing when a player can't participate.
    """

    def __init__(self, name, seed, grade, sides, *restrictions):
        self.name = name
        self.seed = seed
        self.grade = grade
        self.sides = sides
        self.restrictions = restrictions
        self.schedule = []