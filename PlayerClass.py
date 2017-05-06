"""
Class for players.
@author: Chase Fleming
@date: 4/20/17

Defines a player in the NHF.
"""


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
    """

    def __init__(self, name, division, hometown, school, bee, bowl, anniversary, sande, citizen, military,
                 geography, csaexam, fqn, seed, tournament, restriction=None):
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
        self.csaexam = csaexam
        self.fqn = fqn
        self.seed = seed
        self.restriction = restriction

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
                self.military, self.geography, self.csaexam, self.bowl, self.seed]
