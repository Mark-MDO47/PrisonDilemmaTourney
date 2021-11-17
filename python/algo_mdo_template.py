# Author: Mark Olson 2021-11-06 https://github.com/Mark-MDO47/PrisonDilemmaTourney
#
# algo_mdo_template.py a template for Prisoner's Dilemma algorithms.
#
# The algorithm in this template file behaves as follows:
#    On the first round it returns COOPERATE
#    On all subsequent rounds, it alternates between DEFECT and COOPERATE
#
# For an algorithm python routine in a file (i.e. with filename algo_mdo.py), the calling sequence is
#     choice = algo_mdo(myChoices, oppChoices)
#     NOTE that the function name is the same as the python filename with the "*.py" removed
#     I recommend adding your initials (mine are mdo) to your file/algorithm name so we don't have name collisions
#     This template file is named algo_mdo_template.py so the function name is algo_mdo_template
# Each call to the algorithm will have the following for parameters:
#     list of history all the choices made by both parties in reverse order (latest choice before this is [0], prev [1])
#       Thus the opponent choice made in previous round, assuming this isn't the first round, is oppChoices[0].
#          if len(oppChoices) > 0, there was at least one prior round.
#       note: len(oppChoices) should be identical to len(myChoices)
#     value of each entry  in xxxChoices is one of value.DEFECT or value.COOPERATE
#
# The algorithm will return
#     value.DEFECT or value.COOPERATE
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

import sys
import PrisonersDilemmaTournament as choices # pick up choices.DEFECT and choices.COOPERATE

# note: the function name should be exactly the same as the filename but without the ".py"
#
# The algorithm in this template file behaves as follows:
#    On the first move it returns COOPERATE
#    On all subsequent move, it alternates between DEFECT and COOPERATE
# note: len(selfHist) and len(oppHist) should always be the same; I put both tests in just to demonstrate this
#
# NOTE: this has the debug code removed to show how simple the actual code is
def algo_mdo_template(selfHist, oppHist):
    rtn = choices.DEFECT
    if (0 == (len(selfHist) % 2)) and (0 == (len(oppHist) % 2)):
        rtn = choices.COOPERATE
    else:
        rtn = choices.DEFECT
    return rtn

"""
# NOTE: Don't Panic! This just shows some potential debug code, not necessary!
def algo_mdo_template(selfHist, oppHist):
    DEBUG_ALGO = True

    if DEBUG_ALGO:
        print(" algo_mdo_template DEBUG    len(self)=%d len(opp)=%d" % (len(selfHist),len(oppHist)))
    if (0 == (len(selfHist) % 2)) and (0 == (len(oppHist) % 2)):
        if DEBUG_ALGO:
            print(" algo_mdo_template DEBUG move %d choice=%s" % (1+len(oppHist), choices.TEXT_INTERP[choices.COOPERATE]))
        return choices.COOPERATE
    else:
        if DEBUG_ALGO:
            print(" algo_mdo_template DEBUG move %d choice=%s" % (1+len(oppHist), choices.TEXT_INTERP[choices.DEFECT]))
        return choices.DEFECT
"""

if __name__ == "__main__":
    sys.stderr.write("ERROR - algo_mdo_template.py is not intended to be run stand-alone\n")
    exit(-1)
