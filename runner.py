from TournamentClass import Tournament
from Scheduler import generateplayingfield, createpdfs, doscheduling
import time
from PlayerClass import *


def main():

    # reset unaccounted parameter
    zerocount()
    # initialize a new tournament
    nhf = Tournament()
    field = generateplayingfield("practiceupdate.xlsx", nhf)
    # schedule field in tournament
    doscheduling(field, nhf)

    # do it until there are no kids left unaccoutned
    while getcount() != 0:
        zerocount()
        # initialize a new tournament
        nhf = Tournament()
        field = generateplayingfield("practiceupdate.xlsx", nhf)
        # schedule field in tournament
        doscheduling(field, nhf)

    # generate PDFs
    #createpdfs(field)


if __name__ == "__main__":
    # track time
    t0 = time.time()
    main()
    # calculate length
    t = time.time() - t0
    print "it took " + str(round(t, 2)) + " to complete"