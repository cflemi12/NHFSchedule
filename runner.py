from TournamentClass import Tournament
from Scheduler import generateplayingfield, createpdfs, doscheduling

# initialize a new tournament
nhf = Tournament()
field = generateplayingfield("practiceupdate.xlsx", nhf)
doscheduling(field, nhf)
count = 0
#createpdfs(field)
