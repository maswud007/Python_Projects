print("welcome to my quiz game project.\nHere I will ask you five questions on computer science.\nYou have to answer all of the questions.\n"
      "Do you want to play? I'm sure it will be fun :)  \n")
answer = input("If you want to play then type YES . Otherwise the game will be terminated :( ")
if answer.lower() != 'yes':
    print("OOPS, I got hurt. Hope You play next time :) ")
    quit()
else:
    print("That's great. Let's fun :) ")
score = 0

answer = input("what is the full form of EPROM?")
if answer.lower() == 'erasable programmable read only memory':
    print("Great! That's correct!")
    score += 1
else:
    print("Oppppps, That's incorrect")

answer = input("what is the full form of API?")
print(answer.lower())
if answer.lower() == 'application programming interface':
    print("Great! That's correct!")
    score += 1
else:
    print("Oppppps, That's incorrect")

answer = input("what is the full form of HDD?")
if answer.lower() == 'hard disk drive':
    print("Great! That's correct!")
    score += 1
else:
    print("Oppppps, That's incorrect")

answer = input("what is the full form of GPU?")
if answer.lower() == 'graphics processing unit':
    print("Great! That's correct!")
    score += 1
else:
    print("Oppppps, That's incorrect")

answer = input("what is the full form of SSD?")
if answer.lower() == 'solid state drive':
    print("Great! That's correct!")
    score += 1
else:
    print("Oppppps, That's incorrect")

print("you have scored " + str(score) + " out of five")
print("you have scored " + str(score/5*100) + "%")






