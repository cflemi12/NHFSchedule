from TournamentClass import Tournament
from Scheduler import generateplayingfield, createpdfs, doscheduling
import time
from interval import interval

t0 = time.time()
# initialize a new tournament
nhf = Tournament()
field = generateplayingfield("practiceupdate.xlsx", nhf)
doscheduling(field, nhf)
createpdfs(field)


t = time.time() - t0
print "it took " + str(round(t, 2)) + " to complete"