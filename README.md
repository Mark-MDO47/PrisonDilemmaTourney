# Prisoner's Dilemma tournament

## What is the Prisoner's Dilemma?
* See https://en.wikipedia.org/wiki/Prisoner%27s_dilemma
* See https://cs.stanford.edu/people/eroberts/courses/soco/projects/1998-99/game-theory/axelrod.html

Merrill Flood and Melvin Dresher from RAND corporation framed the concept in 1950 to show why two completely rational individuals might not cooperate, even if it appears that it is in their best interests to do so.

There are many scenarios that can be mapped to this concept, but the famous mapping by Albert W. Tucker called the "Prisoner's Dilemma" revolves around two prisoners, "A" and "B", guilty of the same crime and being held in separate interrogation rooms.
* Due to weak evidence held by the police, if both refuse to betray the other that will lead to a very small sentence for each of them. If one stays silent and the other betrays, the betrayer gets off free and the silent one gets a large sentence. If they both betray each other, they both get an intermediate sentence.
* (spoiler alert) If the game is played exactly one time, the game-theory best choice for each player is to betray the other player.

Robert Axelrod, professor of political science at the University of Michigan, held a tournament of competing strategies for the famous Prisoner's Dilemma in 1980.
* He had the insight that if the game is played many times in succession, then the history of play allows each player to take into account the "reputation" of the other player in making their choice of behavior.
* He invited some game theorists to submit algorithms that would be competed against each other in a computer tournament.
* Later he held another tournament and invited anyone to submit algorithms.
* The "Tit-For-Tat" algorithm seemed to do the best.

## What is this repository for?

I plan to run a Prisoner's Dilemma tournament among members of my extended family. This repository will contain a (hopefully) short Python program to run such touraments.

I am aware that there is already existing software for this such as https://evolution-outreach.biomedcentral.com/articles/10.1007/s12052-012-0434-x
* although I cannot follow the link to the code

... but it is more fun to write my own.
