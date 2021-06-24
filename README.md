# Calculate your birth year!
Ever wondered what your birth year was? That was the point of [this task](https://trello.com/c/26TGCH2Y).

The program will ask you for your name and your age. It will then try to work out the year you were born in and then ask you to confirm it was correct, if not it'll recalculate. Finally it'll let you know how many hours you've been alive!

Comments in the code will walk you through so you know what's going on.

This is also the first time we've seen `import` and `datetime` which both made this possible and futureproofed the program

## `birthyear.py`
First, `datetime` was imported
```python
import datetime
```
This will make it easier to do calculations based on time and futureproof the program.

Next, we'll ask the user for their name and their current age:
```python
name = input("What is your name? ")
age = int(input("How old are you in years? "))
```
Then, we'll assign the current year to a variable:
```python
now = datetime.date.today().year
```
Then we'll calulate their birth year using the current year and subtract their age:
```python
year_of_birth = now - age
```
...and for later in the program we'll calculate the hours alive too:
```python
hours_alive = age * (24 * 365)
```
Then we'll give the user a personalised message where we bring the above information all together
```python
print(f"OMG {name}, you are {age} years old. This means you were born in {year_of_birth}.")
```
But what if their birthday has already passed? We'll ask them and adjust the calculation accordingly:
```python
confirm = input("Unless, your birthday has passed? Has it?\nAnswer with yes or no: ")

if confirm.strip().lower() == "no":
    print(f"Good, enjoy the {year_of_birth} life!")
else:
    print(f"Sorry to hear you were actually born in {year_of_birth - 1}")
```
`else` simply just takes our inital year calculation then it subtracts 1 to get the year before!

Then we tell the user how many hours they've been alive based on their age:
```python
print(f"Just to let you know, you've been alive for {hours_alive} hours")
```
Then the program quits