"""
Class for players.
@author: Chase Fleming
@date: 4/20/17

Defines a player in the NHF.
"""

import random

from interval import interval

idchoices = list(range(10000, 99999))
count = 0


def getcount():
    global count
    return count


def zerocount():
    global count
    count = 0


class Player(object):
    """
           Attributes:
               name - String of name of participant.
               division - String of Elementary, 7, or 8 grade.
               hometown - String of where the player is from.
               school - String of school they're representing.
               anniversary - Boolean for participating in the anniversary challenge.
               sande - Boolean for participating in the sports and entertainment bee.
               citizen - Boolean for participating in the citizenship bee.
               military - Boolean for participating in the Subject Exam #1.
               geography - Boolean for participating in the Subject Exam #2.
               csaexam - Boolean for participating in the Citizenship, Sports, and Anniversary exam.
               bowl - Boolean for participating in the Bowl.
               seed - String representing seat seed. 
               schedule - Schedule for the player. A tuple containing the name of the event and time.
    """

    def __init__(self, name, division, hometown, school, bee, bowl, anniversary, sande, citizen, military,
                 geography, fqn, seed, tournament, restriction=None):
        """ Initiates the player. 
        :type restriction: a set of intervals which the player cannot play
        """
        self.name = name
        self.division = division
        self.hometown = hometown
        self.school = school
        self.bee = bee
        self.bowl = bowl
        self.anniversary = anniversary
        self.sande = sande
        self.citizen = citizen
        self.military = military
        self.geography = geography
        self.fqn = fqn
        self.seed = seed
        self.restriction = restriction
        self.schedule = []
        tempid = random.choice(idchoices)
        idchoices.remove(tempid)
        if self.division == "8":
            self.id = int("8" + str(tempid))
        elif self.division == "7":
            self.id = int("7" + str(tempid))
        else:
            self.id = int("6" + str(tempid))
        self.buzzrounds = 0

        if restriction is None:
            self.restriction = []
        self.schedule = []
        if bowl:
            for period in tournament.bowlschedule:
                self.restriction.append(period)
        if fqn:
            for period in tournament.fqnschedule:
                self.restriction.append(period)

    def getinfo(self):
        """ Returns the basic information of each player in a list. """
        return [self.name, self.division, self.hometown, self.school, self.anniversary, self.sande, self.citizen,
                self.military, self.geography, self.bowl, self.seed]

    def schedulemil(self, tournament):
        """ Schedules a player for a military exam. """
        if self.military is False:
            return self
        time = random.choice(tournament.militaryschedule)
        while self.overlap(time):
            time = random.choice(tournament.militaryschedule)
        event = ["Military Exam", time, None]
        self.schedule.append(event)
        self.restriction.append(time)
        return self

    def schedulegeo(self, tournament):
        """ Schedules a player for a military exam. """
        if self.geography is False:
            return self
        time = random.choice(tournament.geographyschedule)
        while self.overlap(time):
            time = random.choice(tournament.militaryschedule)
        event = ["Geography Exam", time, None]
        self.schedule.append(event)
        self.restriction.append(time)
        return self

    def schedulecit(self, tournament):
        """ Scheduels a player for the citizenship bee. """
        if self.citizen is False:
            return self
        time = random.choice(tournament.citizenschedule)
        while self.overlap(time):
            time = random.choice(tournament.citizenschedule)
        event = ["Citizenship Bee", time, None]
        self.schedule.append(event)
        self.restriction.append(time)
        time = random.choice(tournament.csaexamschedule)
        while self.overlap(time):
            time = random.choice(tournament.csaexamschedule)
        event = ["Citizenship Exam", time, None]
        self.schedule.append(event)
        self.restriction.append(time)
        return self

    def schedulesae(self, tournament):
        """ Scheduels a player for the citizenship bee. """
        if self.sande is False:
            return self
        time = random.choice(tournament.sandeschedule)
        while self.overlap(time):
            time = random.choice(tournament.sandeschedule)
        event = ["Sports and Entertainment Bee", time, None]
        self.schedule.append(event)
        self.restriction.append(time)
        time = random.choice(tournament.csaexamschedule)
        while self.overlap(time):
            time = random.choice(tournament.csaexamschedule)
        event = ["Sports and Entertainemnt Exam", time, None]
        self.schedule.append(event)
        self.restriction.append(time)
        return self

    def scheduleexm(self, tournament):
        """ Schedules a bee player for an exam. """
        if self.bee is not True:
            return self
        temp = tournament.examschedule[:]
        time = random.choice(temp)
        while overlapthirty(time, self.restriction):
            temp.remove(time)
            if len(temp) == 0:
                global count
                count += 1
                return self
            time = random.choice(temp)
        event = ["History Bee Exam", time, None]
        self.schedule.append(event)
        self.restriction.append(time)
        return self

    def attemptschedulebuz(self, freq, n, sched):
        """ Attempt to schedule buzzer rounds. Returns a boolean, player, and schedule. """
        # Create temps
        tempschedule = self.schedule[:]
        temprestriction = self.restriction[:]
        temp = sched[:]

        # Attempt first buzz round
        time = random.choice(temp)
        while overlapthirty(time, temprestriction) or freq[sched.index(time)] >= n:
            temp.remove(time)
            if len(temp) == 0:
                return False, self, tempschedule
            time = random.choice(temp)
        event = ["History Bee Buzzer Round", time, None]
        tempschedule.append(event)
        temprestriction.append(time)
        freq[sched.index(time)] += 1

        # Attempt second buzz round
        if len(temp) == 0:
            return False, self, tempschedule
        time = random.choice(temp)
        while overlapthirty(time, temprestriction) or freq[sched.index(time)] >= n:
            temp.remove(time)
            if len(temp) == 0:
                return False, self, tempschedule
            time = random.choice(temp)
        event = ["History Bee Buzzer Round", time, None]
        tempschedule.append(event)
        temprestriction.append(time)
        freq[sched.index(time)] += 1

        return True, self, tempschedule

    def updateschedule(self, newschedule):
        """ Sets a player schedule given a new one and updates restrictions."""
        self.schedule = newschedule
        for event, time, room in self.schedule:
            self.restriction.append(time)

    def overlap(self, event):
        """ Determines if event is in a players restriction. """
        for res in self.restriction:
            k = res & event
            if len(k) == 0:
                continue
            if k[0][1] - k[0][0] != 0:
                return True
        return False


def overlapthirty(event, restrictions):
    """ Determines if the event is at least 30minutes apart. """
    for res in restrictions:
        bot = interval([res[0][0] - 0.5, res[0][0]])
        top = interval([res[0][1], res[0][1] + 0.5])
        expanded = bot | res | top
        k = expanded & event
        if len(k) == 0:
            continue
        if k[0][1] - k[0][0] != 0:
            return True
    return False
