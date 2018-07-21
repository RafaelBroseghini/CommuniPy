# Chat Bot

Create a bot, where the computer will respond to the user based on specific inputs.
* Types of Bot:
    * Random Jokes Bot.
    * Chat Bot.
    * Daily Inspiration Bot.
    * Fun Facts about (you choose) Bot.

# Steps:
Have your Bot `return` a random quote, phrase, sentence etc upon running the program.
```python
"Bot asks: Why was the stadium so cold?"
"Bot responds: Because there were a lot of fans."
```
---

```python
"Bot says: Why do the French eat snails?"
"Bot impatiently responds: Because they don't like fast food."
```
Create a pre defined set of accepted inputs.
This can be done with simple `if` statements.
```python
if user_input == "hey":
    print(random.choice(["Hello!", "Wassup!", "Good to have you here!"])
else:
    print("I'm not that smart. I did not understand what you said.")
```
Repeat this process as many times as you would like as you progress through a chat with your bot.

# Hints:
  * Use a main while loop such that the Bot keeps asking you questions until user enters 'stop' for example.

# Improvements:
  * Prompting with Colorama for beautified prompt.
  * Read about NLP with TextBlob. [TextBlob Tutorial](https://www.analyticsvidhya.com/blog/2018/02/natural-language-processing-for-beginners-using-textblob/).
  * Use `time.sleep(...)` to set up a timer between bot asking question and bot responding."
