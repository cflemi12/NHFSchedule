from TournamentClass import Tournament
from Scheduler import generateplayingfield, createpdfs

#initialize a new tournament
nhf = Tournament()
field = generateplayingfield("practice.xlsx", nhf)
createpdfs(field)