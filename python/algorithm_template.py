# Author: Mark Olson 2021-11-06 https://github.com/Mark-MDO47/PrisonDilemmaTourney
#
# algorithm_template.py a template for Prisoner's Dilemma algorithms.
#
# PrisonersDilemmaTournament.py receives a text string with the path to two algorithm python routines
# For an algorithm python routine in file algo.py, the calling sequence is
#     choice = algo(oppChoices, myChoices)
# Each call to the algorithm will have the following for parameters:
#     list of history all the choices made by both parties in reverse order (latest choice before this is [0], prev [1])
#       note: len(oppChoices) should be identical to len(myChoices); zero for first call, one for second call
#     value of each entry is one of BETRAY or KEEPSILENT
# The algorithm will return
#     BETRAY or KEEPSILENT
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
# Due to weak evidence held by the police, if both refuse to betray the other that will lead to a very small sentence
#   for each of them. If one stays silent and the other betrays, the betrayer gets off free and the silent one gets a
#   large sentence. If they both betray each other, they both get an intermediate sentence.
# (spoiler alert) If the game is played exactly one time, the game-theory best choice for each player is to
#   betray the other player.
#
# Robert Axelrod, professor of political science at the University of Michigan, held a tournament of competing
# strategies for the famous Prisoner's Dilemma in 1980.
#
# He had the insight that if the game is played many times in succession, then the history of play allows each player
#   to take into account the "reputation" of the other player in making their choice of behavior.
# He invited some game theorists to submit algorithms that would be competed against each other in a computer tournament.
# Later he held another tournament and invited anyone to submit algorithms.
# The "Tit-For-Tat" algorithm seemed to do the best.

def algorithm_template(selfHist1, oppHist1):
    BETRAY = 0
    KEEPSILENT = 1

    return BETRAY

if __name__ == "__main__":
   sys.stderr.write("ERROR - algorithm_template.py is not intended to be run stand-alone")
   exit(-1)
