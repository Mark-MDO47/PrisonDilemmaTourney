# ALGORITHMS

Each algorithm has a file that starts with algo_ and ends with .py. It is suggested that the author initials (mine are mdo) follow algo_, i.e. algo_mdo_description.py.

The file algorithm_template.py has information on naming conventions and methodology for creating algorithms, plus examples.

Each algorithm has access to the entire history of play so far for this round, but does not know what the opponent will do for this move. The two choices available are `cooperate` (c) or `defect` (d).

The algorithms here are my attempts to implement some famous algorithms from the literature. Currently there are two categories of algorithms here: deterministic and probabilistic.

## DETERNINISTIC ALGORITHMS

I won't list in alphabetical order. I will first list the simplest, then tit-for-tat and variations, then others.

- **algo_mdo_all_coop.py** - On every move it returns COOPERATE
- **algo_mdo_all_defect.py** - On every move it returns DEFECT
- **algo_mdo_per_cd.py** - sequences through COOPERATE, DEFECT
- **algo_mdo_per_ccd.py** - sequences through COOPERATE, COOPERATE, DEFECT
- **algo_mdo_per_ddc.py** - sequences through DEFECT, DEFECT, COOPERATE

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
- **algo_mdo_gradual.py** - first move it returns COOPERATE and sets its state to COOPERATE with zero "more defects" and zero "more cooperates", after that:
  - if the state is choices.COOPERATE:
    - if "more cooperates" is > 0, decrement "more cooperates" and return COOPERATE
    - else if opponent did COOPERATE, return COOPERATE
    - else (opponent did DEFECT), set state DEFECT and set "more defects" to (total number opponent defects - 1) and return DEFECT
  - else if the state is DEFECT
    - if "more defects" is > 0, decrement "more defects" and return DEFECT
    -  else if "more defects" is == 0, set state COOPERATE, set "more cooperates" to 1, and return COOPERATE
- **algo_mdo_gradual_var.py** This variant merely changes the number of times to DEFECT in response to DEFECT by the opponent
 - first move it returns COOPERATE and sets its state to COOPERATE with zero "more defects" and zero "more cooperates", after that:
    - if the state is choices.COOPERATE:
      - if "more cooperates" is > 0, decrement "more cooperates" and return COOPERATE
      - else if opponent did COOPERATE, return COOPERATE
      - else (opponent did DEFECT), set state DEFECT and set "more defects" to (n-1)*n/2 - 1 (where "n" is total number opponent defects) and return DEFECT
    - else if the state is DEFECT
      - if "more defects" is > 0, decrement "more defects" and return DEFECT
      - else if "more defects" is == 0, set state COOPERATE, set "more cooperates" to 1, and return COOPERATE

- **algo_mdo_spiteful.py**
- **algo_mdo_pavlov.py**
- **algo_mdo_prober.py**
- **algo_mdo_mem2.py**


## PROBABILISTIC ALGORITHMS

- **algo_mdo_equalizerA.py**
- **algo_mdo_equalizerB.py**
- **algo_mdo_equalizerC.py**
- **algo_mdo_equalizerD.py**
- **algo_mdo_equalizerE.py**
- **algo_mdo_equalizerF.py**
- **algo_mdo_extortionA.py**
- **algo_mdo_extortionB.py**
- **algo_mdo_extortionC.py**
- **algo_mdo_extortionD.py**
- **algo_mdo_extortionE.py**
- **algo_mdo_extortionF.py**
