from TournamentClass import Tournament
from Scheduler import generateplayingfield, createpdfs, doscheduling, createscoresheets, createmasters
import time
import PlayerClass
import copy
from openpyxl import Workbook




def main():

    # initialize a new tournament
    nhf = Tournament()
    originalfield = generateplayingfield("Final.xlsx", nhf)
    field = copy.deepcopy(originalfield)

    # schedule field in tournament
    doscheduling(field, nhf)

    # do it until there are no kids left not fully scheduled
    while PlayerClass.failed != 0:
        print "Number of students not able to scheduled: " + str(PlayerClass.failed)
        print "Failed configuration."
        # reset number of kids not fully scheduled
        PlayerClass.failed = 0
        # initialize a new tournament
        del nhf
        nhf = Tournament()
        del field
        field = copy.deepcopy(originalfield)
        # schedule field in tournament
        doscheduling(field, nhf)

    print "Good configuration."


    # generate PDFs
    #createpdfs(field)

    # create scoresheets
    #createscoresheets(nhf)

    # create master schedules
    createmasters(field, nhf)


if __name__ == "__main__":
    # track time
    t0 = time.time()
    main()
    # calculate length
    t = time.time() - t0
    print "Done."
    print "it took " + str(round(t, 2)) + " to complete."
