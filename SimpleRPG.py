import time
import random

#################
#               #
# // classes \\ #
#               #
#################
class Monsters:
  def __init__(self,name,hp,dmg):
    self.name = name
    self.hp = hp
    self.dmg = dmg
class Cmbclasss:
  def __init__(self,name,hp):
    self.name = name
    self.hp = hp
############
slime = Monsters("Slime", 15, random.randint(1,3))
slimeStatus = f"{slime.name} - {slime.hp}HP"
wolf = Monsters("Wolf", 25, random.randint(3,5))
wolfStatus = f"{wolf.name} - {wolf.hp}HP"
####
tank1 = Cmbclasss("Tank", 25)
berserker1 = Cmbclasss("Berserker", 20)
knight1 = Cmbclasss("Knight", 20)
tank = f"{tank1.name} - {tank1.hp}HP"
berserker = f"{berserker1.name} - {berserker1.hp}HP"
knight = f"{knight1.name} - {knight1.hp}HP"
#######
begginerSword = ['BegginnerSword', random.randint(2, 5)]
garen = "Garen -> "

def sleep():
	time.sleep(2)

user = input(
    f"??? -> hello adventeror, I'm Garen! what can I call a young lad like you? \n"
)
sleep()
print(f"{garen}so its the... AMAZING {user.upper()}?!")
sleep()
print(f"{user} -> ???")
sleep()
print(
    f"{garen} *cough* sorry... i was just trying to lighten the mood... you know what never mind -_-"
)
sleep()
print(
    "[Thats right... the mood here is a bit gloomy, currently you stand in a empty battlefriend, you came here to be recruited into a new job... the Adventeror.]"
)
sleep()
################
#choosing class#
################
while True:
	cmbclass = input(
	    f"{garen}so kind of combat style do you wish to learn?\n[Tank][Berserker][Knight]\n"
	)
	sleep()
	if cmbclass.lower() == "tank":
		cmbclass = tank
		print(f"{cmbclass.name}? good choice...")
		sleep()
		break
	elif cmbclass.lower() == "berserker":
		cmbclass = berserker
		print(f"{cmbclass.name}? good choice...")
		sleep()
		break
	elif cmbclass.lower() == "knight":
		cmbclass = knight
		print(f"{cmbclass.name}? good choice...")
		break
	else:
		sleep()
		print(f"[{cmbclass} Is an invalid entry... try again.]")
		sleep()
sleep()
print(f"{garen}well lets just get started... here take this")
sleep()
print(f"[You receive an ordinary looking sword from Garen.]")
sleep()

userINV = []
userINV.append(begginerSword[0])
while True:
	user_input = input("[try typing inventory]\n")
	if user_input.lower() == "inventory":
		print(userINV)
		break
	elif user_input.lower != "inventory":
		print(f"[{user_input} Is an invalid command]")

sleep()
print(f"{garen}now go over there and attack that slime!")
sleep()
print("[Garen points to a medium sized cage which houses a few slime]")
sleep()
while True:
	user_input = input("[Do you wish to attack the slime? type -> [Yes][No]\n")
	sleep()
	if user_input.lower() == "yes":
		break
	elif user_input.lower() == "no":
		sleep()
		print(
		    f"{garen}what do you mean no?! just get over there {user}!\n[seems you don't really have a choice...]"
		)
		break
	elif user_input.lower() != "yes":
		print("the command you entered is not valid, try again.")
		sleep()
sleep()
print("You head over and engage combat.")
sleep()
print(slimeStatus)
sleep()
print(cmbclass)
