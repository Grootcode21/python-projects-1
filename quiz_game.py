print("Hello, Welcome to my computer quiz game!")

playing = input("Do you want to play the game?")

if playing != "Yes":
    quit()

print("Great, Lets play the game")
score = 0

response = input("What does OS stand for?")
if response == "operating system":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("Which OS are you using?")
if response == "windows 11":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does GPU stand for?")
if response == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does OTG stand for?")
if response == "on the go":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What is an ATM?")
if response == "automated teller machine":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does PDF stand for?")
if response == "portable document format":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does GPS stand for?")
if response == "global positioning system":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does HDMI stand for?")
if response == "high definition multimedia interface":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does LCD stand for?")
if response == "liquid crystal display":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does LED stand for?")
if response == "light emmiting diode":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What is Wi-Fi?")
if response == "wireless fidelity":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does GPRS stand for?")
if response == "general packet radio service":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does DVD stand for?")
if response == "digital versatile disc":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What is the brain of the computer?")
if response == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does RAM stand for in computing?")
if response == "random accesss memory":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("Which operating system is developed by Microsoft?")
if response == "windows":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does HTTP stand for?")
if response == "hypertext transfer protocol":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does GUI stand for?")
if response == "graphical user interface":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does BIOS stand for?")
if response == "basic input output system":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does SSD stand for?")
if response == "solid state drive":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

print("Your final score is:", score, "/ 30")