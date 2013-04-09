import sys, computerMayhemRooms

def start():
	print("ComputerMayhem Version 1.0")
	intro()

def end():
	print("The end, You have done well")
	playAgain = input('play again(y/n)').lower()
	if playAgain == y :
		start()
	else: sys.exit()
		

def intro():
	print('You are a digurntled office worker who cant take it anymore.') 
	print('You sit all day in front of your computer')
	print('doing nothing and then you come home and sit in your') 
	print('computer until its time to go to be and do')
	print('everything over again. And you are tired of it.')
	print('You are Alaina and since you cant take your anger')
	print('Out on your work computer. You decide to destroy')
	print('You home computers.')
	condo()

def condo():
	print('You race home in your sports car. To your')
	print('fancy new condo to do some damage to your Electronics')
	print('Where do you want to go')
	print('b) bedroom', end=" ")
	print('L) livingroom', end=" ")
	print('a) bathroom', end=" ")
	print('k) kitchen', end=" ")
	print('g) game room')
	selectARoom = input('>')
	selectRoom(selectARoom)
	
	

def selectRoom(whichRoom):
	if whichRoom == 'b':
		print("bedroom")
		computerMayhemRooms.bedRoom()
	elif whichRoom == 'l':
		living_room()
	elif whichRoom == 'a':
		bath_room
	elif whichRoom == 'k':
		kitchen()
	elif whichRoom == 'g':
		game_room
	else:
		print('you have reached the end')
condo()

		
		
	

	