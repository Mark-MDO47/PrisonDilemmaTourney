
import random
import PrisonersDilemmaTournament as choices # pick up choices.DEFECT and choices.COOPERATE

###################################################################################
# probabilistic_strategy - calculate move using probabilistic strategy from
#      one previous move.
#
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
def probabilistic_strategy(selfHist, oppHist, ID, p_c_c, p_c_d, p_d_c, p_d_d):
    if 0 == len(selfHist):
        return choices.COOPERATE

    myrand = random.random()
    myprob = 0.0
    if (choices.COOPERATE == selfHist[0]) and (choices.COOPERATE == oppHist[0]):
        myprob = p_c_c
    elif (choices.COOPERATE == selfHist[0]) and (choices.DEFECT == oppHist[0]):
        myprob = p_c_d
    elif (choices.DEFECT == selfHist[0]) and (choices.COOPERATE == oppHist[0]):
        myprob = p_d_c
    else: # (choices.DEFECT == selfHist[0]) and (choices.DEFECT == oppHist[0]):
        myprob = p_d_d

    if myrand < myprob:
        return choices.COOPERATE
    else:
        return choices.DEFECT