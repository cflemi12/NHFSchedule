"""
Class for Exam Rooms.
@author: Chase Fleming
@date: 5/5/17

Defines a buzzer Room.

"""

from RoomClass import Room


class BuzzerRoom(Room):
    """ An exam room object representing the single exam room.

        Attributes:
            name - Name of the specific type of exam room. E.g. military, geo, etc.
            roundnumber - Nth round of the schedule.
            roomnumber - Number of this type of room in a round.
            schedule - List of intervals representing the schedule of a type of event.
            roster - Roster of the kids assigned to this room.
    """

    def __init__(self, schedule, roundnumber, roomnumber):
        """ Initiates an exam room. """
        super(Room, self).__init__()
        self.roundnumber = roundnumber
        self.roomnumber = roomnumber
        self.schedule = schedule
        self.roster = {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None,
                       'h': None, 'i': None, 'j': None}

    def addplayer(self, player):
        """ Adds a player to the roster. """
        self.roster[player.seed] = player
