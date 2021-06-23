# Game of Greed

**Authors**: Glenn Clark, Lauren Sierra, Kassie Bradshaw

**Version**: 1.0.0

**[Our whiteboard](https://lucid.app/lucidchart/e1fbad30-80be-4c91-a42e-96ce5bdd84a7/edit?referringApp=slack&shared=true&page=0_0#)**

## Overview

Today you’ll begin working in teams on a command line version of the dice game Game of Greed by expanding your understanding of Python standard library.

----

## Feature Tasks

### LAB 06

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

## Change Log

**06-22-21**:

* Created initial setup for Lab 06, updated README to include feature tasks and requirements.
