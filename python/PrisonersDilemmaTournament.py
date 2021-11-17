# Author: Mark Olson 2021-11-06 https://github.com/Mark-MDO47/PrisonDilemmaTourney
#
# PrisonersDilemmaTournament.py will run a tournament for Prisoner's Dilemma algorithms.
# The algorithms are of the form displayed in algo_mdo_template.py
# The profile of parameters to explore are stored in a file of the form prof_mdo_template.yaml
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
#       Thus the opponent choice made in previous move, assuming this isn't the first move, is oppChoices[0].
#          if len(oppChoices) > 0, there was at least one prior move.
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
import time
import os
import sys
import yaml

"""
import string
import pandas as pd
import datetime
"""

DEFECT    = 0
COOPERATE = 1
TEXT_INTERP = ["DEFECT", "COOPERATE"]

# for results, T > R > P > S and T + S < 2R
IDX_RESULT_D_C = 0 # "S" in literature
IDX_RESULT_C_C = 1 # "R" in literature
IDX_RESULT_D_D = 2 # "P" in literature
IDX_RESULT_C_D = 3 # "T" in literature
REWARDS_DICT = {}
NUM_MOVES_LIST = []
MISTAKE_PERCENTAGES_LIST = []
WHOOPSIE_MARKER = "*"

###################################################################################
# calcResult - calculate the results for one player of a move
#
# D_C is my result if I defect and my opponent cooperates    ("S" in literature)
# C_C is my result if I cooperate and my opponent cooperates ("R" in literature)
# D_D is my result if I defect and my opponent defects       ("P" in literature)
# C_D is my result if I cooperate and my opponent defects    ("T" in literature)
#
def calcResult(range, selfChoice, oppChoice):
    the_result = 0
    D_C = REWARDS_DICT[range][IDX_RESULT_D_C]
    C_C = REWARDS_DICT[range][IDX_RESULT_C_C]
    D_D = REWARDS_DICT[range][IDX_RESULT_D_D]
    C_D = REWARDS_DICT[range][IDX_RESULT_C_D]
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
def whoopsie(choice1, choice2, mistake_percent):
    global whoopsie_count
    whoopsie_checkit = [DEFECT, COOPERATE]

    whoopsie_count += 1
    if (choice1 not in whoopsie_checkit) or (choice2 not in whoopsie_checkit):
        print("ERROR: input to whoopsie is %d %d %0.2f on count %d" % (choice1, choice2, mistake_percent, whoopsie_count))
        exit()
    try1 = random.random()
    if try1 < mistake_percent:
        choice1 = 1-choice1
        # print("DEBUG whoopsie   change choice1=%d try1 %0.2f mistake %0.0f" % (choice1, try1, 100*mistake_percent))
    else:
        # print("DEBUG whoopsie nochange choice1=%d try1 %0.2f mistake %0.0f" % (choice1, try1, 100*mistake_percent))
        pass
    try2 = random.random()
    if try2 < mistake_percent:
        choice2 = 1-choice2
        # print("DEBUG whoopsie   change choice2=%d try2 %0.2f mistake %0.0f" % (choice2, try2, 100 * mistake_percent))
    else:
        # print("DEBUG whoopsie nochange choice2=%d try2 %0.2f mistake %0.0f" % (choice2, try2, 100 * mistake_percent))
        pass
    return choice1, choice2

    # end whoopsie()

###################################################################################
# print_scores - print results
#
def print_scores(title, algolist, num_moves, mistake_percent, percent_symb, rand_seed, reward_key, rslttbl, results_type):
    print("\n\n%s Results of Prisoner's Dilemma Tournament: %s moves, %s%s mistakes (seed %s), ResultsTbl=%s: D_D=%s C_C=%s D_C=%s C_D=%s" % \
        (title, num_moves, mistake_percent, percent_symb, rand_seed, reward_key,
         rslttbl[IDX_RESULT_D_C], rslttbl[IDX_RESULT_C_C], rslttbl[IDX_RESULT_D_D], rslttbl[IDX_RESULT_C_D]))
    print("Algorithm\tTotalScore")
    for idx1 in range(len(algolist)):
        print("%s\t%s" % (algolist[idx1], results_type[idx1]))

    # end print_scores()

###################################################################################
# doReadParms - read the tournament parameters from a YAML file
#
def doReadParms(fname):
    global REWARDS_DICT
    global NUM_MOVES_LIST
    global MISTAKE_PERCENTAGES_LIST
    global WHOOPSIE_MARKER

    with open(fname, 'rt') as stream:
        data_loaded = yaml.safe_load(stream)

    REWARDS_DICT = data_loaded["REWARDS_DICT"]
    NUM_MOVES_LIST = data_loaded["NUM_MOVES_LIST"]
    MISTAKE_PERCENTAGES_LIST = data_loaded["MISTAKE_PERCENTAGES_LIST"]
    WHOOPSIE_MARKER = data_loaded["WHOOPSIE_MARKER"]

    # end doReadParms()

