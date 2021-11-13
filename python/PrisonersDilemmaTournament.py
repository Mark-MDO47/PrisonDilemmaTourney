# Author: Mark Olson 2021-11-06 https://github.com/Mark-MDO47/PrisonDilemmaTourney
#
# PrisonersDilemmaTournament.py will run a tournament for Prisoner's Dilemma algorithms.
# The algorithms are of the form displayed in algo_mdo_template.py
#
# PrisonersDilemmaTournament.py gets its algorithms by searching the current directory for algo_*.py.
#     I recommend adding your initials (mine are mdo) to your file/algorithm name so we don't have name collisions.
#     For example: algo_mdo_something.py
#
# For an algorithm python routine in a file (i.e. with filename algo_mdo_something.py), the calling sequence is
#     choice = algo_mdo_something(myChoices, oppChoices)
#     NOTE that the function name is the same as the python filename with the "*.py" removed
# Each call to the algorithm will have the following parameters:
#     list of history all the choices made by both parties in reverse order (latest choice before this is [0], prev [1])
#       Thus the opponent choice made in previous round, assuming this isn't the first round, is oppChoices[0].
#          if len(oppChoices) > 0, there was at least one prior round.
#       note: len(oppChoices) should be identical to len(myChoices)
#     value of each entry is one of choices.DEFECT or choices.COOPERATE
# The algorithm will return
#     choices.DEFECT or choices.COOPERATE
#     NOTE: in PrisonersDilemmaTournament.py (this file), these are just DEFECT or COOPERATE.
#           Algorithm files contain "import PrisonersDilemmaTournament as choices" so they refer to these as
#           choices.DEFECT or choices.COOPERATE
#
# See https://en.wikipedia.org/wiki/Prisoner%27s_dilemma
# See https://cs.stanford.edu/people/eroberts/courses/soco/projects/1998-99/game-theory/axelrod.html
# See https://www.pnas.org/content/109/26/10409
# See https://ncase.me/trust/
#
# Merrill Flood and Melvin Dresher from RAND corporation framed the concept in 1950 to show why two completely
#   rational individuals might not cooperate, even if it appears that it is in their best interests to do so.
#
# There are many scenarios that can be mapped to this concept, but the famous mapping by Albert W. Tucker called
#   the "Prisoner's Dilemma" revolves around two prisoners, "A" and "B", guilty of the same crime and being held in
#   separate interrogation rooms.
#
# Due to weak evidence held by the police, if both choose to cooperate (C) (refuse to defect (D)) that will lead to
#    an intermediate sentence R for each of them. If one chooses to cooperate and the other chooses to defect,
#    the defector gets a very low sentence T (usually zero) and the cooperator gets a large sentence S. If they both
#    choose to defect, they both get an intermediate sentence P.
# In my "sentence" formulation for a Prisoner's Dilemma (instead of the "reward" formulation),
#    S > P > R > T. Because P > R, mutual cooperation pays off better than mutual defection.
# If the game is played only once, the game-theoretic best response for each player is to defect
#    (betray the other person).
#
# Personally, I find this S > P > R > T nomenclature a little hard to remember.
#    I think of it (and the code refers to it) as the result a self-choice and an opponent-choice.
#    Thinking of one of the participants as self and the other as opponent, here are the results as
#    self-choice_opponent-choice:
#        C_D = S = I nobly cooperate but my dastardly opponent defects
#        D_D = P = I reluctantly follow my short-term best interests and defect and my dastardly opponent
#                    self-interestedly defects too
#        C_C = R = I nobly cooperate and my opponent probably slips and chooses to cooperate too
#        D_C = T = I slyly defect and my naive opponent cooperates
#
# Robert Axelrod, professor of political science at the University of Michigan, had the insight that if the game
#    is played many times in succession, then the history of play allows each player to take into account the
#    "reputation" of the other player in making their choice of behavior. He held tournaments of competing strategies
#    for the Prisoner's Dilemma starting in 1980, and this led to a great deal of research.
# The "Tit-For-Tat" algorithm seemed to do the best. Later it was found that there are scenarios where other
#    algorithms can do as well or better.
#

import argparse
import importlib
import random
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

# for results, T > R > P > S and T + S < 2R
CALC_RESULT_RANGES = { "001-Classical Range": [0,1,3,5], "002-Extended Range": [0,1,5,10] }
IDX_RESULT_D_C = 0 # "S" in literature
IDX_RESULT_C_C = 1 # "R" in literature
IDX_RESULT_D_D = 2 # "P" in literature
IDX_RESULT_C_D = 3 # "T" in literature

###################################################################################
# calcResult - calculate the results of a round for one player
#
def calcResult(range, selfChoice, oppChoice):
    the_result = 0
    D_C = CALC_RESULT_RANGES[range][IDX_RESULT_D_C]
    C_C = CALC_RESULT_RANGES[range][IDX_RESULT_C_C]
    D_D = CALC_RESULT_RANGES[range][IDX_RESULT_D_D]
    C_D = CALC_RESULT_RANGES[range][IDX_RESULT_C_D]
    if (DEFECT == selfChoice) and (DEFECT == oppChoice):
        the_result = D_D
    elif (COOPERATE == selfChoice) and (COOPERATE == oppChoice):
        the_result = C_C
    elif (DEFECT == selfChoice) and (COOPERATE == oppChoice):
        the_result = D_C
    elif (COOPERATE == selfChoice) and (DEFECT == oppChoice):
        the_result = C_D
    return the_result, (D_C, C_C, D_D, C_D)

    # end calcResult()

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
# whoopsie - insert "real world" errors into choices
#
whoopsie_count = 0
whoopsie_checkit = [DEFECT, COOPERATE]
def whoopsie(result1, result2, mistake_percent):
    global whoopsie_count

    whoopsie_count += 1
    if (result1 not in whoopsie_checkit) or (result2 not in whoopsie_checkit):
        print("ERROR: input to whoopsie is %d %d on count %d" % (result1, result2, whoopsie_count))
        exit()
    if random.random() < mistake_percent:
        result1 = 1-result1
        # print("DEBUG whoopsie   change result1=%d %0.0f" % (result1, 100*mistake_percent))
    else:
        # print("DEBUG whoopsie nochange result1=%d %0.0f" % (result1, 100*mistake_percent))
        pass
    if random.random() < mistake_percent:
        result2 = 1-result2
        # print("DEBUG whoopsie   change result2=%d %0.0f" % (result2, 100 * mistake_percent))
    else:
        # print("DEBUG whoopsie nochange result2=%d %0.0f" % (result2, 100 * mistake_percent))
        pass
    return result1, result2

    # end whoopsie()

