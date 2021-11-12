# Author: Mark Olson 2021-11-06 https://github.com/Mark-MDO47/PrisonDilemmaTourney
#
# PrisonersDilemmaTournament.py will run a tournament for Prisoner's Dilemma algorithms.
# The algorithms are of the form displayed in algo_mdo_template.py
#
# PrisonersDilemmaTournament.py receives a text string with the path to two algorithm python routines
# For an algorithm python routine in a file (i.e. with filename algo_mdo.py), the calling sequence is
#     choice = algo_mdo(myChoices, oppChoices)
#     NOTE that the function name is the same as the python filename with the "*.py" removed
#     I recommend adding your initials (mine are mdo) to your file/algorithm name so we don't have name collisions
# Each call to the algorithm will have the following for parameters:
#     list of history all the choices made by both parties in reverse order (latest choice before this is [0], prev [1])
#       Thus the opponent choice made in previous round, assuming this isn't the first round, is oppChoices[0].
#          if len(oppChoices) > 0, there was at least one prior round.
#       note: len(oppChoices) should be identical to len(myChoices)
#     value of each entry is one of value.DEFECT or value.COOPERATE
# The algorithm will return
#     value.DEFECT or value.COOPERATE
#     NOTE: in PrisonersDilemmaTournament.py (this file), these are just DEFECT or COOPERATE.
#           Algorithm files contain "import PrisonersDilemmaTournament as values" so they refer to these as
#           value.DEFECT or value.COOPERATE
#
# See https://en.wikipedia.org/wiki/Prisoner%27s_dilemma
# See https://cs.stanford.edu/people/eroberts/courses/soco/projects/1998-99/game-theory/axelrod.html
#
# Merrill Flood and Melvin Dresher from RAND corporation framed the concept in 1950 to show why two completely rational
#   individuals might not cooperate, even if it appears that it is in their best interests to do so.
#
# There are many scenarios that can be mapped to this concept, but the famous mapping by Albert W. Tucker called the
#   "Prisoner's Dilemma" revolves around two prisoners, "A" and "B", guilty of the same crime and being held in
#   separate interrogation rooms.
#
# Due to weak evidence held by the police, if both cooperate (do not betray the other), that will lead to a small sentence
#   for each of them. If one cooperates and the other defects, the defector gets off free and the cooperator gets a
#   large sentence. If they both defect, they both get an intermediate sentence.
# (spoiler alert) If the game is played exactly one time, the game-theory best choice for each player is to
#   defect (or betray the other player).
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
import os

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
RESULT_D_C = 0
RESULT_C_C = 1
RESULT_D_D = 5
RESULT_C_D = 10

###################################################################################
# get_algos - do directory and return information and funcptr to algorithms
#
# algorithms are implemented in algo_<<<initials>>>_<<<algorithm_name>>>.py
#
# returns sorted list of algorithm names and algorithm funcptrs
def get_algos():
    flist = sorted(os.listdir("."))
    algolist = []
    for fname in flist:
        if (0 == fname.find("algo_")) and (".py" == fname[-len(".py"):]):
            algolist.append(fname[:-len(".py")])
    algofunc = []
    for algo in algolist:
        algofunc.append(getattr(importlib.import_module(algo), algo))
    return algolist, algofunc

    # end get_algos()

###################################################################################
# calcResult - calculate the results of a round for one player
#
def calcResult(selfChoice, oppChoice):
    the_result = 0
    if (DEFECT == selfChoice) and (DEFECT == oppChoice):
        the_result = RESULT_D_D
    elif (COOPERATE == selfChoice) and (COOPERATE == oppChoice):
        the_result = RESULT_C_C
    elif (DEFECT == selfChoice) and (COOPERATE == oppChoice):
        the_result = RESULT_D_C
    elif (COOPERATE == selfChoice) and (DEFECT == oppChoice):
        the_result = RESULT_C_D
    return the_result

    # end calcResult()

###################################################################################
# doTournament - conducts a round-robin tournament among algorithms found in "."
#
# Tournament includes competing each algorithm against itself
#
def doTournament(number_of_iterations):
    algolist, algofunc = get_algos()

    results = [0]*len(algolist)
    for idx1 in range(len(algolist)):
        for idx2 in range(idx1, len(algolist)):
            selfHist1 = []
            selfHist2 = []
            for idx3 in range(number_of_iterations):
                choice1 = algofunc[idx1](selfHist1,selfHist2)
                choice2 = algofunc[idx2](selfHist2,selfHist1)
                selfHist1 = [choice1] + selfHist1 # latest choice is always [0]
                selfHist2 = [choice2] + selfHist2
                results[idx1] += calcResult(choice1, choice2)
                results[idx2] += calcResult(choice2, choice1)

            print("\nRound\t%s\t%s\t" % (algolist[idx1], algolist[idx2]))
            maxHist_m1 = len(selfHist1) - 1
            for idx in range(maxHist_m1 + 1):
                print("%d\t%s\t%s\t" % (1+idx, TEXT_INTERP[selfHist1[maxHist_m1 - idx]], TEXT_INTERP[selfHist2[maxHist_m1 - idx]]))

    print("\n\nResults of Prisoner's Dilemma Tournament: %d rounds, params: D_D=%d C_C=%d D_C=%d C_D=%d" % \
          (number_of_iterations, RESULT_D_D, RESULT_C_C, RESULT_D_C, RESULT_C_D))
    print("\nAlgorithm\tTotalScore")
    for idx1 in range(len(algolist)):
        print("%s\t%s" % (algolist[idx1], results[idx1]))

    # end doTournament()


###################################################################################
# "__main__" processing for PrisonersDilemmaTournament
#
# use argparse to process command line arguments
# python PrisonersDilemmaTournament.py -h to see what the arguments are
#
if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(prog='PrisonersDilemmaTournament',
        formatter_class=argparse.RawTextHelpFormatter,
        description="stdout receives tab-separated-values results of algo1 and algo2\n",
        epilog="""Example:
python PrisonersDilemmaTournament.py number_of_iterations > formattedResults.txt
""",
        usage='python %(prog)s number_of_iterations\n' +
              "   note: runs all files algo_*.py in directory\n" +
              "   note: algo_*.py written per algo_mdo_template.py")
    my_parser.add_argument('number_of_iterations',type=int,help='number of iterations to run')
    args = my_parser.parse_args()

    # all the real work is done here
    doTournament(args.number_of_iterations)

    # end of "__main__"
