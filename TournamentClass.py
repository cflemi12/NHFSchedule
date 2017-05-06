"""
Class for rooms.
@author: Chase Fleming
@date: 4/23/17

Defines a tournament set schedule. 
"""

from interval import interval
from ExamRoomClass import ExamRoom
from BuzzerRoomClass import BuzzerRoom
from SideEventRoomClass import SideEventRoom

MAX_ROOMS = 45


class Tournament(object):
    """Tournament that will hold the schedules for each event in the form of intervals whose points
    are times. E.G. 110 represents friday at 10am, while 215.5 represents Saturdat at 3:30pm. The 
    tournament object will also hold the rooms necessary for the tournament.

        Attributes:
            buzzerschedule - Intervals of buzzer round times.
            examschedule - Intervals of regular exam round times.
            militaryschedule - Intervals of military exam round times.
            geographyschedule - Intervals of geography exam round times.
            csaexamschedule - Intervals of citizen, sports, and anniversary exam round times.
            citizenschedule - Intervals of citizenship bee round times.
            sandeschedule - Intervals of sports and entertainment bee round times.
            anniversaryschedule - Intervals of anniversary bee round times. 
            bowlschedule - Intervals of bowl round times.
            fqnschedule - Intervals for family quiz night.
            buzzerrooms - Rooms for the regular history bee.
            anniversaryrooms - Rooms for anniversary bee.
            sanderooms - Rooms for the sports and entertainment bee.
            citizenrooms - Rooms for the citizenship bee.
            examroom - ExamRoom for all regular exams.
            militaryroom - Military exam room.
            geographyroom - Geography exam room.
            csaroom - CSA exam room.

    """

    def __init__(self):
        """ Initialize the tournament by creating the schedule and the rooms. """
        self.buzzerschedule = []
        times = [110, 110.5, 111, 111.5, 113, 113.5, 114, 114.5,
                 211, 211.5, 212, 212.5, 214, 214.5, 215, 215.5, ]
        for start in times:
            k = interval(start, start + .5)
            self.buzzerschedule.append(k)

        # fill exam schedule
        self.examschedule = []
        times = [110, 111, 114, 115, 118, 119, 120,
                 209, 211, 214, 215]
        for start in times:
            k = interval(start, start + 1)
            self.examschedule.append(k)
        self.militaryschedule = []
        times = [112, 117]
        for start in times:
            k = interval(start, start + 1)
            self.militaryschedule.append(k)
        self.geographyschedule = []
        times = [213, 217]
        for start in times:
            k = interval(start, start + 1)
            self.geographyschedule.append(k)
        self.csaexamschedule = []
        times = [116, 210]
        for start in times:
            k = interval(start, start + 1)
            self.csaexamschedule.append(k)

        # fill side schedule
        self.citizenschedule = []
        times = [115, 209]
        for start in times:
            k = interval(start, start + .5)
            self.citizenschedule.append(k)
        self.sandeschedule = []
        times = [115.5, 209.5]
        for start in times:
            k = interval(start, start + .5)
            self.sandeschedule.append(k)
        self.anniversaryschedule = []
        times = [116, 210]
        for start in times:
            k = interval(start, start + .5)
            self.anniversaryschedule.append(k)

        # fill bowl schedule
        self.bowlschedule = []
        times = [118, 218]
        for start in times:
            k = interval(start, start + 3)
            self.bowlschedule.append(k)

        # fill fqn schedule
        self.fqnschedule = []
        times = [118]
        for start in times:
            k = interval(start, start + 2)
            self.fqnschedule.append(k)

        """ Initialize rooms. """
        # start with buzzer rooms
        self.buzzerrooms = []
        for i in range(len(self.buzzerschedule)):
            roundrooms = []
            for j in range(MAX_ROOMS):
                newroom = BuzzerRoom(self.buzzerschedule, i, j)
                roundrooms.append(newroom)
            self.buzzerrooms.append(roundrooms)

        # anniversary rooms
        self.anniversaryrooms = []
        for i in range(len(self.anniversaryschedule)):
            roundrooms = []
            for j in range(MAX_ROOMS):
                newroom = SideEventRoom("anniversary", self.anniversaryschedule, i, j)
                roundrooms.append(newroom)
            self.anniversaryrooms.append(newroom)

        # sports and enterinament rooms
        self.sanderooms = []
        for i in range(len(self.sandeschedule)):
            roundrooms = []
            for j in range(MAX_ROOMS):
                newroom = SideEventRoom("sande", self.sandeschedule, i, j)
                roundrooms.append(newroom)
            self.sanderooms.append(newroom)

        # citizenship bee rooms
        self.citizenrooms = []
        for i in range(len(self.citizenschedule)):
            roundrooms = []
            for j in range(MAX_ROOMS):
                newroom = SideEventRoom("citizen", self.citizenschedule, i, j)
                roundrooms.append(newroom)
            self.citizenrooms.append(newroom)

        # regular exam rooms
        self.examrooms = []
        for i in range(len(self.examschedule)):
            examroom = ExamRoom("exam", self.examschedule, i)
            self.examrooms.append(examroom)

        #