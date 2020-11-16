# Guessing game

## Story

Your friend Victor has done some kind of game in Python but he did it in a
somewhat ugly way (no offense, Victor only started coding a couple of weeks ago).

As writing easy-to-understand and easy-to-maintain (in short: *clean*) code is
really important in programming, it's your job to help him to make his
code more readable and maintainable!



## What are you going to learn?

- code comprehension (understand written code)
- clean code refactoring (making code more easy to read and maintain
  without changing any feature)

## Tasks

1. Read the code and try to understand first without running it. Use comments to write in the next to the code what you understand from it. Commit and push your work. Remove the comments after pushing.
**Disclamier**: In real life *you shouldn't comment your program this way*. For a real programmers `starting_number = 5` is something obvious. This task is just to check if it's obvious for you too.
    - Every line of the program has comments next to it describing what's going on in it.
Example comments:
```python
starting_number = 5 # assign 5 to variable starting_number
numbers = [1, 2, 3] # initialize list with values and assign it to variable numbers
for number in numbers: # loop through list numbers (assign each value to variable number)
```
    - Comments use proper technical language, are short and specific enough to understand what's going on
    - One sentence comment is added at the top of the file describing what this program does
    - The modifications are committed with the commit message "add code comprehension comments" and pushed into the remote repository

2. Make the program more easy to understand and more easy to modify (maintain). Do it step by step and commit after each modification. Push your changes.
    - Running the program results in the exact same behavior before and after refactoring.
    - Variable names in the program are meaningful nouns and not abbreviated
    - Function names in the program are meaningful verbs and not abbreviated
    - There are no unnecessary (dead) code or comments in the program
    - There are no duplicating code parts or code parts doing the same thing differently in the program
    - There are no function that doing more than one thing in the program
    - After each modification the changes are committed, the program is runnable and results in the exact same behavior than at the beginning
    - Commit messages are meaningful

## General requirements

None

## Hints

- Always keep the features of the original code (don't even change a dot or newline).
- Always keep the code in a runnable state.
- Commit early commit often.
- Pay attention to create not only readable but maintainable code as well.

## Starting your project



## Background materials

- <i class="far fa-exclamation"></i> [Basics of clean code](project/curriculum/materials/pages/general/clean-code.md)
- <i class="far fa-exclamation"></i> [Refactoring in action](project/curriculum/materials/pages/general/refactoring-in-action.md)
- <i class="far fa-exclamation"></i> About [nice commit messages](https://chris.beams.io/posts/git-commit/)
- <i class="far fa-exclamation"></i> How to use [Math.random()](https://www.educative.io/edpresso/how-to-use-the-mathrandom-method-in-java)
- <i class="far fa-exclamation"></i> How to use [Random.nextInt()](https://www.javatpoint.com/post/java-random-nextint-method)
