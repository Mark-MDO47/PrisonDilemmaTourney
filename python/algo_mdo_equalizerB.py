# Author: Mark Olson 2021-11-06 https://github.com/Mark-MDO47/PrisonDilemmaTourney
#
# algo_mdo_equalizerB.py a Prisoner's Dilemma algorithm.
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
import probabilistic_strategy as prob        # guts of probabilistic strategy

# These probabilistic algorithms are based on the paper found here: https://www.jasss.org/20/4/12.html
#
# The algorithm in this template file behaves as follows:
#    On the first move it returns COOPERATE
#    On all subsequent moves, it calculates return with probabilty dependent on last self_opponent move:
#       returns COOPERATE given percent of the time per below
#           p1 = p_c_c if the last self,opponent move was COOPERATE,COOPERATE
#           p2 = p_c_d if the last self,opponent move was COOPERATE,DEFECT
#           p3 = p_d_c if the last self,opponent move was DEFECT,COOPERATE
#           p4 = p_d_d if the last self,opponent move was DEFECT,DEFECT
#
p_c_c = 0.90
p_c_d = 0.70
p_d_c = 0.20
p_d_d = 0.10
def algo_mdo_equalizerB(selfHist, oppHist, ID):
    return prob.probabilistic_strategy(selfHist, oppHist, ID, p_c_c, p_c_d, p_d_c, p_d_d)

if __name__ == "__main__":
    sys.stderr.write("ERROR - algo_mdo_equalizerB.py is not intended to be run stand-alone\n")
    exit(-1)

