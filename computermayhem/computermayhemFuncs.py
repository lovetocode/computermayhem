import sys, computerMayhemRooms

def end():
	print("The end, You have done well")
	playAgain = input('play again(y/n)').lower()
	if playAgain == 'y' :
		start()
	elif playAgain == 'n':
		sys.exit()
	else: 
		print("what in the world are you doing here")

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
		computerMayhemRooms.bedRoom()
	elif whichRoom == 'l':
		computerMayhemRooms.livingRoom()
	elif whichRoom == 'b':
		computerMayhemRooms.bathRoom()
	elif whichRoom == 'k':
		computerMayhemRooms.kitchen()
	#elif whichRoom == 5:
		#computerMayhemRooms.gameRoom()
	else:
		print('Invalid selection please select 1=5, thank you.')
		#end()
condo()

		
		
	

	