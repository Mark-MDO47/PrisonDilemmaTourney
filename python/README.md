# ALGORITHMS

Each algorithm has a file that starts with algo_ and ends with .py. It is suggested that the author initials (mine are mdo) follow algo_, i.e. algo_mdo_description.py.

The file algorithm_template.py has information on naming conventions and methodology for creating algorithms, plus examples.

Each algorithm has access to the entire history of play so far for this round, but does not know what the opponent will do for this move. The two choices available are `cooperate` (c) or `defect` (d).

The algorithms here are my attempts to implement some famous algorithms from the literature. Currently there are two categories of algorithms here: deterministic and probabilistic.

## DETERMINISTIC ALGORITHMS

I won't list in alphabetical order. I will first list the simplest, then tit-for-tat and variations, then others.

- **algo_mdo_all_coop.py** - On every move it returns COOPERATE
- **algo_mdo_all_defect.py** - On every move it returns DEFECT
- **algo_mdo_per_cd.py** - sequences through COOPERATE, DEFECT
- **algo_mdo_per_ccd.py** - sequences through COOPERATE, COOPERATE, DEFECT
- **algo_mdo_per_ddc.py** - sequences through DEFECT, DEFECT, COOPERATE

- **algo_mdo_spiteful.py** - first move it returns COOPERATE, after that
  - it returns COOPERATE unless and until the opponent ever does DEFECT
  - if the opponent ever does a DEFECT, it will return DEFECT forever
- **algo_mdo_pavlov.py** - first move it returns COOPERATE, after that if on previous move both self and opponent
  - disagree: return DEFECT
  - agree: return COOPERATE

- **algo_mdo_tit_for_tat.py** - first move it returns COOPERATE, after that it does what the opponent did on the previous move
- **algo_mdo_susp_tit_for_tat.py** - first move it returns DEFECT, after that it does what the opponent did on the previous move
- **algo_mdo_tit_for_2_tat.py** - first two moves it returns COOPERATE, after that:
  - if the opponent did DEFECT within the last two moves, it returns DEFECT this move
  - else it returns COOPERATE this move
- **algo_mdo_forgiv_tit_for_tat.py** - first two moves it returns COOPERATE, after that:
  - if the opponent did DEFECT within the last two moves, it returns DEFECT this move
  - else it returns COOPERATE this move
- **algo_mdo_slow_tit_for_tat.py** - first two moves it returns COOPERATE and sets its state to COOPERATE, after that:
  - if the last two opponent moves were the same, it switches its state to that move
  - then it returns its state
- **algo_mdo_soft_majo.py**  - first move it returns COOPERATE, after that:
  - if the opponent COOPERATE >= DEFECT, return COOPERATE
  - else return DEFECT
- **algo_mdo_hard_majo.py**  - first move it returns COOPERATE, after that:
  - if the opponent COOPERATE >= DEFECT (not >=), return COOPERATE
  - else return DEFECT
- **algo_mdo_prober.py** - the first three moves are DEFECT, COOPERATE and COOPERATE. On the fourth move it evaluates if its opponent has cooperated in the moves 2 and 3
  - If so: return DEFECT from then on
  - else: play as in tit_for_tat
- **algo_mdo_mem2.py** - the first two moves are the same as TIT-FOR-TAT. Following that, it continually evaluates the previous two moves
  - if both of the previous two moves by both sides are COOPERATE, then play TIT-FOR-TAT the following 2 moves
  - if both of the previous two moves by both sides are opposite each other, then play TIT-FOR-2-TAT next 2 moves
  - in all other cases play ALL-D the next two moves, keeping track of how often this is done
    - if ALL-D gets picked twice (ever) then that decision becomes permanent
