import random

correct_number = random.randint(0, 5)
guess = None

while guess != correct_number:
  guess = int(input("Pick a number from 0-5: "))

  if guess == correct_number:
    print("Thats correct!")
    break
  
  else:
    print("No please try again")