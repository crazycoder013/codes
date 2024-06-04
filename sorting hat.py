# Write code below 💖
Q1 = int(input(" do you like Dawn(1) or dusk(2)"))
griff = int(0)
raven = int(0)
huffle = int(0)
slyth = int(0)
if Q1 == 1:
  griff = griff + 1
  raven = raven + 1
elif Q1 == 2:
  huffle = huffle + 1
  slyth = slyth + 1
else:
  print("Wrong input")
print("When i am dead I want people to remember me as")
print(" 1) the good")
print(" 2) the great")
print(" 3) the wise")
print(" 4) The bold")
Q2 = int(input(" enter your awnser (1-4)"))
if Q2 == 1:
  huffle = huffle + 2
elif Q2 == 2:
  slyth = slyth + 2
elif Q2 == 3:
  raven = raven + 2
elif Q2 == 4:
  griff = griff + 2
else:
  print("wrong input")
print("Which kind of instrument most pleases your ear")
print("1) violin")
print("2) trumpet")
print("3) piano")
print("4) the drum")
Q3 = int(input("Enter your awnser 1-4  "))
if Q3 == 1:
  slyth = slyth + 4
elif Q3 == 2:
  huffle = huffle + 4
elif Q3 == 3:
  raven = raven + 4
elif Q3 == 4:  
  griff = griff + 4
else:
  print("wrong output")
winner = ("none")
if griff > raven and griff > huffle and griff > slyth:
  print("Gryffindor")
elif raven > griff and raven > slyth and raven > huffle:
  print("Ravenclaw")
elif huffle > raven and huffle > slyth and huffle > griff:
  print("Hufflepuff")
else:
  print("Slytherin")