# Author: Mark Olson 2021-11-06 https://github.com/Mark-MDO47/PrisonDilemmaTourney
#
# algo_mdo_mem2.py - Prisoner's Dilemma tournament algorithm file
#
#
# The algo_mdo_mem2 algorithm behaves as follows:
#    the first two moves are the same as TIT-FOR-TAT
#    following that, it continually evaluates the previous two moves
#       if both of the previous two moves by both sides are COOPERATE, then play TIT-FOR-TAT the following 2 moves
#       if both of the previous two moves by both sides are opposite each other, then play TIT-FOR-2-TAT next 2 moves
#       in all other cases play ALL-D the next two moves, keeping track of how often this is done
#          if ALL-D gets picked twice (ever) then that decision becomes permanent
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

# The algo_mdo_mem2 algorithm behaves as follows:
#    the first two moves are the same as TIT-FOR-TAT
#    following that, it continually evaluates the previous two moves
#       if both of the previous two moves by both sides are COOPERATE, then play TIT-FOR-TAT the following 2 moves
#       if both of the previous two moves by both sides are opposite each other, then play TIT-FOR-2-TAT next 2 moves
#       in all other cases play ALL-D the next two moves, keeping track of how often this is done
#          if ALL-D gets picked twice (ever) then that decision becomes permanent
#
# note: the function name should be exactly the same as the filename but without the ".py"
# note: len(selfHist) and len(oppHist) should always be the same
#
ALGO_MDO_MEM2_STORAGE = {}
def algo_mdo_mem2(selfHist, oppHist, ID):
    global ALGO_MDO_MEM2_STORAGE

    # handle the first move in the game
    if 0 == len(selfHist): # must reinitialize each "game"
        ALGO_MDO_MEM2_STORAGE[ID] = ["TIT-FOR-TAT", 2, 0]

    BEHAVIOR, BEHAVE_COUNT, ALL_D_COUNT = ALGO_MDO_MEM2_STORAGE[ID]

    # sys.stderr.write("DEBUG move=%d ID=%s VIOR=%s VE_COUNT=%s D_COUNT=%s\n   selfhist = %s\n    opphist = %s\n" % \
    #                  (len(selfHist), ID, BEHAVIOR, BEHAVE_COUNT, ALL_D_COUNT, selfHist, oppHist))

    rtn = choices.DEFECT

    # make sure we are in the correct state to choose a move
    if 2 <= ALL_D_COUNT:
        # sys.stderr.write("DEBUG pass D_COUNT=%s\n" % ALL_D_COUNT)
        pass # stay ALL-D forever
    elif 1 <= BEHAVE_COUNT:
        # sys.stderr.write("DEBUG pass VE_COUNT==%s\n" % BEHAVE_COUNT)
        pass # stay the course for this behavior
    elif 0 >= BEHAVE_COUNT: # reached another decision point
        # sys.stderr.write("DEBUG decision VE_COUNT==%s\n" % BEHAVE_COUNT)
        if (choices.COOPERATE == selfHist[1]) and (choices.COOPERATE == oppHist[1]) and \
                (choices.COOPERATE == selfHist[0]) and (choices.COOPERATE == oppHist[0]):
            BEHAVIOR = "TIT-FOR-TAT"
            BEHAVE_COUNT = 2
    elif (oppHist[1] != selfHist[1]) and (oppHist[0] != selfHist[0]):
        # sys.stderr.write("DEBUG check1 VE_COUNT==%s\n" % BEHAVE_COUNT)
        BEHAVIOR = "TIT-FOR-2-TAT"
        BEHAVE_COUNT = 2
    else:
        # sys.stderr.write("DEBUG check2 VE_COUNT==%s\n" % BEHAVE_COUNT)
        BEHAVIOR = "ALL-D"
        BEHAVE_COUNT = 2
        ALL_D_COUNT += 1

    if 1 <= BEHAVE_COUNT: # this is not really needed
        BEHAVE_COUNT -= 1
    if ("ALL-D" == BEHAVIOR) or (2 <= ALL_D_COUNT):
        rtn = choices.DEFECT # always return DEFECT
    elif "TIT-FOR-TAT" == BEHAVIOR:
        if len(oppHist) <= 0:  # first move
            rtn = choices.COOPERATE
        else:
            rtn = oppHist[0]
    elif "TIT-FOR-2-TAT" == BEHAVIOR:
        if (choices.DEFECT == oppHist[1]) or (choices.DEFECT == oppHist[0]):
            rtn = choices.DEFECT
        else:
            rtn = oppHist[0]
    else:
        sys.stderr.write("\nERROR algo_mdo_mem2 - invalid state %s\n\n" % BEHAVIOR)

    ALGO_MDO_MEM2_STORAGE[ID] = [BEHAVIOR, BEHAVE_COUNT, ALL_D_COUNT]

    return rtn

if __name__ == "__main__":
    sys.stderr.write("ERROR - algo_mdo_mem2.py is not intended to be run stand-alone\n")
    exit(-1)
