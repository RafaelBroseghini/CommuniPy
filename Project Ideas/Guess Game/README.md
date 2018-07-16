# Guess Game

Create a text-based guess game, where the computer chooses an element from an array and the player tries to guess it, keeping track of the number of tries.

# Steps:
Initialize a variable 'tries' starting at 0.
```python
tries = 0
```

Create a list with words or use the [random](https://docs.python.org/3/library/random.html) module to choose a random number.
Choose a random word/number.
Take user input and cross-check with target word/number.
Keep checking until user guesses it right.

# Hints:
  * **It is easier to implement a guess number game since we can give feeback to the user if their guess was above or below the target number.**
  * If using words, it is harder to provide feedback.
    * Think having a list of used guesses.

# Improvements:
  * Prompting with colorama for beautified prompt. 
  * Depending on the number of tries it took the user to guess it, return a customized response.
```python
if tries = 20:
return "Wow, you were slow on this one!"
```
