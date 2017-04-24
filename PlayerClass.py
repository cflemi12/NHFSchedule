"""
Class for players.
@author: Chase Fleming
@date: 4/20/17

Defines a player in the NHF.

       Attributes:
           name - String of name of participant.
           division - String of Elementary, 7, or 8 grade.
           hometown - String of where the player is from.
           school - String of school they're representing.
           anniversary - Boolean for participating in the anniversary bee.
           sande - Boolean for participating in the sports and entertainment bee.
           citizen - Boolean for participating in the citizenship bee.
           military - Boolean for participating in the Subject Exam #1.
           geography - Boolean for participating in the Subject Exam #2.
           csaexam - Boolean for participating in the Citizenship, Sports, and Anniversary exam.
           bowl - Boolean for participating in the Bowl.
           seed - String representing seat seed. 
"""


class Player(object):

    """ Initiates the player. """

    def __init__(self, name, division, hometown, school, anniversary, sande, citizen, military, geography,
                 csaexam, bowl, seed, tournament, restriction=None):
        self.name = name
        self.division = division
        self.hometown = hometown
        self.school = school
        self.anniversary = anniversary
        self.sande = sande
        self.citizen = citizen
        self.military = military
        self.geography = geography
        self.csaexam = csaexam
        self.bowl = bowl
        self.seed = seed
        self.restriciton = restriction
        if restriction is None:
            self.restriciton = []
        self.schedule = []
        if bowl:
            for length in tournament.bowlschedule:
                self.restriciton.append(length)

    """ Returns the basic information of each player in a list. """

    def getinfo(self):
        return [self.name, self.division, self.hometown, self.school, self.anniversary, self.sande, self.citizen,
                self.military, self.geography, self.csaexam, self.bowl, self.seed]
