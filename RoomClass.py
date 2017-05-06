"""
Class for rooms.
@author: Chase Fleming
@date: 4/23/17

Defines a room.

"""


class Room(object):
    """Room objects are representative of one room at the tournament.
    
        Attributes:
            schedule - A schedule in the form of a list of intervals of the event going on in that room.
            roomnumber - Number  representing the nth room for a given round. E.g. the 12th room of the buzzer roounds.
            roundnumber - Number indicating its in the nth round in schedule[n].
    """

    def __init__(self, schedule, roundnumber, roomnumber=0):
        """ Initiates a room. """

        self.schedule = schedule
        self.roundnumber = roundnumber
        self.roomnumber = roomnumber

