"""
Class for players.
@author: Chase Fleming
@date: 4/20/17

Defines a player in the NHF.
"""

import random


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
        """ Initiates the player. """
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
        event = ("Military Exam", time, None)
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
        event = ("Geography Exam", time, None)
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
        event = ("Citizenship Bee", time, None)
        self.schedule.append(event)
        self.restriction.append(time)
        time = random.choice(tournament.csaexamschedule)
        while self.overlap(time):
            time = random.choice(tournament.csaexamschedule)
        event = ("Citizenship Exam", time, None)
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
        event = ("Sports and Entertainment Bee", time, None)
        self.schedule.append(event)
        self.restriction.append(time)
        time = random.choice(tournament.csaexamschedule)
        while self.overlap(time):
            time = random.choice(tournament.csaexamschedule)
        event = ("Sports and Entertainemnt Exam", time, None)
        self.schedule.append(event)
        self.restriction.append(time)
        return self

    def scheduleexm(self, tournament):
        """ Schedules a bee player for an exam. """
        time = random.choice(tournament.examschedule)
        while self.overlap(time):
            time = random.choice(tournament.examschedule)
        event = ("History Bee Exam", time, None)
        self.schedule.append(event)
        self.restriction.append(time)
        return self

    def overlap(self, event):
        """ Determines if event is in a players restriction. """
        for res in self.restriction:
            k = res & event
            if len(k) == 0:
                continue
            if k[0][1] - k[0][0] != 0:
                return True
        return False
