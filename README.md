# Prisoner's Dilemma tournament

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

Of course, there has been a lot of thinking about the issues around this game since then. For an excellent and gentle interactive introduction to the basics and then many of the factors that can affect the tournament, I highly recommend https://ncase.me/trust/, which is based on Robert Axelrod's the book `THE EVOLUTION OF COOPERATION`.

## What is this repository for?

I plan to run an Iterated Prisoner's Dilemma tournament among members of my extended family and friends. This repository will contain a (hopefully) short Python program to run such touraments.

I will create a template for the python code for the algorithms and write code for the 17 basic deterministic strategies from the literature (including the simplest imaginable strategies such as always defect). Thus we will have at least the basics covered.

Idea for the tournament is to create one or more algorithms and submit them, or choose an existing strategy and vote for it. If you wish to implement your own version of a strategy in the 17 I will provide, we will run that also. I suggest including your initials in the python filename of your algorithm to avoid name collisions.

Then I will have an extra-round-robin tournament in which each strategy plays versus each other strategy and (here is the extra part) also plays against itself.

I am aware that there is already existing software for this type of tournament such as https://evolution-outreach.biomedcentral.com/articles/10.1007/s12052-012-0434-x
* although the link to the code is broken
* ... even if link was not broken, it is more fun to write my own.

There is the possibility of sensitivity of tournament results to the values used to calculate the score (number of years of sentence) under the different choices. Let's call the two participants X and Y and their choices (`C` or `D`) are selected by the horizontal and vertical axes of the table, respectively. 

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; X <BR> `Y`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Cooperate | Defect |
| --- | --- | --- |
| **Cooperate** | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **R** <BR> `R`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **T** <BR> `S`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| **Defect** | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **S** <BR> `T`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **P** <BR> `P`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |

This tournament will be played under several different payoff ranges, each with `S` > `P` > `R` > `T`.

Personally, I find this `S` > `P` > `R` > `T` nomenclature a little hard to remember. I think of it (and the code refers to it) as the result a self-choice and an opponent-choice. Thinking of one of the participants as self and the other as opponent, here are the results as `self-choice`_`opponent-choice`:
* `C_D` = `S` = I nobly `cooperate` but my dastardly opponent `defects`
* `D_D` = `P` = I reluctantly follow my short-term best interests and `defect` and my dastardly opponent self-interestedly `defects` too
* `C_C` = `R` = I nobly `cooperate` and my opponent probably slips and chooses to `cooperate` too
* `D_C` = `T` = I slyly defect and my naive opponent cooperates

Another factor that can affect the tournament is the concept of errors. In the real world, sometimes factors intervene to prevent us from implementing the choice we made. This tournament will range through some percentage of these errors.

Another factor is the number of rounds per match. Again, this tournament will range through a range of rounds per match. If the number of rounds was known to be 10, you could have an algorithm always `defect` on the last round!
