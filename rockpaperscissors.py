import random
for i in range(10):
  a = ["rock", "paper", "scissors"]
  b= random.choice(a)
  x=input("rock, paper, or scissors: ")
  print("You chose " + x + " and the computer chose " + b)
  if b == "rock" and x == "paper":
    print("you won")
    break
  elif b == "rock"  and x == "scissors":
    print(" you lost")
  elif b == "rock" and x == "rock":
    print("you tied")
  elif b == "paper" and x == "rock":
    print("you lost ")
  elif b == "paper" and x == "scissors":
    print("you won ")
    break
  elif b == "paper" and x == "paper":
    print("you tied")
  elif b == "scissors" and x == "rock":
    print("you won")
    break
  elif b == "scissors" and x == "paper":
    print("you lost")
  elif b == "scissors" and x == "scissors":
    print("you tied")
