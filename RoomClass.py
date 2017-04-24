"""
Class for rooms.
@author: Chase Fleming
@date: 4/23/17

Defines a room.

"""


class Room(object):

    def __init__(self, number, schedule):
        """ Initiates a room. """

        self.number = number
        self.rounds = []
        for i in range(len(schedule)):
            roster = {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None, "h": None, "i": None,
                      "j": None}
            self.rounds.append(roster)
