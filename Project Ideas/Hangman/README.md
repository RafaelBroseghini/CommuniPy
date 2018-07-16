# Hangman

Create a text-based hangman game, where the computer chooses a word and the player tries to guess it, but if they make too many wrong guesses, they lose.

# Steps:
Initialize a variable 'tries' that references the number of allowed tries in this game.
```python
tries = 5
```
Create a list with words in it. (either from text file, or manually populate list)
```python
with open("words.txt","r") as file:
    words = [word.strip() for word in file]
```
Choose a random word from the list.
```python
chosen_word = random.choice(words)
```
Take user input and cross-check with target word.
```python
for letter in range(len(word)):
    if user_choice == word[letter]:
        word[letter] = user_choice
```
 * Store used words in a list and check if user input is in this list. If true, ask for user input again.
 * Count number of tries. (Only decrease number of tries, if guess is wrong.)

# Hints:
  * Turn chosen_word into a list itself, so you can reassign indexes to correct guesses.

# Improvements:
  * Prompting with colorama for beautified prompt. 
  * Implement difficulty setting based on word length.
