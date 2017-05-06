"""
Class for side event rooms.
@author: Chase Fleming
@date: 4/23/17

Defines a side event room. 

"""

from RoomClass import Room


class SideEventRoom(Room):
    """ Side event room class. Used to represent a side event room.
    
        Attributes:
            name - name of the side event.
            schedule - Schedule that will be happening in the room.
            roundnumber - The Nth round of the schedule.
            roomnumber - The Nth room of the same kind
            roster - List of children participating in side event.
    """

    def __init__(self, name, schedule, roundnumber, roomnumber):
        """ Initiates an exam room. """
        super(Room, self).__init__()
        self.name = name
        self.roundnumber = roundnumber
        self.roomnumber = roomnumber
        self.schedule = schedule
        self.roster = []