- **algo_mdo_gradual.py** - first move it returns COOPERATE and sets its state to COOPERATE with zero "more defects" and zero "more cooperates", after that:
  - if the state is COOPERATE:
    - if "more cooperates" is > 0, decrement "more cooperates" and return COOPERATE
    - else if opponent did COOPERATE, return COOPERATE
    - else (opponent did DEFECT), set state DEFECT and set "more defects" to (total number opponent defects - 1) and return DEFECT
  - else if the state is DEFECT
    - if "more defects" is > 0, decrement "more defects" and return DEFECT
    -  else if "more defects" is == 0, set state COOPERATE, set "more cooperates" to 1, and return COOPERATE
- **algo_mdo_gradual_var.py** This variant merely changes the number of times to DEFECT in response to DEFECT by the opponent
  - first move it returns COOPERATE and sets its state to COOPERATE with zero "more defects" and zero "more cooperates", after that:
    - if the state is COOPERATE:
      - if "more cooperates" is > 0, decrement "more cooperates" and return COOPERATE
      - else if opponent did COOPERATE, return COOPERATE
      - else (opponent did DEFECT), set state DEFECT and set "more defects" to (n-1)*n/2 - 1 (where "n" is total number opponent defects) and return DEFECT
    - else if the state is DEFECT
      - if "more defects" is > 0, decrement "more defects" and return DEFECT
      - else if "more defects" is == 0, set state COOPERATE, set "more cooperates" to 1, and return COOPERATE

## PROBABILISTIC ALGORITHMS

These probabilistic algorithms are based on the paper found here: https://www.jasss.org/20/4/12.html<br>
On the first move they return COOPERATE<br>
On all subsequent moves, the calculate return with probabilty dependent on last self_opponent move<br>
- p1 = p_c_c if the last self,opponent move was COOPERATE,COOPERATE
- p2 = p_c_d if the last self,opponent move was COOPERATE,DEFECT
- p3 = p_d_c if the last self,opponent move was DEFECT,COOPERATE
- p4 = p_d_d if the last self,opponent move was DEFECT,DEFECT

<br>

- **algo_mdo_equalizerA.py** - p_c_c = 0.75, p_c_d = 0.25, p_d_c = 0.50, p_d_d = 0.25
- **algo_mdo_equalizerB.py** - p_c_c = 0.90, p_c_d = 0.70, p_d_c = 0.20, p_d_d = 0.10
- **algo_mdo_equalizerC.py** - p_c_c = 0.90, p_c_d = 0.50, p_d_c = 0.50, p_d_d = 0.30
- **algo_mdo_equalizerD.py** - p_c_c = 27.0/35.0, p_c_d = 17.0/35.0, p_d_c = 0.20, p_d_d = 2.0/35.0
- **algo_mdo_equalizerE.py** - p_c_c = 2.0/3.0, p_c_d = 0.00, p_d_c = 2.0/3.0, p_d_d = 1.0/3.0
- **algo_mdo_equalizerF.py** - p_c_c = 1.00, p_c_d = 13.0/15.0, p_d_c = 0.20, p_d_d = 0.40
- **algo_mdo_extortionA.py** - p_c_c = 8.0/9.0, p_c_d = 2.0/9.0, p_d_c = 11.0/18.0, p_d_d = 0.00
- **algo_mdo_extortionB.py** - p_c_c = 0.80, p_c_d = 0.10, p_d_c = 0.60, p_d_d = 0.00
- **algo_mdo_extortionC.py** - p_c_c = 11.0/12.0, p_c_d = 5.0/24.0, p_d_c = 2.0/3.0, p_d_d = 0.00
- **algo_mdo_extortionD.py** - p_c_c = 5.0/6.0, p_c_d = 0.25, p_d_c = 0.50, p_d_d = 0.00
- **algo_mdo_extortionE.py** - p_c_c = 0.85, p_c_d = 3.0/40.0, p_d_c = 0.70, p_d_d = 0.00
- **algo_mdo_extortionF.py** - p_c_c = 11.0/15.0, p_c_d = 2.0/15.0, p_d_c = 7.0/15.0, p_d_d = 0.00
