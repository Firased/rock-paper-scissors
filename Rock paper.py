import random
def Draw():
    print("Your play is : " + str(pp) +" | The computer play is : " + str(p)) 
    print("Its a draw")
    print("Restert the game")
def Win():
    print("Your play is : " + str(pp) +" | The computer play is : " + str(p)) 
    print("You have won this game!")
    print("Restert the game")
def Loss():
    print("Your play is : " + str(pp) +" | The computer play is : " + str(p)) 
    print("You have lost!")
    print("Restert the game")

pp = 0
input("Press enter to start")
while pp<1 or pp>3:
    pp = int(input("Choose your play \n[1]Scissor\n[2]Rock\n[3]Paper\n :"))
cp = ["Scissor" ,"Rock" ,"Paper"]
p = random.choice(cp)
if pp ==1:
    pp = "Scissor"
if pp ==2:
    pp="Rock"
if pp ==3:
    pp="Paper"


if pp == "Scissor"and p == "Paper":
    Win()
if pp == "Rock" and p == "Scissor":
    Win()
if pp == "Paper" and p == "Rock":
    Win()


if pp == "Paper" and p=="Scissor":
    Loss()
if pp == "Scissor" and p== "Rock":
    Loss()
if pp == "Rock" and p =="Paper":
    Loss()

if pp == p:
    Draw()

    


