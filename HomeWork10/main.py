'''

Homeword Assignment #10, in the Python is Easy course with Pirple. 

Import a library, study it and shows its capabilities either in an app or in code samples using its imported functions. 

Extra credit is to create a blog about the library. 

I will be showing the logging module which I found interesting, by applying it to one of the previous projects done in this course.

The project I will apply the logging (including error handling) to, is Connect 4 - because when I created the Connect 4 game earlier on in the course,
I had to build in a whole lot of IF statements to avoid the Index errors (just so the game could work).

So with Logging and Error Handling, I hope to make the Connect 4 code more efficient. 

The code below is a deliverable for two different homework assignments - I have just changed the description above slightly and published in differet Github repo's. 

'''


import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create format
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Configure logger
logging.basicConfig(
    filename = "test.log", 
    level= logging.DEBUG, 
    format=log_format
    )

# test logger
# logging.debug("this is a debug message")
# logging.info("this is an info message")
# logging.warning('This is a warning')
# logging.error('This is an error',exc_info=True)
# logging.critical("this is a critical message")

# Connect 4 game code 


def drawGamepPlay(move):
	for row in range(7): 
		for col in range(16):
			columnNumber = int((col+1)/2)
			if col == 15:
				print(" ")
				break
			if row == 6:
				if col%2 ==0:
					print(" ",end="")
				else:
					print(columnNumber,end="")
				continue
			if col%2 == 0:
				print("|",end="")
			else:
				print(move[columnNumber-1][row],end="")

GameStatus = [["_","_","_","_","_","_"],["_","_","_","_","_","_"],["_","_","_","_","_","_"],["_","_","_","_","_","_"],["_","_","_","_","_","_"],["_","_","_","_","_","_"],["_","_","_","_","_","_"]]

Player = 1
# winnerCounter = 0
drawGamepPlay(GameStatus)
# print(winnerCounter)
import sys
import os


def checkline1_1():
	logging.debug("Check line 1_1 for win.")
	if GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot] == GameStatus[int(playermove)+1][colslot] == GameStatus[int(playermove)+2][colslot]:
		#print("1.1")
		logging.debug("Entering to winner function for line 1_1")
		winner()
def checkline1_2():
	logging.debug("Check line 1_2 for win.")
	if GameStatus[int(playermove)-2][colslot] == GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot] == GameStatus[int(playermove)+1][colslot]:
		#print("1.2")
		logging.debug("Entering to winner function for line 1_2")
		winner()
def checkline1_3():
	logging.debug("Check line 1_3 for win.")
	if GameStatus[int(playermove)-3][colslot] == GameStatus[int(playermove)-2][colslot] == GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot]:
		#print("1.3")
		logging.debug("Entering to winner function for line 1_3")
		winner()
def checkline1_4():
	logging.debug("Check line 1_4 for win.")
	if GameStatus[int(playermove)-4][colslot] == GameStatus[int(playermove)-3][colslot] == GameStatus[int(playermove)-2][colslot] == GameStatus[int(playermove)-1][colslot]:
		#print("1.4")
		logging.debug("Entering to winner function for line 1_4")
		winner()
def checkline2_1():
	logging.debug("Check line 2_1 for win.")
	if GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)-1][colslot+1] == GameStatus[int(playermove)-1][colslot+2] == GameStatus[int(playermove)-1][colslot+3]:
		#print("2.1")
		logging.debug("Entering to winner function for line 2_1")
		winner()
def checkline3_1():
	logging.debug("Check line 3_1 for win.")
	if GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot-1] == GameStatus[int(playermove)+1][colslot-2] == GameStatus[int(playermove)+2][colslot-3]:
		#print("3.1")
		logging.debug("Entering to winner function for line 3_1")
		winner()
def checkline3_2():
	logging.debug("Check line 3_2 for win.")
	if GameStatus[int(playermove)-2][colslot+1] == GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot-1] == GameStatus[int(playermove)+1][colslot-2]:
		#print("3.2")
		logging.debug("Entering to winner function for line 3_2")
		winner()
def checkline3_3():
	logging.debug("Check line 3_3 for win.")
	if GameStatus[int(playermove)-3][colslot+2] == GameStatus[int(playermove)-2][colslot+1] == GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot-1]:
		#print("3.3")
		logging.debug("Entering to winner function for line 3_3")
		winner()
def checkline3_4():
	logging.debug("Check line 3_4 for win.")
	if GameStatus[int(playermove)-4][colslot+3] == GameStatus[int(playermove)-3][colslot+2] == GameStatus[int(playermove)-2][colslot+1] == GameStatus[int(playermove)-1][colslot]:
		#print("3.4")
		logging.debug("Entering to winner function for line 3_4")
		winner()
