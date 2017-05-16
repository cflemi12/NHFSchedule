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
        pdf.set_fill_color(30, 60, 120)
        pdf.print_schedule(player.name, player.schedule, player.id, player.seed)
        pdf.output('Schedules/' + player.name + '.pdf', 'F')


def schedulebuz(field, tournament):
    """ Schedules the buzzer portion to the """
    seeds = [seed for seed in "abcdefghij"]
    divisions = ['8', '7', "Elementary"]
    friday = tournament.buzzerschedule[0:8]
    saturday = tournament.buzzerschedule[8:]
    divisiontotals = zip(divisions, [12, 9, 11])

    for div, tots in divisiontotals:
        for seed in seeds:
            print "Division: " + div + ", " + "Seed: " + seed
            players = list(filter(lambda stu: (stu.division == div) & (stu.seed == seed), field))
            tot = tots

            signedup = [0] * 8
            attemptschedule = list(
                map(lambda stu: stu.attemptschedulebuz(tournament, signedup, tot, friday), players))
            while len(filter(lambda ev: ev[0] is False, attemptschedule)) != 0:
                signedup = [0] * 8
                attemptschedule = list(
                    map(lambda stu: stu.attemptschedulebuz(tournament, signedup, tot, friday), players))
            for attempt, player, schedule in attemptschedule:
                player.updateschedule(schedule)

            attemptschedule = list(
                map(lambda stu: stu.attemptschedulebuz(tournament, signedup, tot, saturday), players))
            while len(filter(lambda ev: ev[0] is False, attemptschedule)) != 0:
                signedup = [0] * 8
                attemptschedule = list(
                    map(lambda stu: stu.attemptschedulebuz(tournament, signedup, tot, saturday), players))
            for attempt, player, schedule in attemptschedule:
                player.updateschedule(schedule)


def doscheduling(field, tournament):
    """Does all the heavy lifting. Makes the schedule for each student."""
    print "Scheduling Military Exams."
    map(lambda stu: stu.schedulemil(tournament), field)
    print "Scheduling Geography Exams."
    map(lambda stu: stu.schedulegeo(tournament), field)
    print "Scheduling Side Events."
    map(lambda stu: stu.schedulecit(tournament), field)
    map(lambda stu: stu.schedulesae(tournament), field)
    print "Scheduling Buzzer rounds for..."
    #schedulebuz(field, tournament)
    print "Scheduling Exams."
    map(lambda stu: stu.scheduleexm(tournament), field)

    print "Setting Exam Rooms."
    tournament.scheduleexamrooms(field)
    print "Setting Side Event Rooms."
    # tournament.schedulesiderooms(field)
    print "Setting Buzzer Rooms."
    # tournament.schedulebuzzerrooms(field)
