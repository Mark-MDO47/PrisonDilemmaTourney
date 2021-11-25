# Prisoner's Dilemma tournament

## Quick Introduction

Quoting from the paper listed below `with slight editing`:
* See https://www.jasss.org/20/4/12.html
> "The iterated prisoner’s dilemma is a game that allows `one` to understand various basic truths about social behaviour and how cooperation between entities is established and evolves sharing `the` same space: living organisms sharing an ecological niche, companies competitors fighting over a market, people with questions about the value of conducting a joint work, etc. ..."

> "Although based on an extreme simplification of the interactions between entities, the mathematical study of the iterated prisoner’s dilemma remains difficult, and often, only computer simulations are able to solve classical questions or identify ways of building efficient behaviours ..."

For an excellent and gentle interactive introduction to the basics and then many of the factors that can affect the tournament, I highly recommend https://ncase.me/trust/, which is based on Robert Axelrod's book `THE EVOLUTION OF COOPERATION`.

## What is the Prisoner's Dilemma and the Iterated Prisoner's Dilemma?
* See https://en.wikipedia.org/wiki/Prisoner%27s_dilemma
* See https://cs.stanford.edu/people/eroberts/courses/soco/projects/1998-99/game-theory/axelrod.html
* See https://www.pnas.org/content/109/26/10409

Merrill Flood and Melvin Dresher from RAND corporation framed the concept in 1950 to show why two completely rational individuals might not cooperate, even if it appears that it is in their best interests to do so.

There are many scenarios that can be mapped to this concept, but the famous mapping by Albert W. Tucker called the "Prisoner's Dilemma" revolves around two prisoners, "A" and "B", guilty of the same crime and being held in separate interrogation rooms.
* Due to weak evidence held by the police, if both choose to `cooperate (C)` (refuse to `defect (D)`) that will lead to an intermediate sentence `R` for each of them. If one chooses to `cooperate` and the other chooses to `defect`, the defector gets a very low sentence `T` (usually zero) and the cooperator gets a large sentence `S`. If they both choose to `defect`, they both get an intermediate sentence `P`.
* In my "sentence" formulation for a Prisoner's Dilemma (instead of the "reward" formulation), `S` > `P` > `R` > `T`. Because `P` > `R`, mutual cooperation pays off better than mutual defection.
* If the game is played only once, the game-theoretic best response for each player is to defect (betray the other person).

Robert Axelrod, professor of political science at the University of Michigan, had the insight that if the game is played many times in succession, then the history of play allows each player to take into account the "reputation" of the other player in making their choice of behavior. He held tournaments of competing strategies for the Prisoner's Dilemma starting in 1980, and this led to a great deal of research.
* The "Tit-For-Tat" algorithm seemed to do the best.

Of course, there has been a lot of thinking about the issues around this game since then. For an excellent and gentle interactive introduction to the basics and then many of the factors that can affect the tournament, I highly recommend https://ncase.me/trust/, which is based on Robert Axelrod's book `THE EVOLUTION OF COOPERATION`.

## What is this tournament and how do I participate?

I plan to run an Iterated Prisoner's Dilemma tournament among members of my extended family and friends. This repository contains a short Python program (PrisonersDilemmaTournament.py) that runs both a tourament and an evolutionary competition.

I wrote a template for the python code for the algorithms (algorithm_template.py), and also wrote code for the 19 basic deterministic strategies from the literature (including the simplest imaginable strategies such as always defect). Thus we have at least the basics covered.

Submitted algorithms will have the naming convention algo_`your-initials`_`description`.py; this will help avoid naming collisions.
See algorithm_template.py for examples and information on this and other common techniques such as static storage for algorithms.

The idea for the tournament is to create one or more algorithms and submit them, or choose an existing strategy and vote for it. If you wish to implement your own version of a strategy in the 19 I included, we will run that also.

