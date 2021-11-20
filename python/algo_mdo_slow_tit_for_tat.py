# Author: Mark Olson 2021-11-06 https://github.com/Mark-MDO47/PrisonDilemmaTourney
#
# algo_mdo_slow_tit_for_tat.py - Prisoner's Dilemma tournament algorithm file
#
# The algo_mdo_slow_tit_for_tat algorithm behaves as follows:
#    On the first two moves it returns choices.COOPERATE and sets its state to cooperate
#    On all subsequent moves,
#       if the last two opponent moves were the same, it switches its state to that move
#       it returns its state
#
# For an algorithm python routine in a file (i.e. with filename algo_mdo.py), the calling sequence is
#     choice = algo_mdo(myChoices, oppChoices)
#     NOTE that the function name is the same as the python filename with the "*.py" removed
#     I recommend adding your initials (mine are mdo) to your file/algorithm name so we don't have name collisions
#     This template file is named algorithm_template.py so the function name is algorithm_template
# Each call to the algorithm will have the following for parameters:
#     list of history all the choices made by both parties in reverse order (latest choice before this is [0], prev [1])
#       Thus the opponent choice made in previous move, assuming this isn't the first move, is oppChoices[0].
#          if len(oppChoices) > 0, there was at least one prior move.
#       note: len(oppChoices) should be identical to len(myChoices)
#     value of each entry  in xxxChoices is one of choices.DEFECT or choices.COOPERATE
#
# The algorithm will return
#     choices.DEFECT or choices.COOPERATE
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

# The algo_mdo_slow_tit_for_tat algorithm behaves as follows:
#    On the first two moves it returns choices.COOPERATE and sets its state to cooperate
#    On all subsequent moves,
#       if the last two opponent moves were the same, it switches its state to that move
#       it returns its state
#
# note: the function name should be exactly the same as the filename but without the ".py"
# note: len(selfHist) and len(oppHist) should always be the same
#
ALGO_MDO_SLOW_TIT_FOR_TAT_STATE = choices.COOPERATE
def algo_mdo_slow_tit_for_tat(selfHist, oppHist):
    global ALGO_MDO_SLOW_TIT_FOR_TAT_STATE # need some static storage

    if len(oppHist) <= 1: # first two moves
        ALGO_MDO_SLOW_TIT_FOR_TAT_STATE = choices.COOPERATE
    elif oppHist[0] == oppHist[1]:
        ALGO_MDO_SLOW_TIT_FOR_TAT_STATE = oppHist[0]
    return ALGO_MDO_SLOW_TIT_FOR_TAT_STATE

if __name__ == "__main__":
    sys.stderr.write("ERROR - algo_mdo_slow_tit_for_tat.py is not intended to be run stand-alone\n")
    exit(-1)
