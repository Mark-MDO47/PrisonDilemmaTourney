# Author: Mark Olson 2021-11-06 https://github.com/Mark-MDO47/PrisonDilemmaTourney
#
# PrisonersDilemmaTournament.py will run a tournament for Prisoner's Dilemma algorithms.
# The algorithms are of the form displayed in algorithm_template.py
#
# PrisonersDilemmaTournament.py receives a text string with the path to two algorithm python routines
# For an algorithm python routine in file algo.py, the calling sequence is
#     choice = algo(myChoices, oppChoices)
# Each call to the algorithm will have the following for parameters:
#     list of history all the choices made by both parties in reverse order (latest choice before this is [0], prev [1])
#       note: len(oppChoices) should be identical to len(myChoices); zero for first call, one for second call
#     value of each entry is one of DEFECT or COOPERATE
# The algorithm will return
#     DEFECT or COOPERATE
#
# See https://en.wikipedia.org/wiki/Prisoner%27s_dilemma
# See https://cs.stanford.edu/people/eroberts/courses/soco/projects/1998-99/game-theory/axelrod.html
#
# Merrill Flood and Melvin Dresher from RAND corporation framed the concept in 1950 to show why two completely rational
#   individuals might not DEFECT, even if it appears that it is in their best interests to do so.
#
# There are many scenarios that can be mapped to this concept, but the famous mapping by Albert W. Tucker called the
#   "Prisoner's Dilemma" revolves around two prisoners, "A" and "B", guilty of the same crime and being held in
#   separate interrogation rooms.
#
# Due to weak evidence held by the police, if both refuse to DEFECT the other that will lead to a very small sentence
#   for each of them. If one stays silent and the other DEFECTs, the DEFECTer gets off free and the silent one gets a
#   large sentence. If they both DEFECT each other, they both get an intermediate sentence.
# (spoiler alert) If the game is played exactly one time, the game-theory best choice for each player is to
#   DEFECT the other player.
#
# Robert Axelrod, professor of political science at the University of Michigan, held a tournament of competing
# strategies for the famous Prisoner's Dilemma in 1980.
#
# He had the insight that if the game is played many times in succession, then the history of play allows each player
#   to take into account the "reputation" of the other player in making their choice of behavior.
# He invited some game theorists to submit algorithms that would be competed against each other in a computer tournament.
# Later he held another tournament and invited anyone to submit algorithms.
# The "Tit-For-Tat" algorithm seemed to do the best.

import argparse
import importlib
"""
import sys
import string
import os
import pandas as pd
import datetime
"""

DEFECT    = 0
COOPERATE = 1
TEXT_INTERP = ["DEFECT", "COOPERATE"]


def convert_to_strings(algo):
    # get just the module name
    tmp = algo.rfind("\\")
    if -1 != tmp:
        algo = algo[tmp + 1:]
    tmp = algo.rfind("/")
    if -1 != tmp:
        algo = algo[tmp + 1:]
    tmp = algo.rfind(".py")
    if -1 != tmp:
        algo = algo[:tmp]

    return algo

def doTournament(number_of_iterations, algo1, algo2):
    # print("DEBUG ", number_of_iterations, algo1, algo2)
    selfHist1 = [] # do not put these on same line all "=" together
    selfHist2 = []
    import_algo1 = convert_to_strings(algo1)
    import_algo2 = convert_to_strings(algo2)
    # print("DEBUG ", import_algo1)

    algotype1 = importlib.import_module(import_algo1)
    algofunc1 = getattr(algotype1, import_algo1)
    algotype2 = importlib.import_module(import_algo2)
    algofunc2 = getattr(algotype2, import_algo2)
    # print("DEBUG ", type(algotype1))

    for idx in range(number_of_iterations):
        choice1 = algofunc1(selfHist1,selfHist2)
        choice2 = algofunc2(selfHist2,selfHist1)
        selfHist1 = [choice1] + selfHist1 # latest choice is always [0]
        selfHist2 = [choice2] + selfHist2

    print("Round\t%s\t%s\t" % (algo1, algo2))
    for idx in range(len(selfHist1)):
        print("%d\t%s\t%s\t" % (idx, TEXT_INTERP[selfHist1[idx]], TEXT_INTERP[selfHist2[idx]]))



###################################################################################
# "__main__" processing for PrisonersDilemmaTournament
#
# use argparse to process command line arguments
# python PrisonersDilemmaTournament.py -h to see what the arguments are
#
if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(prog='PrisonersDilemmaTournament',
        formatter_class=argparse.RawTextHelpFormatter,
        description="stdout receives tab-separated-values results of algo1 and algo2\n" +
                "   note: ok to have algo1 and algo2 be the same",
        epilog="""Example:
python PrisonersDilemmaTournament.py number_of_iterations algo1.py algo2.py > formattedList.txt
""",
        usage='%(prog)s listFname prevRatingsFname')
    my_parser.add_argument('number_of_iterations',type=int,help='number of iterations to run')
    my_parser.add_argument('algo1',type=str,help='path to algorithm1.py code')
    my_parser.add_argument('algo2',type=str,help='path to algorithm2.py code')
    args = my_parser.parse_args()

    # all the real work is done here
    doTournament(args.number_of_iterations, args.algo1, args.algo2)

    # end of "__main__"