def checkline4_1():
	logging.debug("Check line 4_1 for win.")
	if GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot+1] == GameStatus[int(playermove)+1][colslot+2] == GameStatus[int(playermove)+2][colslot+3]:
		#print("4.1")
		logging.debug("Entering to winner function for line 4_1")
		winner()
def checkline4_2():
	logging.debug("Check line 4_2 for win.")
	if GameStatus[int(playermove)-2][colslot-1] == GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot+1] == GameStatus[int(playermove)+1][colslot+2]:
		#print("4.2")
		logging.debug("Entering to winner function for line 4_2")
		winner()
def checkline4_3():
	logging.debug("Check line 4_3 for win.")
	if GameStatus[int(playermove)-3][colslot-2] == GameStatus[int(playermove)-2][colslot-1] == GameStatus[int(playermove)-1][colslot] == GameStatus[int(playermove)][colslot+1]:
		#print("4.3")
		logging.debug("Entering to winner function for line 4_3")
		winner()
def checkline4_4():
	logging.debug("Check line 4_4 for win.")
	if GameStatus[int(playermove)-4][colslot-3] == GameStatus[int(playermove)-3][colslot-2] == GameStatus[int(playermove)-2][colslot-1] == GameStatus[int(playermove)-1][colslot]:
		#print("4.4")
		logging.debug("Entering to winner function for line 4_4")
		winner()

def winner():
	logging.debug("Entered into 'winner' function.")
	os.system("cls")
	print("=========================\n\nGAME OVER!.\n")
	drawGamepPlay(GameStatus)
	print("\nPlayer",Player,"WINS!\n=========================")
	# drawGamepPlay(GameStatus)
	# print("\n\nGAME OVER! \n\nPlayer",Player,"WINS!")
	# winnerCounter = 1
	# if winnerCounter == 1:
	exit()
	# return winnerCounter
	# quit()
	# raise SystemExit
	# print("not exited ... should have though... should not be seeing this message.")

checkLineList = [checkline1_1,checkline1_2,checkline1_3,checkline1_4,checkline2_1,checkline3_1,checkline3_2,checkline3_3,checkline3_4,checkline4_1,checkline4_2,checkline4_3,checkline4_4]

