"""
Class for rooms.
@author: Chase Fleming
@date: 4/23/17

Defines a tournament set schedule. 
"""

from interval import interval
from BuzzerRoomClass import BuzzerRoom
from ExamRoomClass import ExamRoom
from SideEventRoomClass import SideEventRoom
from math import ceil, floor
from random import sample
from operator import itemgetter

MAX_ROOMS = 40
ROOM_RANGE = xrange(MAX_ROOMS)


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
            examrooms - ExamRoom for all regular exams.
            militaryrooms - Military exam room.
            geographyrooms - Geography exam room.
            csarooms - CSA exam rooms.

    """

    def __init__(self):
        """ Initialize the tournament by creating the schedule and the rooms. """
        buzztimes = [110, 110.5, 111, 111.5, 113, 113.5, 114, 114.5,
                     211, 211.5, 212, 212.5, 214, 214.5, 215, 215.5, ]
        self.buzzerschedule = list(map(lambda time: interval([time, time + .5]), buzztimes))

        # fill exam schedule
        examtimes = [110, 111, 114, 115, 118, 119, 120, 209, 211, 214, 215]
        self.examschedule = list(map(lambda time: interval([time, time + 1]), examtimes))
        self.militaryschedule = list(map(lambda time: interval([time, time + 1]), [112, 217]))
        self.geographyschedule = list(map(lambda time: interval([time, time + 1]), [213, 117]))
        self.csaexamschedule = list(map(lambda time: interval([time, time + 1]), [116, 210]))

        # fill side schedule
        self.citizenschedule = list(map(lambda time: interval([time, time + .5]), [115, 209]))
        self.sandeschedule = list(map(lambda time: interval([time, time + .5]), [115.5, 209.5]))
        self.anniversaryschedule = list(map(lambda time: interval([time, time + .5]), [213, 213.5]))

        # fill bowl schedule
        self.bowlschedule = list(map(lambda time: interval([time, time + 3]), [118, 218]))

        # fill fqn schedule
        self.fqnschedule = [interval([118, 118 + 2])]

        """ Initialize rooms. """
        # start with buzzer rooms
        self.buzzerrooms = []
        for i, item in enumerate(self.buzzerschedule):
            roundrooms = list(map(lambda j: BuzzerRoom(self.buzzerschedule, i, j), ROOM_RANGE))
            self.buzzerrooms.append(roundrooms)

        # anniversary rooms
        self.anniversaryrooms = []
        for i, item in enumerate(self.anniversaryschedule):
            roundrooms = list(map(lambda j: SideEventRoom("anniversary", self.anniversaryschedule, i, j), ROOM_RANGE))
            self.anniversaryrooms.append(roundrooms)

        # sports and enterinament rooms
        self.sanderooms = []
        for i, item in enumerate(self.sandeschedule):
            roundrooms = list(map(lambda j: SideEventRoom("sande", self.sandeschedule, i, j), ROOM_RANGE))
            self.sanderooms.append(roundrooms)

        # citizenship bee rooms
        self.citizenrooms = []
        for i, item in enumerate(self.citizenschedule):
            roundrooms = list(map(lambda j: SideEventRoom("citizen", self.citizenschedule, i, j), ROOM_RANGE))
            self.citizenrooms.append(roundrooms)

        # regular exam rooms
        k = xrange(len(self.examschedule))
        self.examrooms = list(map(lambda j: ExamRoom("exam", self.examschedule, j), k))

        # military exam rooms
        k = xrange(len(self.militaryschedule))
        self.militaryrooms = list(map(lambda j: ExamRoom("military", self.militaryschedule, j), k))

        # geography exam rooms
        k = xrange(len(self.geographyschedule))
        self.geographyrooms = list(map(lambda j: ExamRoom("geography", self.geographyschedule, j), k))

        # csa exam rooms
        self.csarooms = []
        for i in xrange(len(self.csaexamschedule)):
            cit = ExamRoom("cit", self.csaexamschedule, i)
            sport = ExamRoom("sports", self.csaexamschedule, i)
            self.csarooms.append((cit, sport))

    def scheduleexamrooms(self, field):
        """ Assigns field to exam rooms. """
        # regular exams
        for player in field:
            for event in player.schedule:
                if event[0] == "History Bee Exam":
                    self.examrooms[self.examschedule.index(event[1])].addplayer(player)
                    event[2] = "Exam Room"

        # geography exams
        for player in field:
            for event in player.schedule:
                if event[0] == "Geography Exam":
                    self.geographyrooms[self.geographyschedule.index(event[1])].addplayer(player)
                    event[2] = "Exam Room"

        # military exams
        for player in field:
            for event in player.schedule:
                if event[0] == "Military Exam":
                    self.militaryrooms[self.militaryschedule.index(event[1])].addplayer(player)
                    event[2] = "Exam Room"

    def schedulesiderooms(self, field):
        """ Assigns field to side event rooms. """
        sande = list(filter(lambda stu: stu.sande, field))
        cit = list(filter(lambda stu: stu.citizen, field))

        # creates pools of players for sports and entertainemnt
        poolsande = [[] for _ in self.sandeschedule]
        for player in sande:
            for event in player.schedule:
                if event[0] == "Sports and Entertainment Bee":
                    poolsande[self.sandeschedule.index(event[1])].append(player)
                if event[0] == "Sports and Entertainemnt Exam":
                    self.csarooms[self.csaexamschedule.index(event[1])][1].addplayer(player)
                    event[2] = "Exam Room"

        # divides pool
        eig1 = list(filter(lambda stu: stu.division == '8', poolsande[0]))
        eig2 = list(filter(lambda stu: stu.division == '8', poolsande[1]))
        sev1 = list(filter(lambda stu: stu.division == '7', poolsande[0]))
        sev2 = list(filter(lambda stu: stu.division == '7', poolsande[1]))
        elm1 = list(filter(lambda stu: stu.division == 'Elementary', poolsande[0]))
        elm2 = list(filter(lambda stu: stu.division == 'Elementary', poolsande[1]))

        # puts players into rooms
        rn = [40]
        self.sideroomhelp(rn, eig1, self.sanderooms[0])
        self.sideroomhelp(rn, sev1, self.sanderooms[0])
        self.sideroomhelp(rn, elm1, self.sanderooms[0])

        rn = [40]
        self.sideroomhelp(rn, eig2, self.sanderooms[1])
        self.sideroomhelp(rn, sev2, self.sanderooms[1])
        self.sideroomhelp(rn, elm2, self.sanderooms[1])

        # create pools of players for citizenship bee
        poolcit = [[] for _ in self.citizenschedule]
        for player in cit:
            for event in player.schedule:
                if event[0] == "Citizenship Bee":
                    poolcit[self.citizenschedule.index(event[1])].append(player)
                if event[0] == "Citizenship Exam":
                    self.csarooms[self.csaexamschedule.index(event[1])][0].addplayer(player)
                    event[2] = "Exam Room"

        # divides pool
        eig1 = list(filter(lambda stu: stu.division == '8', poolcit[0]))
        eig2 = list(filter(lambda stu: stu.division == '8', poolcit[1]))
        sev1 = list(filter(lambda stu: stu.division == '7', poolcit[0]))
        sev2 = list(filter(lambda stu: stu.division == '7', poolcit[1]))
        elm1 = list(filter(lambda stu: stu.division == 'Elementary', poolcit[0]))
        elm2 = list(filter(lambda stu: stu.division == 'Elementary', poolcit[1]))

        # puts players into rooms
        rn = [40]
        self.sideroomhelp(rn, eig1, self.citizenrooms[0])
        self.sideroomhelp(rn, sev1, self.citizenrooms[0])
        self.sideroomhelp(rn, elm1, self.citizenrooms[0])

        rn = [40]
        self.sideroomhelp(rn, eig2, self.citizenrooms[1])
        self.sideroomhelp(rn, sev2, self.citizenrooms[1])
        self.sideroomhelp(rn, elm2, self.citizenrooms[1])

    def schedulebuzzerrooms(self, field):
        """ Assigns field to buzzerrooms."""
        seeds = [seed for seed in "abcdefghij"]
        divisions = ["8", "7", "Elementary"]
        field = list(filter(lambda stu: stu.bee is True, field))
        for player in field:
            player.schedule = list(sorted(player.schedule, key=itemgetter(1)))

        playersperround = [[] for _ in range(len(self.buzzerschedule))]
        for i, time in enumerate(self.buzzerschedule, 0):
            for player in field:
                for event in player.schedule:
                    if time in event:
                        playersperround[i].append(player)

        count = 0
        for j, rounds in enumerate(playersperround, 0):
            roomcounter = 0
            for div in divisions:
                for seed in seeds:
                    tosched = list(filter(lambda stu: stu.division == div and stu.seed == seed, playersperround[j]))
                    count += len(tosched)
        print count

    @staticmethod
    def sideroomhelp(roomnum, players, rooms):
        """ Helps schedule the side events by calculating the amount of players."""
        numrooms = ceil(len(players) / 10.0)
        mod = len(players) % int(numrooms)
        freq = [int(floor(len(players) / numrooms))] * int(numrooms)
        for i in range(mod):
            freq[i] += 1
        for num in freq:
            toadd = sample(players, num)
            for player in toadd:
                players.remove(player)
                rooms[roomnum[0] - 1].addplayer(player)
                for event in player.schedule:
                    if event[0] == "Sports and Entertainment Bee":
                        event[2] = "Room " + str(roomnum[0])
                    if event[0] == "Citizenship Bee":
                        event[2] = "Room " + str(roomnum[0])
            roomnum[0] -= 1
