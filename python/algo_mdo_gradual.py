# Author: Mark Olson 2021-11-06 https://github.com/Mark-MDO47/PrisonDilemmaTourney
#
# algo_mdo_gradual.py - Prisoner's Dilemma tournament algorithm file
#
# This one is a little complicated. Here is the description from
# https://www.researchgate.net/publication/2697047_Our_Meeting_With_Gradual_A_Good_Strategy_For_The_Iterated_Prisoner's_Dilemma
#
# This strategy acts as tit-for-tat, except when it is time to forgive and remember the past. It uses cooperation on
# the first move and then continues to do so as long as the other player cooperates. Then after the ﬁrst defection
# of the other player, it defects one time and cooperates two times; after the second defection of the opponent, it
# defects two times and cooperates two times, ... after the nth defection it reacts with n consecutive defections and
# then calms down its opponent with two cooperations. As we can see this strategy has the same qualities as
# those described by Axelrod in [2] for tit-for-tat except one: the simplicity. Gradual has a memory of the game
# since the beginning of it.
#
# The algo_mdo_gradual algorithm behaves as follows:
#    On the first move it returns choices.COOPERATE and sets its states to
#           choices.COOPERATE and zero "more defects" and zero "more cooperates"
#    On all subsequent moves
#       if the state is choices.COOPERATE
#           if "more cooperates" is > 0, decrement "more cooperates" and return choices.COOPERATE
#           else if opponent did choices.COOPERATE, return choices.COOPERATE
#           else (opponent did choices.DEFECT), set state choices.DEFECT and set "more defects" to
#                       (total number opponent defects - 1) and return choices.DEFECT
#       else if the state is choices.DEFECT
#           if "more defects" is > 0, decrement "more defects" and return choices.DEFECT
#           else if "more defects" is == 0, set state choices.COOPERATE, set "more cooperates" to 1, and return choices.COOPERATE
#
# For an algorithm python routine in a file (i.e. with filename algo_mdo_something.py), the calling sequence is
#     algo_mdo_something(selfHist, oppHist, ID))
#     I recommend adding your initials (mine are mdo) to your file/algorithm name so we don't have name collisions
#     NOTE that the function name is the same as the python filename with the *.py removed
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

# The algo_mdo_gradual algorithm behaves as follows:
#    On the first move it returns choices.COOPERATE and sets its states to
#           choices.COOPERATE and zero "more defects" and zero "more cooperates"
#    On all subsequent moves
#       if the state is choices.COOPERATE
#           if "more cooperates" is > 0, decrement "more cooperates" and return choices.COOPERATE
#           else if opponent did choices.COOPERATE, return choices.COOPERATE
#           else (opponent did choices.DEFECT), set state choices.DEFECT and set "more defects" to
#                       (total number opponent defects - 1) and return choices.DEFECT
#       else if the state is choices.DEFECT
#           if "more defects" is > 0, decrement "more defects" and return choices.DEFECT
#           else if "more defects" is == 0, set state choices.COOPERATE, set "more cooperates" to 1, and return choices.COOPERATE
#
# note: the function name should be exactly the same as the filename but without the ".py"
# note: len(selfHist) and len(oppHist) should always be the same
#
ALGO_MDO_GRADUAL_STORAGE = {}
def algo_mdo_gradual(selfHist, oppHist, ID):
    global ALGO_MDO_GRADUAL_STORAGE # need some static storage

    if len(oppHist) == 0: # first move
        ALGO_MDO_GRADUAL_STORAGE[ID] = [choices.COOPERATE, 0, 0, 0]

    STATE, MORE_COOP, MORE_DEFECTS, NUM_OPP_DEFECTS = ALGO_MDO_GRADUAL_STORAGE[ID]

    # keep track of total number of opponent defects for convenience; could use oppHist
    if (len(oppHist) != 0) and (choices.DEFECT == oppHist[0]):
        NUM_OPP_DEFECTS += 1

    if len(oppHist) == 0: # first move
        pass
    elif STATE == choices.COOPERATE:
        if MORE_COOP > 0:
            MORE_COOP -= 1
        elif choices.DEFECT == oppHist[0]:
            STATE = choices.DEFECT
            MORE_DEFECTS = NUM_OPP_DEFECTS-1
    else: # if STATE = choices.DEFECT:
        if MORE_DEFECTS > 0:
            MORE_DEFECTS -= 1
        else: # MORE_DEFECTS == 0
            STATE = choices.COOPERATE
            MORE_COOP = 1

    ALGO_MDO_GRADUAL_STORAGE[ID] = [STATE, MORE_COOP, MORE_DEFECTS, NUM_OPP_DEFECTS]

    return STATE

if __name__ == "__main__":
    sys.stderr.write("ERROR - algo_mdo_gradual.py is not intended to be run stand-alone\n")
    exit(-1)
