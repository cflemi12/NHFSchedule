from TournamentClass import Tournament
from Scheduler import generateplayingfield, createpdfs, doscheduling
import time
from interval import interval

t0 = time.time()

# initialize a new tournament
nhf = Tournament()
field = generateplayingfield("practiceupdate.xlsx", nhf)

doscheduling(field, nhf)
#createpdfs(field)

for f in field:
    print f.schedule

events = []
for h in nhf.examschedule:
    events.append(("History Bee Exam", h, None))




t = time.time() - t0
print "it took " + str(round(t, 2)) + " to complete"

