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
    """
    Generates the playing field given the raw data.
    Gets passed the file name and the tournament.
    """

    # load workbook data
    print "Loading workbook data."
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
        anniversary = str(row[5].value).lower() in ['yes']
        sande = str(row[6].value).lower() in ['yes']
        citizen = str(row[7].value).lower() in ['yes']
        military = str(row[8].value).lower() in ['military']
        geography = str(row[9].value).lower() in ['geography']
        fqn = str(row[10].value).lower in ['yes']
        bowl = str(row[11].value).lower() in ['yes']
        bee = str(row[12].value).lower() in ['yes']
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
    print "Creating PDFs."
    for player in players:
        pdf = PDF()
        pdf.print_schedule(player.name, player.schedule, player.id, player.seed)
        pdf.output('/Users/chasefleming/PycharmProjects/NHFSchedule/output/Schedules/' + player.name + '.pdf', 'F')


def schedulebuz(field, tournament):
    """ Schedules the buzzer portion to the """
    field = list(filter(lambda stu: stu.bee, field))
    seeds = [seed for seed in "abcdefghij"]
    divisions = ['8', '7', "Elementary"]
    friday = tournament.buzzerschedule[0:8]
    saturday = tournament.buzzerschedule[8:]
    eig = [12, 12, 12, 12, 12, 12, 12, 12]
    sev = [9, 9, 9, 9, 9, 9, 9, 9]
    elm = [10, 11, 10, 11, 10, 11, 10, 11]
    divisiontotals = zip(divisions, [eig, sev, elm])

    for div, tots in divisiontotals:
        print "Division: " + div
        for seed in seeds:
            players = list(filter(lambda stu: (stu.division == div) & (stu.seed == seed), field))

            signedup = [0] * 8
            attemptschedule = list(
                map(lambda stu: stu.attemptschedulebuz(signedup, tots, friday), players))
            while not all(ev[0] for ev in attemptschedule):
                signedup = [0] * 8
                attemptschedule = list(
                    map(lambda stu: stu.attemptschedulebuz(signedup, tots, friday), players))
            for attempt, player, schedule in attemptschedule:
                player.updateschedule(schedule)

            attemptschedule = list(
                map(lambda stu: stu.attemptschedulebuz(signedup, tots, saturday), players))
            while not all(ev[0] for ev in attemptschedule):
                signedup = [0] * 8
                attemptschedule = list(
                    map(lambda stu: stu.attemptschedulebuz(signedup, tots, saturday), players))
            for attempt, player, schedule in attemptschedule:
                player.updateschedule(schedule)


def doscheduling(field, tournament):
    """Does all the heavy lifting. Makes the schedule for each student."""
    print "Scheduling Military Exams."
    #map(lambda stu: stu.schedulemil(tournament), field)
    print "Scheduling Geography Exams."
    #map(lambda stu: stu.schedulegeo(tournament), field)
    print "Scheduling Side Events."
    #map(lambda stu: stu.schedulecit(tournament), field)
    #map(lambda stu: stu.schedulesae(tournament), field)
    print "Scheduling Buzzer rounds for..."
    schedulebuz(field, tournament)
    print "Scheduling Exams."
    #map(lambda stu: stu.scheduleexm(tournament), field)

    print "Setting Exam Rooms."
    #tournament.scheduleexamrooms(field)
    print "Setting Side Event Rooms."
    #tournament.schedulesiderooms(field)
    print "Setting Buzzer Rooms."
    tournament.schedulebuzzerrooms(field)
