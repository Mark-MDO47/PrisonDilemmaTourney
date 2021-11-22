# Author: Mark Olson 2021-11-06 https://github.com/Mark-MDO47/PrisonDilemmaTourney
#
# algorithm_template.py a template for Prisoner's Dilemma algorithms.
#
# The algorithm in this template file behaves as follows:
#    On the first round it returns COOPERATE
#    On all subsequent rounds, it alternates between DEFECT and COOPERATE
#
# For an algorithm python routine in a file (i.e. with filename algo_mdo_something.py), the calling sequence is
#     algo_mdo_something(selfHist, oppHist, ID))
#     NOTE that the function name is the same as the python filename with the "*.py" removed
#     I recommend adding your initials (mine are mdo) to your file/algorithm name so we don't have name collisions
#     This template file is named algorithm_template.py so the function name is algorithm_template
# Each call to the algorithm will have the following for parameters:
#     list of history all the choices made by both parties in reverse order (latest choice before this is [0], prev [1])
#       Thus the opponent choice made in previous round, assuming this isn't the first round, is oppChoices[0].
#          if len(oppChoices) > 0, there was at least one prior round.
#       note: len(oppChoices) should be identical to len(myChoices)
#     value of each entry  in xxxHist is one of choices.DEFECT or choices.COOPERATE
# The algorithm will return
#     choices.DEFECT or choices.COOPERATE
# The algorithm can keep state variables. Remember that the algorithm will "restart" multiple times to compete with
#     other algorithms, so you must reset your state variables on the first move (0 == len(oppChoices)).
#     Also remember that your states will be global, so use the name of the algorithm in the name of your global.
#     This file has a trivial example of this technique.
# It is OK to use random.random() in your algorithm, but do not set the seed (do not call random.seed()). The
#     tournament uses random.* and it is nice to have repeatable runs when desired, so please play nice!
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
# This is essentially the same effect as algo_mdo_per_cd.py
#
# NOTE: this has the debug code removed to show how simple the actual code is
# NOTE: use of static global storage is just for illustration, not actually used in the code itself
ALGORITHM_TEMPLATE_STORAGE = {} # static global storage is just for illustration
def algorithm_template(selfHist, oppHist, ID):
    global ALGORITHM_TEMPLATE_STORAGE

    if (0 == len(oppHist)):
        ALGORITHM_TEMPLATE_STORAGE[ID] = 1.0 # must reset state variable(s) if first move
    ALGORITHM_TEMPLATE_RANDOM = ALGORITHM_TEMPLATE_STORAGE[ID] # move state variables to local variables

    rtn = choices.DEFECT
    if (0 == (len(selfHist) % 2)) and (0 == (len(oppHist) % 2)): # both lengths guaranteed to be the same
        rtn = choices.COOPERATE
    else:
        rtn = choices.DEFECT
    ALGORITHM_TEMPLATE_RANDOM *= random.random() # useless but is a demo; please do NOT call random.seed()!

    ALGORITHM_TEMPLATE_STORAGE[ID] = ALGORITHM_TEMPLATE_RANDOM # move local variables to state variables

    return rtn

"""
# NOTE: Don't Panic! This just shows some potential debug code, not necessary!
def algorithm_template(selfHist, oppHist, ID):
    DEBUG_ALGO = True

    if DEBUG_ALGO:
        print(" algorithm_template DEBUG    len(self)=%d len(opp)=%d" % (len(selfHist),len(oppHist)))
    if (0 == (len(selfHist) % 2)) and (0 == (len(oppHist) % 2)):
        if DEBUG_ALGO:
            print(" algorithm_template DEBUG move %d choice=%s" % (1+len(oppHist), choices.TEXT_INTERP[choices.COOPERATE]))
        return choices.COOPERATE
    else:
        if DEBUG_ALGO:
            print(" algorithm_template DEBUG move %d choice=%s" % (1+len(oppHist), choices.TEXT_INTERP[choices.DEFECT]))
        return choices.DEFECT
"""

if __name__ == "__main__":
    sys.stderr.write("ERROR - algorithm_template.py is not intended to be run stand-alone\n")
    exit(-1)
