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
	throw_at_object = input('>')

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

def bathroom():
	print("You walk into the room and take a look around the room")
	print(" you see a toilet")
	print(" and a vanity")
	print(" There is your shower and tub")
	print(" combination. Which do you choose")
	print("t = toilet, v = vanity, s = shower")
	choice = input("<")

def bathroomThrow():
	if choice == "t":
		toilet()
	if choice == "v":
		vanity()
	if chice == "s":
		shower()

def toilet():
	print("you hit the toilet and now")
	print(" There is porcelain all over the place")
	print(" You are sad because the toilet was expensive")
	print(" Though it was cathartic to hit something and")
	print(" see it smash into pieces, yes")
	print(" You start to feel better")

	