With algorithms collected, I will run the tournament:
* each strategy plays versus each other strategy and also plays against itself, with scores summed up
* each strategy also plays in an "evolution" section, in which multiples of each algorithm are all started.
  * In each evolution, each instance of algorithm is competed against all the others and then the worst few scorers are replaced with instances of the highest few scorers.
  * This usually shows a clear winner pretty soon, with most eliminated and perhaps one or two others persisting at a low level.
  
I am aware that there is already existing software for this type of tournament such as https://evolution-outreach.biomedcentral.com/articles/10.1007/s12052-012-0434-x
* although the link to the code is broken...
* ... even if the link was not broken, it is more fun to write my own!

## Factors that will be varied during the tournament

### Rewards or Scoring
There is the possibility of sensitivity of tournament results to the values used to calculate the score (number of years of sentence) under the different choices. Let's call the two participants X and Y and their choices (`C` or `D`) are selected by the horizontal and vertical axes of the table, respectively. The score for each combination of choices by X and Y is indicated by the letters on the top and left of the cell, respectively. Also the highlighting style will help associate the score with the entry in the cell. These letters `S`, `P`, `R`, and `T` are used in the literature.

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; X <BR> `Y`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Cooperate | Defect |
| --- | --- | --- |
| **Cooperate** | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **R** <BR> `R`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **T** <BR> `S`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| **Defect** | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **S** <BR> `T`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **P** <BR> `P`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |

This tournament will be played under several different payoff ranges, each with `S` > `P` > `R` > `T`. `T` is typically zero in the literature.

Personally, I find this `S` > `P` > `R` > `T` nomenclature a little hard to remember. I think of it (and the code refers to it) as the result a self-choice and an opponent-choice. Thinking of one of the participants as self and the other as opponent, here are the results as `self-choice` _ `opponent-choice` or equivalently the `C` or `D` choices of `Y` _ **X** in the table above:
* `C_D` = `S` = I nobly `cooperate` but my dastardly opponent `defects`
* `D_D` = `P` = I reluctantly follow my short-term best interests and `defect` and my dastardly opponent self-interestedly `defects` too
* `C_C` = `R` = I nobly `cooperate` and my opponent probably slips and chooses to `cooperate` too
* `D_C` = `T` = I slyly defect and my naive opponent cooperates

### Number of moves per match
Another factor is the number of moves per match. Again, this tournament will range through a range of moves per match. If the number of moves was known to be 10, you could have an algorithm always `defect` on the last move!

### Errors
Another factor that can affect the tournament is the concept of errors. In the real world, sometimes factors intervene to prevent us from implementing the choice we made. This tournament will range through some percentage of these errors.

## Factors that will be varied during Evolution
In addition to the factors above, these factors will be varied:

### Number of clones of each algorithm in the starting population
In the literature it is typical to start evolution with 100 clones or instances of each algorithm in a giant round-robin for each Evolution iteration. Even with just my 19 initial algorithms, this would be 1900 * (1900-1) / 2 pairings, or 1,804,050 pairings (each with a number of moves) for each Evolution iteration. Then if I wanted to explore the effects of anything across a range, that would be multiplied many times over. I will typically use a much smaller number of clones for my starting population. Maybe after doing some explorations, I will do a few with 100 clones to validate that my results are representative.

### Number of bottom-ranked clones to be replaced by top-ranked clones on each Evolution iteration
This one is pretty self-explanatory. If this number is significantly smaller than the number of clones in the starting population, it will take a while for any one algorithm to be eliminated or reach a low self-sustaining level. The downside is that it takes more Evolution iterations before the final result becomes evident.
 
In the literature they seem to start with 100 clones and then reach a near steady state after 25 iterations. In one example with 17 algorithms, 7 algorithms have gone to zero population counts after 25 Evolution iterations. This means that they must be replacing about 700/25 or 28 (probably 30) of the bottom-ranked clones each Evolution iteration.
 
### Number of Evolution iterations before calculating the final score
Most of the results in the literature show a steady or near-steady state after 25 Evolution iterations or so. Just eyeballing the graphs, it looks to me like the trends become clear after 15 iterations or so. Of course, as described above, to achieve this one must adjust the other parameters so that it can reach stability so quickly.

