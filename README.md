# Prisoner's Dilemma tournament

## What is the Prisoner's Dilemma?
* See https://en.wikipedia.org/wiki/Prisoner%27s_dilemma
* See https://cs.stanford.edu/people/eroberts/courses/soco/projects/1998-99/game-theory/axelrod.html

Merrill Flood and Melvin Dresher from RAND corporation framed the concept in 1950 to show why two completely rational individuals might not cooperate, even if it appears that it is in their best interests to do so.

There are many scenarios that can be mapped to this concept, but the famous mapping by Albert W. Tucker called the "Prisoner's Dilemma" revolves around two prisoners, "A" and "B", guilty of the same crime and being held in separate interrogation rooms.
* Due to weak evidence held by the police, if both cooperate (refuse to defect) that will lead to a very small sentence for each of them. If one cooperates and the other defects, the defector gets off free and the cooperator gets a large sentence. If they both defect, they both get an intermediate sentence.
* If the game is played only once, the game-theoretic best response is to defect (betray the other person).

Robert Axelrod, professor of political science at the University of Michigan, had the insight that if the game is played many times in succession, then the history of play allows each player to take into account the "reputation" of the other player in making their choice of behavior. He held tournaments of competing strategies for the Prisoner's Dilemma starting in 1980, and this led to a great deal of research.
* The "Tit-For-Tat" algorithm seemed to do the best.

## What is this repository for?

I plan to run a Prisoner's Dilemma tournament among members of my extended family and friends. This repository will contain a (hopefully) short Python program to run such touraments.

I will create a template for the python code for the algorithms and write code for the 17 basic deterministic strategies from the literature (including the simplest imaginable strategies such as always defect). Thus we will have at least the basics covered.

Idea for the tournament is to create one or more algorithms and submit them, or choose an existing strategy and vote for it. If you wish to implement your own version of a strategy in the 17 I will provide, we will run that also. I suggest including your initials in the python filename of your algorithm to avoid name collisions.

Then I will have an extra-round-robin tournament in which each strategy plays versus each other strategy and (here is the extra part) also plays against itself.

I am aware that there is already existing software for this type of tournament such as https://evolution-outreach.biomedcentral.com/articles/10.1007/s12052-012-0434-x
* although the link to the code is broken

... but it is more fun to write my own.
