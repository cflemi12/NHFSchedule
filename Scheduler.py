"""
File for doing work of making the schedule.
@author Chase Fleming
4/23/17

File that includes heavy lifting functions. Does most of the work for scheduling.
"""

from openpyxl import load_workbook
from PlayerClass import Player
from FPDFClass import PDF
import random


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
        if str(row[0].value).lower() in ['none']:
            continue
        name = str(row[0].value) + " " + str(row[1].value)
        division = str(row[2].value)
        hometown = str(row[3].value)
        school = str(row[4].value)
        bee = str(row[5].value).lower() in ['yes']
        bowl = str(row[6].value).lower() in ['yes']
        anniversary = str(row[7].value).lower() in ['yes']
        sande = str(row[8].value).lower() in ['yes']
        citizen = str(row[9].value).lower() in ['yes']
        military = str(row[10].value).lower() in ['military']
        geography = str(row[11].value).lower() in ['geography']
        fqn = str(row[12].value).lower in ['yes']
        seed = str(row[13].value).lower()
        newplayer = Player(name, division, hometown, school, bee, bowl, anniversary, sande, citizen,
                           military, geography, fqn, seed, tournament)
        players.append(newplayer)

    # close workbook and return players
    wb.close()

    # remove headers from xlsx file
    players.pop(0)
    return players


def createpdfs(players):
    """Creates PDFs."""
    for player in players:
        pdf = PDF()
        pdf.set_fill_color(30, 60, 120)
        pdf.print_schedule(player.name, player.schedule)
        pdf.output('Schedules/' + player.name + '.pdf', 'F')


def doscheduling(field, tournament):
    """Does all the heavy lifting. Makes the schedule for each student."""

    field = list(map(lambda stu: stu.schedulemil(tournament), field))
    field = list(map(lambda stu: stu.schedulegeo(tournament), field))

    # filter side events
    """
    annplayers = list(filter(lambda stu: stu.anniversary is True, field))
    sandeplayers = list(filter(lambda stu: stu.sande is True, field))
    citplayers = list(filter(lambda stu: stu.citizen is True, field))
    for player in annplayers:
        time = random.choice(tournament.anniversaryschedule)
        while player.overlap(time):
            time = random.choice(tournament.anniversaryschedule)
        event = ("Anniversary Bee", time, None)
        player.schedule.append(event)
        player.restriction.append(time)
        time = random.choice(tournament.csaexamschedule)
        while player.overlap(time):
            time = random.choice(tournament.csaexamschedule)
        event = ("Anniversary Exam", time, None)
        player.schedule.append(event)
        player.restriction.append(time)

    for player in sandeplayers:
        time = random.choice(tournament.sandeschedule)
        while player.overlap(time):
            time = random.choice(tournament.sandeschedule)
        event = ("Sports and Entertainment Bee", time, None)
        player.schedule.append(event)
        player.restriction.append(time)
        time = random.choice(tournament.csaexamschedule)
        while player.overlap(time):
            print player.schedule
            print player.restriction
            time = random.choice(tournament.csaexamschedule)
        event = ("Sports and Entertainment Exam", time, None)
        player.schedule.append(event)
        player.restriction.append(time)
    """
    """
    for player in citplayers:
        time = random.choice(tournament.citizenschedule)
        while time in player.restriction:
            time = random.choice(tournament.citizenschedule)
        event = ("Citizenship Bee", time, None)
        player.schedule.append(event)
        player.restriction.append(time)
        time = random.choice(tournament.csaexamschedule)
        while time in player.restriction:
            print player.schedule
            time = random.choice(tournament.csaexamschedule)
        event = ("Citizenship Exam", time, None)
        player.schedule.append(event)
        player.restriction.append(time)
    """

    """
    #create elementary array of seeds
    elem = []
    for s in seeds:
        k = list(filter(lambda x: x.division == 'Elementary' and x.seed == s, field))
        elem.append(k)

    #create 7th grade array of seeds
    seven = []
    for s in seeds:
        k = list(filter(lambda x: x.division == '7' and x.seed == s, field))
        seven.append(k)

    #create 8th grade array of seeds
    eight = []
    for s in seeds:
        k = list(filter(lambda x: x.division == '8' and x.seed == s, field))
        eight.append(k)
    """
