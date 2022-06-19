import random

name = str(input("What is your name: "))
print(f"Welcome {name}")
answers = ['rock', 'paper', 'scissors']


while True:
  option = str(input("Would you like to play rock, paper scissors game? [Y/N]"))
  if option == "Y" or option == "y":
    while True:
      computerAns = random.choice(answers)
      ans = str(input("Rock, Paper or Scissors????: ")) 
      if ans == computerAns:
        print(computerAns)
        print("Its a draw")
        break
      elif ans == "rock" or ans == "Rock":
        if computerAns == "paper":
          print(f"Comnputer Ans: {computerAns}")
          print(f"Wow {name}, You have won!!!! ")
          break
        elif computerAns == "scissors":
          print(f"Comnputer Ans: {computerAns}")
          print(f"Too Bad You Have lost {name}")
          break
      elif ans == "scissors" or ans == "Scissors":
        if computerAns == "rock":
          print(f"Comnputer Ans: {computerAns}")
          print(f"Wow {name}, You have won!!!! ")
          break
        elif computerAns == "paper":
          print(f"Comnputer Ans: {computerAns}")
          print(f"Too Bad You Have lost {name}")
          break
      elif ans == "paper" or ans == "Paper":
        if computerAns == "scissors":
          print(f"Comnputer Ans: {computerAns}")
          print(f"Wow {name}, You have won!!!! ")
          break
        elif computerAns == "rock":
          print(f"Comnputer Ans: {computerAns}")
          print(f"Too Bad You Have lost {name}")
          break
      else:
        print("Please enter a valid option: ")
  elif option == "n" or option == "N" :
    print("Alright See You Next Time!!!")
    exit()

  else:
    print("Please enter a valid option")




