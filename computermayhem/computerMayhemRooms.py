import sys 

def end():
	print("The end, You have done well")
	playAgain = input('play again(y/n)').lower()
	if playAgain == 'y' :
		start()
	elif playAgain == 'n':
		sys.exit()
	else: 
		print("what in the world are you doing here")

def die():
	print("You should not be here, something is wrong with")
	print('my code. Sorry, you get what you pay for.')
	

def bedRoom():
	print('You storm off to your bedroom.')
	print('You are at the door and to your right is your queen sized bed')
	print('And directly in front of you is your dresser with mirror.')
	print('Other than that your bedroom is empty.')
	print('Your expensive laptop is in your hand.')
	print('Do you?')
	print('t) Throw it at the bed d) dresser m) mirror')
	throw = input('>')
	bedRoomThrow(throw)

def bedRoomThrow(throw_at_object):
	if throw_at_object == 'd':
		dresserImpact()
	elif throw_at_object == 't':
		bedImpact() 
	elif throw_at_object == 'm':
		mirrorImpact()
	else: 
		die()
def dresserImpact():
	print("Hey, this is the dresser you got as a")
	print(" kid, you drop to your knees and weep.")
	print(" you, trhow your self on the bed and fall into")
	print(" a fitful sleep")

	
def bedImpact():
	print("Bam!!, Your bed took a direct hit.")
	print(" and is now smashed into 200 pieces.")
	print(" you scream and jump up and down.")
	print(" yay.")
	
def mirrorImpact():
	print(" How could you do that you hit a")
	print(" Mirror you know that is seven years")
	print(" of bad luck")

def bathRoom():
	print("You walk into the room and take a look around the room")
	print(" you see a toilet")
	print(" and a vanity")
	print(" There is your shower and tub")
	print(" combination. Which do you choose")
	print("t = toilet, v = vanity, s = shower")
	choice = input("<")
	bathroomThrow(choice)

def bathroomThrow(choice):
	if choice == "t":
		toilet()
	if choice == "v":
		vanity()
	if choice == "s":
		shower()

def toilet():
	print("you hit the toilet and now")
	print(" There is porcelain all over the place")
	print(" You are sad because the toilet was expensive")
	print(" Though it was cathartic to hit something and")
	print(" see it smash into pieces, yes")
	print(" You start to feel better")
	#end()
	
def vanity():
	print("How could you ever think of ever hitting your own vanity.")
	print(" you paid good more for it. You were in a fit of rage")
	print(" so you are forgiven. The vanity bursts into tiny pieces")
	print(" good for you.")
	
def shower():
	print("Bam, it's a direct hit on the shower.")
	print(" shower tiles go everywhere.")
	print(" its a mess. You, feel great. You will")
	print(" not be able to take a showr for awhile")
	
def livingRoom():
	print("Good for you, you chose the livingroom")
	print(" You have a couch")
	print(" A big screen tv")
	print(" You know you want to hit the fireplace")
	print(" Come on don't hit the pear bear rug.")
	print(" c for couch, t for tv, f for fireplace, r for rug")
	choiceL = input("<")
	livingRoomThrow(choiceL)
	
def livingRoomThrow(choiceL):
	if choiceL == 'c':
		couch()
	if choiceL == "t":
		television()
	if choiceL == 'f':
		fireplace()
	if choiceL == 'r':
		rug()

def couch():
	print("Oh, no you hit your nice couch.")
	print(" shame on you. You are happy now.")
	
def television():
	print("How could you destroy your big screen. ")
	print("now what will you do when your favoite ")
	print("shows are on. Go to your neighbors.")
	
def fireplace():
	print("Your fireplace was it and now you have released ")
	print("toxic smoke into the atmosphere. How selfish.")
	
def rug():
	print("What were you thinking throwing your laptop ")
	print("on a rug. It did shatter though.")
	
def kitchen():
	print("You look straight ahead and you see thekitchen cupboards ")
	print("You look left and you see you table")
	print("At right is the kitchen island")
	print("Also straight ahead is your sink")
	print("pres c = cupboards, t = table, i = island, s = sink")
	choiceK = input("<")
	kitchenThrow(choiceK)
	
def kitchenThrow(choiceK):
	if choiceK == 'c':
		cupboards()
	if choiceK == 't':
		table()
	if choiceK == 'i':
		island()
	if choiceK == 's':
		sink()

def cupboards():
	print("Hey, you are thrown your computer at antique wood.")
	print(" How dare you, but, they are yours so I can't tell you.")
	print(" What to do.")
	
def table():
	print("Your laptop smashes into pieces and your table is unharmed")
	print("To bad.")

def island():
	print("Taking your anger out on the kitchen island ")
	print(" You built with your own hands, thats a no no.")

def sink():
	print("Plastic hitting stainless steel. How did you. ")
	print("ever think that would do any damage.")
	print(" The laptop is eaten by the garbage disposal. ")
	print("You loose.")
	
# end of the first version of the game

def start():
	print("ComputerMayhem Version 1.0, \n" )
	intro()

def intro():
	print('You are a digurntled office worker who cant take it anymore.') 
	print('You sit all day in front of your computer')
	print('doing nothing and then you come home and sit in your') 
	print('computer until its time to go to be and do')
	print('everything over again. And you are tired of it.')
	print('You are Alaina and since you cant take your anger')
	print('Out on your work computer. You decide to destroy')
	print('You home computers.\n')
	condo()

def condo():
	print('You race home in your sports car. To your')
	print('fancy new condo to do some damage to your Electronics')
	print('Where do you want to go')
	print("bd) bedroom")
	print('l) livingroom')
	print('b) bathroom' )
	print('k) kitchen')
	#print('g) game room')
	selectARoom = input('>')
	selectRoom(selectARoom)
	
	
	
def selectRoom(whichRoom):
	if whichRoom == 'bd':
		bedRoom()
	elif whichRoom == 'l':
		livingRoom()
	elif whichRoom == 'b':
		bathRoom()
	elif whichRoom == 'k':
		kitchen()
	#elif whichRoom == 5:
		#computerMayhemRooms.gameRoom()
	else:
		print('Invalid selection please select 1=5, thank you.')
		end()
start()

	

	
	
	


	

	

