from TournamentClass import Tournament
from Scheduler import generateplayingfield, createpdfs

# initialize a new tournament
nhf = Tournament()
field = generateplayingfield("practiceupdate.xlsx", nhf)
createpdfs(field)