def checkwin():
	logging.debug("Entered into 'checkwin' function.")
	# winnerCounter = 0
	for y in range(7):
		for x in range(5,-1,-1):
			if int(playermove)-1 == y and colslot == x:
				for c in checkLineList:
					logging.debug("Entering into try in 'checkwin' function.")
					try:
						c()
					# print("try reached...")
					# checkline1_1()
					# checkline1_2()
					# checkline1_3()
					# checkline1_4()
					# checkline2_1()
					# checkline3_1()
					# checkline3_2()
					# checkline3_3()
					# checkline3_4()
					# checkline4_1()
					# checkline4_2()
					# checkline4_3()
					# checkline4_4()
					except SystemExit:
						# print("system exit reached")
						sys.exit()
					except IndexError:
						logging.debug("Entered into index error. Column: ")
						pass
					except:
						logging.debug("Unaccounted Exception error in checkwin function",exc_info=True)
						pass
						# print("except no counted for reached")



				# below are the IF statements used to avoid errors.

				# if y == 0 and x > 2:
				# 	checkline1_1()
				# 	checkline3_1()
				# 	#print("WINNER118")
				# if y == 1 and x > 2:
				# 	checkline1_1()
				# 	checkline1_2()
				# 	checkline3_1()
				# 	#print("WINNER123")
				# 	if x < 5:
				# 		checkline3_2()
				# 	#	print("WINNER126")
				# 		if x < 4:
				# 			checkline4_2()
				# 	#		print("WINNER129")
				# if y == 2 and x > 2:
				# 	checkline1_1()
				# 	checkline1_2()
				# 	checkline1_3()
				# 	checkline3_1()
				# 	#print("WINNER135")
				# 	if x < 5:
				# 		checkline3_2()
				# 	#	print("WINNER138")
				# 		if x < 4:
				# 			checkline3_3()
				# 	#		print("WINNER141")					
				# if y == 3 and x > 2:
				# 	checkline1_1()
				# 	checkline1_2()
				# 	checkline1_3()
				# 	checkline1_4()
				# 	checkline3_1()
				# 	checkline4_4()
				# 	#print("WINNER149")
				# 	if x < 5:
				# 		checkline3_2()
				# 		checkline4_3()
				# 	#	print("WINNER153")
				# 		if x < 4:
				# 			checkline3_3()
				# 			checkline4_2()
				# 	#		print("WINNER157")
				# if y == 4 and x > 2:
				# 	checkline1_2()
				# 	checkline1_3()
				# 	checkline1_4()
				# 	checkline4_4()
				# 	#print("WINNER163")
				# 	if x < 5:
				# 		checkline4_3()
				# 	#	print("WINNER166")
				# 		if x < 4:
				# 			checkline4_2()
				# 	#		print("WINNER169")
				# if y == 5 and x > 2:
				# 	checkline1_3()
				# 	checkline1_4()
				# 	checkline4_4()
				# 	#print("WINNER174")
				# 	if x < 5:
				# 		checkline4_3()
				# 	#	print("WINNER177")
				# if y == 6 and x > 2:
				# 	checkline1_4()
				# 	checkline4_4()
				# 	#print("WINNER181")
				# if y == 3 and x < 3:
				# 	checkline1_1()
				# 	checkline1_2()
				# 	checkline1_3()
				# 	checkline1_4()
				# 	checkline2_1()
				# 	checkline3_4()
				# 	checkline4_1()
				# 	#print("WINNER190")
				# 	if x > 0:
				# 		checkline3_3()
				# 		checkline4_2()
				# 	#	print("WINNER194")
				# 		if x > 1:
				# 			checkline3_2()
				# 			checkline4_3()
				# 	#		print("WINNER198")							
				# if y == 2 and x < 3:
				# 	checkline1_1()
				# 	checkline1_2()
				# 	checkline1_3()
				# 	checkline2_1()
				# 	checkline4_1()
				# 	#print("WINNER205")
				# 	if x > 0:
				# 		checkline3_3()
				# 		checkline4_2()
				# 	#	print("WINNER209")
				# 		if x > 1:
				# 			checkline3_2()
				# 			checkline4_3()
				# 	#		print("WINNER213")
				# if y == 1 and x < 3:
				# 	checkline1_1()
				# 	checkline1_2()
				# 	checkline2_1()
				# 	checkline4_1()
				# 	#print("WINNER219")
				# 	if x > 0:
				# 		checkline4_2()
				# 	#	print("WINNER222")
				# 		if x > 1:
				# 			checkline3_2()
				# 	#		print("WINNER225")		
				# if y == 0 and x < 3:
				# 	checkline1_1()
				# 	checkline2_1()
				# 	checkline4_1()
				# 	#print("WINNER230")					
				# if y == 4 and x < 3:
				# 	checkline1_2()
				# 	checkline1_3()
				# 	checkline1_4()
				# 	checkline2_1()
				# 	checkline3_4()
				# 	#print("WINNER237")
				# 	if x > 0:
				# 		checkline3_3()
				# 		checkline4_2()
				# 	#	print("WINNER241")
				# 		if x > 1:
				# 			checkline4_3()
				# 			checkline3_2()
				# 	#		print("WINNER245")
				# if y == 5 and x < 3:
				# 	checkline1_3()
				# 	checkline1_4()
				# 	checkline2_1()
				# 	checkline3_4()
				# 	#print("WINNER251")
				# 	if x > 0:
				# 		checkline3_3()
				# 	#	print("WINNER254")
				# 		if x > 1:
				# 			checkline4_3()
				# 	#		print("WINNER257")
				# if y == 6 and x < 3:
				# 	checkline1_4()
				# 	checkline2_1()
				# 	checkline3_4()
				# 	#print("WINNER263")


while(True):
	# drawGamepPlay(GameStatus)
	try:
		print("=========================\n\nPlayers Turn:", "Player",Player)
		playermove = input("Select column: ")
		if GameStatus[int(playermove)-1][0] != "_":
			os.system("cls")
			print("=========================\n\nCareful! Column",playermove,"is full.\n")
			drawGamepPlay(GameStatus)
			print("\nChoose a column with at least one empty space!")
			continue
		colslot = -1
		if Player == 1:
			for n in GameStatus[int(playermove)-1]:
				if n == "_":
					colslot += 1
					if colslot == 5:
						GameStatus[int(playermove)-1][colslot] = "X"
						checkwin()
						Player = 2
						break
				else:
					GameStatus[int(playermove)-1][colslot] = "X"
					checkwin()
					Player = 2
					break
		else:
			for n in GameStatus[int(playermove)-1]:
				if n == "_":
					colslot += 1
					if colslot == 5:
						GameStatus[int(playermove)-1][colslot] = "O"
						checkwin()
						Player = 1
						break
				else:
					GameStatus[int(playermove)-1][colslot] = "O"
					checkwin()
					Player = 1
					break
		os.system("cls")
		print("=========================\n\nYou are playing Connect 4.\n")
		drawGamepPlay(GameStatus)
		print("\nChoose your next column wisely! ")
	except IndexError:
		os.system("cls")
		print("=========================\n\nCareful! You entered: ",playermove,". There's no such column!\n")
		drawGamepPlay(GameStatus)
		print("\nChoose a column from 1 to 7!")
		continue
	except ValueError:
		os.system("cls")
		print("=========================\n\nCareful! You entered: ",playermove,". There's no such column!\n")
		drawGamepPlay(GameStatus)
		print("\nChoose a column from 1 to 7!")
		continue
	except SystemExit:
		sys.exit()
	except:
		logging.debug("Unaccounted Exception error in While loop function",exc_info=True)
		continue