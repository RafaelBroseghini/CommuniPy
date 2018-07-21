# Chat Bot

Create a bot, where the computer will respond to the user based on specific inputs.
* Types of Bot:
    * Random Jokes Bot.
    * Chat Bot.
    * Daily Inspiration Bot.
    * Fun Facts about (you choose) Bot.

# Steps:
Have you Bot `return` a random quote, phrase, sentence etc upon running the program.
```python
>>> Why was the stadium so cold?
>>> Because there were a lot of fans.
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
