print("Welcome to Treasure Island. Your mission is to find the treasure")
option = input ("Enter your option 'right' or 'Left':?").lower()
if option == ('l'):
 option = input ("Enter your option 'swim' or 'wait':?").lower()
 if (option == 'w'):
  option = str(input ("Enter your option Which door:?")).lower()
  if(option == "Blue"):
   print ("Eaten by beasts.Game Over.")
  elif(option == "yellow"):
   print("you win")
  elif(option == "Red"):
   print("Burned by fire. Game Over.")
  else:
   print("Game Over.")
 else:
  print("Attacked by trout.Game Over.")
else:
 print("Fall into a hole. 'Game Over'.")
