# Mini Journal

Create a text-based mini journal, where the computer will ask you to tell it about your day and will save it to a text file along with today's date.

# Steps:
Take user input and today's date. Read about [datetime](https://docs.python.org/3/library/datetime.html).
```python
todays_date = datetime...
todays_thoughts = input("Tell me about today in a short sentence: ")
```
Append it to a text file.

# Hints:
  * Read about different file I/O methods. [Read, Write, Append](https://docs.python.org/3/tutorial/inputoutput.html).
  * Be careful with new line characters when appending to a file.

# Improvements:
* Add a tag section that take key words for that day and append it to the file along with date and text.
* Separate each day with a divider. `(e.g '-----------' or '===========')`
