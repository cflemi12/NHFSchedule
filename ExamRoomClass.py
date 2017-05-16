"""
Class for Exam Rooms.
@author: Chase Fleming
@date: 4/23/17

Defines a room.

"""

from RoomClass import Room


class ExamRoom(Room):
    """ An exam room object representing the single exam room.
    
        Attributes:
            name - Name of the specific type of exam room. E.g. military, geo, etc.
            roundnumber - Nth round of the schedule.
            roomnumber - Number of this type of room in a round.
            schedule - List of intervals representing the schedule of a type of event.
            roster - Roster of the kids assigned to this room.
    """

    def __init__(self, name, schedule, roundnumber, roomnumber=0):
        """ Initiates an exam room. """
        super(Room, self).__init__()
        self.name = name
        self.roundnumber = roundnumber
        self.roomnumber = roomnumber
        self.schedule = schedule
        self.roster = []

    def addplayer(self, player):
        self.roster.append(player)