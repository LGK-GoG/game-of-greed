# Game of Greed

**Authors**: Glenn Clark, Lauren Sierra, Kassie Bradshaw

**Version**: 1.0.0

**[Our whiteboard](https://lucid.app/lucidchart/e1fbad30-80be-4c91-a42e-96ce5bdd84a7/edit?referringApp=slack&shared=true&page=0_0#)**

## Overview

**[Our whiteboard](https://lucid.app/lucidchart/e1fbad30-80be-4c91-a42e-96ce5bdd84a7/edit?referringApp=slack&shared=true&page=0_0#)**

**A Command Line Version of the dice game 'Game of Greed'** - Also known as '10,000', 'Farkle', 'Zilch', 'Foo', 'Crap Out', and more

[Game rules](https://en.wikipedia.org/wiki/Dice_10000) / [Play game online](http://www.playonlinedicegames.com/farkle)

----

## Feature Tasks

### LAB 06

You’ll begin working in teams on a command line version of the dice game Game of Greed by expanding your understanding of Python standard library.

Today is all about tackling the highest risk and/or highest priority features - **scoring, dice rolling** and **banking of points**.

* [ ] Define a `GameLogic` class in `game_of_greed/game_logic.py` file.
* [ ] Handle calculating score for dice roll
  * [ ] Add `calculate_score` static method to GameLogic class.
  * [ ] The input to `calculate_score` is a tuple of integers that represent a dice roll.
  * [ ] The output from `calculate_score` is an integer representing the roll’s score according to **rules of game**.
  
* [ ] Handle rolling dice
  * [ ] Add `roll_dice` static method to GameLogic class.
  * [ ] The input to `roll_dice` is an integer between 1 and 6.
  * [ ] The output of `roll_dice` is a tuple with random values between 1 and 6.
  * [ ] The length of tuple must match the argument given to `roll_dice` method.

* [ ] Handle banking points
  * [ ] Define a `Banker` class
  * [ ] Add a `shelf` instance method
    * [ ] Input to `shelf` is the amount of points (integer) to add to shelf.
    * [ ] `shelf` should temporarily store **unbanked** points.
  * [ ] Add a `bank` instance method
    * [ ] `bank` should add any points on the **shelf** to total and reset shelf to 0.
    * [ ] `bank` output should be the amount of points added to total from shelf.
  * [ ] Add a `clear_shelf` instance method
    * [ ] `clear_shelf` should remove all unbanked points.

----

## Getting Started

* Clone repo to your local terminal
* Run a 'poetry install' to install dependencies
* Make sure you have a .gitignore included in your local version
  * If not, copy the content from [this link](https://github.com/codefellows/seattle-code-python-401n3/blob/main/.gitignore) into a .gitignore in your version 

----

## Architecture

----

## Tests

### LAB 06 Tests

**User Acceptance Tests** : Starter tests will be provided that cover cases listed below

* [ ] All tests must pass as written
* [ ] Additional tests are allowed

**Testing - Roll Dice**: When rolling 1 to 6 dice ensure…

* [ ] A sequence of correct length is returned
* [ ] Each item in sequence is an integer with value between 1 and 6

**Testing - Calculate Score**:

* [ ] zilch - roll with no scoring dice should return 0
* [ ] ones - rolls with various number of 1s should return correct score
* [ ] twos - rolls with various number of 2s should return correct score
* [ ] threes - rolls with various number of 3s should return correct score
* [ ] fours - rolls with various number of 4s should return correct score
* [ ] fives - rolls with various number of 5s should return correct score
* [ ] sixes - rolls with various number of 6s should return correct score
* [ ] straight - 1,2,3,4,5,6 should return correct score
* [ ] three_pairs - 3 pairs should return correct score
* [ ] two_trios - 2 sets of 3 should return correct score
* [ ] leftover_ones - 1s not used in set of 3 (or greater) should return correct score
* [ ] leftover_fives - 5s not used in set of 3 (or greater) should return correct score

**Testing - Banker**:

* shelf
  * [ ] should properly track unbanked points

* bank
  * [ ] should properly add unbanked points to total and return the deposited amount

* clear_shelf
  * [ ] should remove any unbanked points, resetting to zero.
  * [ ] should not affect previously banked points

----

## Change Log

**06-22-21**:

* Created initial setup for Lab 06, updated README to include feature tasks and requirements.
* Started basic scaffolding of classes and methods
* Input starter tests from class repo

----

## Collaboration and Credit
