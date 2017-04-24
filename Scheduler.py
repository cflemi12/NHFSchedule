"""
File for doing work of making the schedule.
@author Chase Fleming
4/23/17

File that includes heavy lifting functions. Does most of the work for scheduling.
"""

from openpyxl import load_workbook
from PlayerClass import Player
from FPDFClass import PDF


def generateplayingfield(info, tournament):
    """Generates the playing field given the raw data.
    Gets passed the file name and the tournament.
    """

    # load workbook data
    players = []
    wb = load_workbook(info, read_only=True, data_only=True)
    ws = wb.active

    # construct players from each row value
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
                           csaexam, bowl, seed, tournament)
        players.append(newplayer)

    # close workbook and return players
    wb.close()

    # remove headers from xlsx file
    players.pop(0)
    return players


def createpdfs(players):
    for player in players:
        pdf = PDF()
        pdf.print_schedule(player.name, player.schedule)
        pdf.output('Schedules/' + player.name + '.pdf', 'F')
