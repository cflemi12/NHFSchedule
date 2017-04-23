"""
Class for players.
@author: Chase Fleming
@date: 4/20/17
"""


class Player(object):
    """ Defines a player in the NHF.

        Attributes:
            name - String of name of participant.
            division - String of Elementary, 7, or 8 grade.
            hometown - String of where the player is from.
            school - String of school they're representing.
            anniversary - Boolean for participating in the anniversary side event.
            sande - Boolean for participating in the sports and entertainment bee.
            cit - Boolean for participating in the citizens exam.
            se1 - Boolean for participating in the Subject Exam #1.
            se2 - Boolean for participating in the Subject Exam #2.
            bowl - Boolean for participating in the Bowl.
            seed - String representing seat seed. 
    """

    def __init__(self, name, division, hometown, school, anniversary, sande, cit, se1, se2,
                 bowl, seed, restriction=None):
        self.name = name
        self.division = division
        self.hometown = hometown
        self.school = school
        self.anniversary = anniversary
        self.sande = sande
        self.cit = cit
        self.se1 = se1
        self.se2 = se2
        self.bowl = bowl
        self.seed = seed
        self.restriciton = restriction
        if restriction is None:
            self.restriciton = []
        self.schedule = []

    def getinfo(self):
        return [self.name, self.division, self.hometown, self.school, self.anniversary, self.sande, self.cit, self.se1,
                self.se2, self.bowl, self.seed]

