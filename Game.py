import random
computer = random.choice([-1,0,1])
print("\nWelcome to Snake, Water and Gun game")
print("s for Snake\nw for Water\ng for Gun")
youstr = input("Enter your choice: ")
youDict = {
  "s": 1,
  "w": -1,
  "g": 0,
}
reverseDict = {
  1: "Snake",
  -1: "Water",
  0: "Gun",
}
you = youDict[youstr]

print(f"You chose {reverseDict[you]},\nComputer chose {reverseDict[computer]}")

if(computer == you):
  print("It's a Draw")
  
else:
  if(computer == -1 and you == 1):
    print("You Win!")
  elif(computer == -1 and you == 0):
    print("You Lose!")
  elif(computer == 1 and you == -1):
    print("You Lose!")
  elif(computer == 1 and you == 0):
    print("You Win!")
  elif(computer == 0 and you == -1):
    print("You Win!")
  elif(computer == 0 and you == 1):
    print("You Lose!")
  else:
    print("Something went wrong!")

'''
Shorthand else code using logic on the basis of computer - you
if((computer - you) == 2 or (computer - you) == 1):
  print("You Win!")
else:
  print("You Lose!")
'''