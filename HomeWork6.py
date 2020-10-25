"""
Homework #6 - (Advanced Loops)
DESCRIPTION:
Build a function using Nested Loops, where parameter for rows and columns are defined, which in turn would print a chess board on the terminal
when you run the application on.

Function is: DrawChessBoard(rows,columns).

"""

ver = "||"
hor = "  "

# These 4 'sub-functions', which will be used within the main function that will print the chessboard.

# The character 'ver', is used for all units in the chessboard EXCEPT the last one in the row from left to right.
def DrawFillSquare():
	for row in range(1):
		for col in range(1,6):
			print(ver, end = "")

# The character 'hor', is used for all units in the chessboard EXCEPT the last one in the row from left to right.
def DrawNoFillSquare():
	for row in range(1):
		for col in range(1,6):
			print(hor, end = "")

# This function prints one of the shapes, to form the first line in the unit of the character 'ver', for ONLY the last unit on the row.
def EndDrawFillSquare():
	for row in range(1):
		for col in range(1,6):
			if col == 5:
				print(ver)
			else:
				print(ver, end = "")

# This function prints one of the shapes, to form the first line in the unit of the character 'hor', for ONLY the last unit on the row.
def EndDrawNoFillSquare():
	for row in range(1):
		for col in range(1,6):
			if col == 5:
				print(hor)
			else:
				print(hor, end = "")

# Below is the function that draws the chessboard.
def DrawChessBoard(rows,column):
	for outrow in range(rows):
		for inrow in range(3):
			for outcol in range(column):
				if outcol == column-1:
					if column % 2 > 0:
						if outrow % 2 == 0:
							EndDrawFillSquare()
						else:
							EndDrawNoFillSquare()
						continue
					if outrow % 2 == 0:
						EndDrawNoFillSquare()
					else:
						EndDrawFillSquare()
					continue
				if outrow % 2 == outcol % 2:
					DrawFillSquare()
				else:
					DrawNoFillSquare()
	return True
# Calling the draw function using concrete values for parameters
DrawChessBoard(3,3)
