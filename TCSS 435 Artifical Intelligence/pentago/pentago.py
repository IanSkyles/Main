
#initialGameBoard will be 2d array with 4 arrays of 9
gameBoardState = [['-','-','-','-','-','-','-','-','-'],
				['-','-','-','-','-','-','-','-','-'],
				['-','-','-','-','-','-','-','-','-'],
				['-','-','-','-','-','-','-','-','-']]


#A method that itterates through the gameBoard and prints each block
# 1,2,3 of gb 1 then | then 1,2,3 of gb 2 then
# 4,5,6 of gb 1 then | then 4,5,6 of gb 2 then
# 7,8,9 of gb 1 then | then 7,8,9 of gb 2 then
#repeat for gb 3 and 4
def printBoard(gameBoard):
	#partition Array representation of gameblocks
	topLeft = 0
	topRight = 1
	bottomLeft = 2
	bottomRight = 3
	print ("+-------+-------+")
	printTwoBlocks(topLeft,topRight,gameBoard)
	print ("+-------+-------+")	
	printTwoBlocks(bottomLeft,bottomRight,gameBoard)
	print ("+-------+-------+")

def printTwoBlocks(firstBlock, secondBlock,gameBoard):
	for partitionRow in range (0,3):
		print ("|"),
		#firstGameBlock
		for partitionCol in range(0,3):
			print(gameBoard[firstBlock][partitionCol + partitionRow * 3]),
		print ("|"),
		#secondGameBlock
		for partitionCol in range(0,3):
			print(gameBoard[secondBlock][partitionCol + partitionRow * 3]),
		print ("|")

#needs to get input from user
#format will be block/position blockDirection
#eg 3/8 1R or 2/4 3L
def getMoveFromUser(gameBoard):
	while True:
		try:
			print ("Your move? (You will have to repeat if not formatted correctly)")
			print ("put in format block/position blockDirection")
			move = raw_input("eg 3/8 1R or 2/4 3L")
			#print (move.split(' '))
			move = move.split(' ')
			# print(move[0][0])
			# print(move[0][2])
			# print(move[1][0])
			# print(move[1][1])
			if isInputValidSquare(int(move[0][0]),int(move[0][2]),gameBoard):
				#print("here")
				if isInputValidRotation(int(move[1][0]),move[1][1]):
					#print("here")
					break
					
		except Exception as e:
			print ("")
			print "Incorrect format"
			print("")
	return ([[int(move[0][0]),int(move[0][2])],[int(move[1][0]),move[1][1]]])


def isInputValidSquare(gameBoardNumber,pieceNumber,gameBoard):
	numberList = [1,2,3,4,5,6,7,8,9]
	gameBoardList = [1,2,3,4]
	#check if input is valid gameBoard
	#print (gameBoardNumber)
	#print (gameBoardNumber in gameBoardList)
	if gameBoardNumber in gameBoardList:
		#print("here")
		#if valid piece position
		if pieceNumber in numberList:
			#print("here")
			#print (gameBoard[gameBoardNumber-1][pieceNumber-1])
			#if move not already taken
			if gameBoard[gameBoardNumber-1][pieceNumber-1] == '-':
				return True
	return False
	#return pieceNumber in numberList and gameBoardNumber in gameBoardList and gameBoard[gameBoardList-1][pieceNumber-1]

def isInputValidRotation(number, letter):
	rotationList = ['l', 'r', 'L', 'R']	
	gameBoardList = [1,2,3,4]
	return letter in rotationList and number in gameBoardList


if __name__ == "__main__":
	print (getMoveFromUser(gameBoardState))
	getMoveFromUser(gameBoardState)
	getMoveFromUser(gameBoardState)
	#printBoard(gameBoardState)