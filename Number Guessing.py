import random

computerAns = random.randint(1, 100)

while True: 
  
  playerAns = int(input("Enter a number range from 1 - 100: "))

  if playerAns == computerAns:
    print("Congrats you found the correct number")
    break
  elif playerAns < computerAns:
    print("Try Guessing Higher Number")
  elif playerAns > computerAns:
    print("Try Guessing Lower Number")
  else:
    print("Please Try Guessing Again")