###################################################################################
# print_results - print results
#
def print_results(title, algolist, num_rounds, mistake_percent, percent_symb, reward_key, rslttbl, results_type):
    print("\n\n%s Results of Prisoner's Dilemma Tournament: %s rounds, %s%s mistakes, ResultsTbl=%s: D_D=%s C_C=%s D_C=%s C_D=%s" % \
        (title, num_rounds, mistake_percent, percent_symb, reward_key,
         rslttbl[IDX_RESULT_D_C], rslttbl[IDX_RESULT_C_C], rslttbl[IDX_RESULT_D_D], rslttbl[IDX_RESULT_C_D]))
    print("Algorithm\tTotalScore")
    for idx1 in range(len(algolist)):
        print("%s\t%s" % (algolist[idx1], results_type[idx1]))

    # end print_results()

###################################################################################
# doTournament - conducts a round-robin tournament among algorithms found in "."
#
# Tournament includes competing each algorithm against itself
#
def doTournament():
    rounds_ranges = [ 3, 5, 10, 20, 50, 100 ]
    mistake_percentages_list = [ 0.0, 0.05, 0.10, 0.15, 0.20, 0.25 ]

    # get the algorithms in the directory
    algolist, algofunc = get_algos()
    results_rewards_keys = sorted(CALC_RESULT_RANGES.keys())

    # do the tournament over the various ranges
    results_overall = [0]*len(algolist)
    for mistake_percent in mistake_percentages_list:
        results_mistakes = [0] * len(algolist)
        for reward_key in results_rewards_keys:
            results_rewardstbl = [0] * len(algolist)
            for num_rounds in rounds_ranges:

                # now do pairing of two algorithms
                results_pairing = [0] * len(algolist)
                for idx1 in range(len(algolist)):
                    for idx2 in range(idx1, len(algolist)):
                        selfHist1 = []
                        selfHist2 = []
                        for idx3 in range(num_rounds):
                            choice1 = algofunc[idx1](selfHist1,selfHist2)
                            choice2 = algofunc[idx2](selfHist2,selfHist1)
                            choice1, choice2 = whoopsie(choice1, choice2, mistake_percent)

                            selfHist1 = [choice1] + selfHist1 # latest choice is always [0]
                            selfHist2 = [choice2] + selfHist2
                            result1, rlsttbl = calcResult(reward_key, choice1, choice2)
                            result2, rslttbl = calcResult(reward_key, choice2, choice1)

                            results_overall[idx1] += result1
                            results_overall[idx2] += result2
                            results_mistakes[idx1] += result1
                            results_mistakes[idx2] += result2
                            results_rewardstbl[idx1] += result1
                            results_rewardstbl[idx2] += result2
                            results_pairing[idx1] += result1
                            results_pairing[idx2] += result2

                        print("\nRound\t%s\t%s\t%s%s mistakes\tResultsTbl=%s: D_D=%s C_C=%s D_C=%s C_D=%s" % \
                              (algolist[idx1], algolist[idx2], mistake_percent, "%", reward_key,
                               rslttbl[IDX_RESULT_D_C], rslttbl[IDX_RESULT_C_C], rslttbl[IDX_RESULT_D_D],
                               rslttbl[IDX_RESULT_C_D]))
                        maxHist_m1 = len(selfHist1) - 1
                        for idx in range(maxHist_m1 + 1):
                            print("%d\t%s\t%s\t" % (1+idx, TEXT_INTERP[selfHist1[maxHist_m1 - idx]], TEXT_INTERP[selfHist2[maxHist_m1 - idx]]))

                print_results("Pairing", algolist, num_rounds, "%0.0f" % (100.0*mistake_percent), "%", reward_key, rslttbl, results_pairing)
            print_results("RewardsTable", algolist, "N/A", "%0.0f" % (100.0*mistake_percent), "%", reward_key, rslttbl, results_rewardstbl)
        print_results("Mistakes", algolist, "N/A", "%0.0f" % (100.0*mistake_percent), "%", "N/A", ("N/A", "N/A", "N/A", "N/A"), results_mistakes)
    print_results("Overall", algolist, "N/A", "N/A", "", "N/A", ("N/A", "N/A", "N/A", "N/A"), results_overall)
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
python PrisonersDilemmaTournament.py > formattedResults.txt
""",
        usage='python %(prog)s randseed\n' +
              "   note: runs all files algo_*.py in directory\n" +
              "   note: algo_*.py written per algo_mdo_template.py")
    my_parser.add_argument('randseed', type=str, help='if integer, seed for random number; else random seed')
    args = my_parser.parse_args()

    if args.randseed[0].isdigit():
        random.seed(int(args.randseed))
    else:
        random.seed(42) # FIXME - random seed, maybe based on time

    # all the real work is done here
    doTournament()

    # end of "__main__"
