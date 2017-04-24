"""
Class for Exam Rooms.
@author: Chase Fleming
@date: 4/23/17

Defines a room.

"""

from RoomClass import Room


class ExamRoom(Room):

    def __init__(self, number, name, schedule):
        """ Initiates an exam room. """
        super(Room, self).__init__()
        self.name = name
        self.number = number
        self.schedule = schedule
        self.rounds = []
        for i in range(len(schedule)):
            self.rounds.append([])
