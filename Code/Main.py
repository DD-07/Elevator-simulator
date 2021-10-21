import random
let levels = ["1","2","3","4","5","6","7","8"]

print("Welcome to elevator simulator! Which floor would you like to board?")
print(levels)

while True:
  print("You're currently at the ground floor")
  level_chosen = input("Answer below:"))
  if level_chosen == "1":
    Facts1 = ["In Germany and Austria, one is the grade for 'very good'", "in French playing cards the Aces are marked with a '1' rather than an 'A'.", 
              "1 is the exact amount of butler schools in the US", "1 is the number of public telephones in Kabul."]
    randomNo1 = random.randint(0,3)
    print(Facts1[randomNo1])
    input("What level would you like to go to next?")
  elif level_chosen == "2":
    Facts1 = ["In Germany and Austria, one is the grade for 'very good'", "in French playing cards the Aces are marked with a '1' rather than an 'A'.", 
              "1 is the exact amount of butler schools in the US", "1 is the number of public telephones in Kabul."]
    randomNo1 = random.randint(0,3)
    print(Facts1[randomNo1])
    input("What level would you like to go to next?")
 
  
