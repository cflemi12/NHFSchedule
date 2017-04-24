from openpyxl import load_workbook
from PlayerClass import Player
from TournamentClass import Tournament

""" Initalize a new tournament. """
nhf = Tournament()
field = []

""" Load kids data. """
wb = load_workbook("practice.xlsx", read_only=True, data_only=True)
ws = wb.active

""" Create players from data. """
for row in ws:
    name = str(row[0].value) + " " + str(row[1].value)
    division = str(row[2].value)
    hometown = str(row[3].value)
    school = str(row[4].value)
    anniversary = str(row[5].value).lower() in ['yes']
    sande = str(row[6].value).lower() in ['yes']
    citizen = str(row[7].value).lower() in ['yes']
    military = str(row[8].value).lower() in ['military']
    geography = str(row[9].value).lower() in ['geography']
    csaexam = str(row[10].value).lower in ['yes']
    bowl = str(row[11].value).lower() in ['yes']
    seed = str(row[12].value).lower()
    newplayer = Player(name, division, hometown, school, anniversary, sande, citizen, military, geography,
                       csaexam, bowl, seed, nhf)
    field.append(newplayer)

wb.close()


