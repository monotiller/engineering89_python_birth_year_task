import datetime # importing a library that is designed to work with dates and times

name = input("What is your name? ") # Asks the user for their name
age = int(input("How old are you in years? ")) # Asks the user for their age in years
now = datetime.date.today().year # Assigns the current year to the value now for easier calculation
year_of_birth = now - age # Calculates the year of birth by simply taking the current year from the user's age
hours_alive = age * (24 * 365) # Calculates the amount of hours the user has been alive, nothing special, just multiplies hours in a day by days in a year

print(f"OMG {name}, you are {age} years old. This means you were born in {year_of_birth}.") # Dislpays the calculation to the user
confirm = input("Unless, your birthday has passed? Has it?\nAnswer with yes or no: ") # Asks the user if the year the program had guessed is correct

if confirm.strip().lower() == "no":
    print(f"Good, enjoy the {year_of_birth} life!") # Reiterates that they were born in the originally calculated year
else:
    print(f"Sorry to hear you were actually born in {year_of_birth - 1}") # Recalculates and displays the new year

print(f"Just to let you know, you've been alive for {hours_alive} hours") # Displays the amount of hours the user has been alive