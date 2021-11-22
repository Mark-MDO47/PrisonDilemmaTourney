# Author: Mark Olson 2021-11-06 https://github.com/Mark-MDO47/PrisonDilemmaTourney
#
# algo_mdo_prober.py - Prisoner's Dilemma tournament algorithm file
#
# The algo_mdo_prober algorithm behaves as follows:
#    the first three moves are choices.DEFECT, choices.COOPERATE and choices.COOPERATE
#    on the fourth move it evaluates if its opponent has cooperated in the moves 2 and 3
#        If so: return choices.DEFECT from then on
#        else: play as in tit_for_tat
#
# For an algorithm python routine in a file (i.e. with filename algo_mdo_something.py), the calling sequence is
#     algo_mdo_something(selfHist, oppHist, ID))
#     NOTE that the function name is the same as the python filename with the "*.py" removed
#     I recommend adding your initials (mine are mdo) to your file/algorithm name so we don't have name collisions
#     This template file is named algorithm_template.py so the function name is algorithm_template
# Each call to the algorithm will have the following for parameters:
#     list of history all the choices made by both parties in reverse order (latest choice before this is [0], prev [1])
#       Thus the opponent choice made in previous move, assuming this isn't the first move, is oppChoices[0].
#          if len(oppChoices) > 0, there was at least one prior move.
#       note: len(oppChoices) should be identical to len(myChoices)
#     value of each entry  in xxxHist is one of choices.DEFECT or choices.COOPERATE
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

# The algo_mdo_prober algorithm behaves as follows:
#    the first three moves are choices.DEFECT, choices.COOPERATE and choices.COOPERATE
#    on the fourth move it evaluates if its opponent has cooperated in the moves 2 and 3
#        If so: return choices.DEFECT from then on
#        else: play as in tit_for_tat
#
# note: the function name should be exactly the same as the filename but without the ".py"
# note: len(selfHist) and len(oppHist) should always be the same
#
ALGO_MDO_PROBER_STORAGE = {}
def algo_mdo_prober(selfHist, oppHist, ID):
    global ALGO_MDO_PROBER_STORAGE

    if 0 == len(selfHist): # must reinitialize each "game"
        ALGO_MDO_PROBER_STORAGE[ID] = "NONE"

    BEHAVIOR = ALGO_MDO_PROBER_STORAGE[ID]

    rtn = choices.DEFECT
    if 0 == len(selfHist):
        BEHAVIOR = "NONE"
        rtn = choices.DEFECT
    elif 2 <= len(selfHist):
        rtn = choices.COOPERATE
    elif 3 == len(selfHist):
        if (choices.COOPERATE == oppHist[0]) or (choices.COOPERATE == oppHist[1]):
            BEHAVIOR = "DEFECT"
        else:
            BEHAVIOR = "TIT-FOR-TAT"

    # this section only happens after choice was made on 3rd move
    if "DEFECT" == BEHAVIOR:
        rtn = choices.DEFECT # always return DEFECT
    elif "TIT-FOR-TAT" == BEHAVIOR:
        rtn = oppHist[0]

    ALGO_MDO_PROBER_STORAGE[ID] = BEHAVIOR

    return rtn

if __name__ == "__main__":
    sys.stderr.write("ERROR - algo_mdo_prober.py is not intended to be run stand-alone\n")
    exit(-1)
