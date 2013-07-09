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
		mirrowImpact()
	else: 
		die()
def dresserImpact():
	print("Hey, this is the dresser you got as a")
	print("kid, you drop to your knees and weep.")
	print("you, trhow your self on the bed and fall into")
	print("a fitful sleep")
	

	

