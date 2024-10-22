print("Hello, Welcome to my computer quiz game!")

playing = input("Do you want to play the game?")

if playing != "Yes":
    quit()

print("Great, Lets play the game")
score = 0

response = input("What does OS stand for?")
if response.lower() == "operating system":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("Which OS are you using?")
if response.lower() == "windows 11":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does GPU stand for?")
if response.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does OTG stand for?")
if response.lower() == "on the go":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What is an ATM?")
if response.lower() == "automated teller machine":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does PDF stand for?")
if response.lower() == "portable document format":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does GPS stand for?")
if response.lower() == "global positioning system":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does HDMI stand for?")
if response.lower() == "high definition multimedia interface":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does LCD stand for?")
if response.lower() == "liquid crystal display":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does LED stand for?")
if response.lower() == "light emmiting diode":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What is Wi-Fi?")
if response.lower() == "wireless fidelity":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does GPRS stand for?")
if response.lower() == "general packet radio service":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does DVD stand for?")
if response.lower() == "digital versatile disc":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What is the brain of the computer?")
if response.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does RAM stand for in computing?")
if response.lower() == "random accesss memory":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("Which operating system is developed by Microsoft?")
if response.lower() == "windows":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does HTTP stand for?")
if response.lower() == "hypertext transfer protocol":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does GUI stand for?")
if response.lower() == "graphical user interface":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does BIOS stand for?")
if response.lower() == "basic input output system":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

response = input("What does SSD stand for?")
if response.lower() == "solid state drive":
    print("Correct!")
    score += 1
else:
    print("Oops, incorrect!")

print("Congrats!, Your final score is:", str(score), "/ 20")