###################################################################################
# doTournament - conducts a round-robin tournament among algorithms found in "."
#
# Tournament includes competing each algorithm against itself
#
def doTournament(rand_seed, print_detail):

    # get the algorithms in the directory
    algolist, algofunc = get_algos()
    rewards_keys = sorted(REWARDS_DICT.keys())

    # do the tournament over the various ranges
    scores_overall = [0]*len(algolist)
    for mistake_percent in MISTAKE_PERCENTAGES_LIST:
        scores_mistakes = [0] * len(algolist)
        for this_reward_key in rewards_keys:
            scores_rewardstbl = [0] * len(algolist)
            for num_moves in NUM_MOVES_LIST:

                # now do pairing of two algorithms
                scores_pairing = [0] * len(algolist)
                for idx1 in range(len(algolist)):
                    for idx2 in range(idx1, len(algolist)):
                        selfHist1 = []
                        selfHist2 = []
                        selfScore1 = []
                        selfScore2 = []
                        origHist1 = []
                        origHist2 = []
                        for idx3 in range(num_moves):
                            orig_choice1 = algofunc[idx1](selfHist1,selfHist2)
                            orig_choice2 = algofunc[idx2](selfHist2,selfHist1)
                            choice1, choice2 = whoopsie(orig_choice1, orig_choice2, mistake_percent)

                            # print("DEBUG doTournament: orig_choice1 %s choice1 %s" % (orig_choice1, choice1))
                            # print("DEBUG doTournament: orig_choice2 %s choice2 %s" % (orig_choice2, choice2))
                            selfHist1 = [choice1] + selfHist1 # latest choice is always [0]
                            selfHist2 = [choice2] + selfHist2
                            origHist1 = [orig_choice1] + origHist1 # scoring is based on orig choice + whoopsie
                            origHist2 = [orig_choice2] + origHist2
                            # print("DEBUG doTournament: origHist1 %s selfHist1 %s" % (origHist1, selfHist1))
                            # print("DEBUG doTournament: origHist2 %s selfHist2 %s" % (origHist2, selfHist2))
                            result1, rlsttbl = calcResult(this_reward_key, choice1, choice2)
                            result2, rslttbl = calcResult(this_reward_key, choice2, choice1)
                            selfScore1 = [result1] + selfScore1
                            selfScore2 = [result2] + selfScore2

                            scores_pairing[idx1] += result1
                            scores_pairing[idx2] += result2
                            scores_rewardstbl[idx1] += result1
                            scores_rewardstbl[idx2] += result2
                            scores_mistakes[idx1] += result1
                            scores_mistakes[idx2] += result2
                            scores_overall[idx1] += result1
                            scores_overall[idx2] += result2

                        if print_detail:
                            print("\nMove\t%s\tScore\t%s\tScore\t%s%s mistakes (seed %s)\tResultsTbl=%s: D_D=%s C_C=%s D_C=%s C_D=%s" % \
                                  (algolist[idx1], algolist[idx2], "%0.0f" % (100.0*mistake_percent), "%", rand_seed,
                                   this_reward_key, rslttbl[IDX_RESULT_D_C], rslttbl[IDX_RESULT_C_C], rslttbl[IDX_RESULT_D_D],
                                   rslttbl[IDX_RESULT_C_D]))
                            maxHist_m1 = len(selfHist1) - 1
                            sum1 = 0
                            sum2 = 0
                            for idx in range(maxHist_m1 + 1):
                                revIdx = maxHist_m1 - idx
                                move1 = TEXT_INTERP[selfHist1[revIdx]]
                                if origHist1[revIdx] != selfHist1[revIdx]:
                                    move1 += WHOOPSIE_MARKER
                                move2 = TEXT_INTERP[selfHist2[revIdx]]
                                if origHist2[revIdx] != selfHist2[revIdx]:
                                    move2 += WHOOPSIE_MARKER
                                print("%d\t%s\t%s\t%s\t%s\t" % (1+idx, move1, selfScore1[revIdx], move2, selfScore2[revIdx]))
                                sum1 += selfScore1[revIdx]
                                sum2 += selfScore2[revIdx]
                            print("Final Score\t%s\t%s\t%s\t%s\t" % (algolist[idx1], sum1, algolist[idx2], sum2))

                print_scores("Pairing", algolist, num_moves, "%0.0f" % (100.0*mistake_percent), "%", rand_seed, this_reward_key, rslttbl, scores_pairing)
            print_scores("RewardsTable", algolist, "N/A", "%0.0f" % (100.0*mistake_percent), "%", rand_seed, this_reward_key, rslttbl, scores_rewardstbl)
        print_scores("Mistakes", algolist, "N/A", "%0.0f" % (100.0*mistake_percent), "%", rand_seed, "N/A", ("N/A", "N/A", "N/A", "N/A"), scores_mistakes)
    print_scores("Overall", algolist, "N/A", "N/A", "", rand_seed, "N/A", ("N/A", "N/A", "N/A", "N/A"), scores_overall)
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
python PrisonersDilemmaTournament.py randomseed prof_mdo_template.yaml > formattedResults_just_the_facts.txt
python PrisonersDilemmaTournament.py --print-detail 47 prof_mdo_template.yaml > formattedResults_detailed.txt
""",
        usage='python %(prog)s randseed\n' +
              "   note: runs all files algo_*.py in directory\n" +
              "   note: algo_*.py written per algo_mdo_template.py")
    my_parser.add_argument('randseed', type=str, help='if integer, seed for random number; else random seed')
    my_parser.add_argument('fname_parms', type=str, help='filename in YAML format of parameters to range such as num_moves')
    my_parser.add_argument('-d', '--print-detail', action='store_true',
                           help='print detailed blow-by-blow for each pairing')
    args = my_parser.parse_args()

    if args.randseed[0].isdigit():
        theSeed = int(args.randseed)
    else:
        theSeed = round(time.time() * 1000) # random seed based on time in milliseconds
    random.seed(theSeed)

    doReadParms(args.fname_parms)

    # all the real work is done here
    doTournament(theSeed, args.print_detail)

    # end of "__main__"
