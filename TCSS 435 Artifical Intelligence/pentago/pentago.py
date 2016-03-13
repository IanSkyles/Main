from random import randint

#initialGameBoard will be 2d array with 4 arrays of 9
gameBoardState = [['-','-','-','-','-','-','-','-','-'],
				['-','-','-','-','-','-','-','-','-'],
				['-','-','-','-','-','-','-','-','-'],
				['-','-','-','-','-','-','-','-','-']]
testBoard = [['1','2','3','4','5','6','7','8','9'],
			['1','2','3','4','5','6','7','8','9'],
			['1','2','3','4','5','6','7','8','9'],
			['1','2','3','4','5','6','7','8','9']]
testBoardWin_Column_And_Row = 
			[['w','w','w','4','5','6','7','8','9'],
			['w','w','3','4','5','b','7','8','b'],
			['1','2','3','4','5','6','7','8','9'],
			['1','2','b','4','5','b','7','8','b']]

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
			move = raw_input("eg 3/8 1R or 2/4 3L\n")
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

#intended use: 
#1 = w, 1 = user goes first
#2 = b, 2 = user goes second
def decideTokenColorOrPlayerOrder():
	return randint(0,1)

def rotateGame(gameBoardState, blockNumber, rotationDirection):
	blockNumber = blockNumber - 1
	if rotationDirection == "L" or rotationDirection == "l":
		gameBoardState[blockNumber] = rotateLeft(gameBoardState[blockNumber])
	else:
		gameBoardState[blockNumber] = rotateRight(gameBoardState[blockNumber])
	return gameBoardState


def rotateRight(gameBoardSubBoardTarget):
	return [gameBoardSubBoardTarget[6],
			gameBoardSubBoardTarget[3],
			gameBoardSubBoardTarget[0],
			gameBoardSubBoardTarget[7],
			gameBoardSubBoardTarget[4],
			gameBoardSubBoardTarget[1],
			gameBoardSubBoardTarget[8],
			gameBoardSubBoardTarget[5],
			gameBoardSubBoardTarget[2]]

def rotateLeft(gameBoardSubBoardTarget):
	return [gameBoardSubBoardTarget[2],
			gameBoardSubBoardTarget[5],
			gameBoardSubBoardTarget[8],
			gameBoardSubBoardTarget[1],
			gameBoardSubBoardTarget[4],
			gameBoardSubBoardTarget[7],
			gameBoardSubBoardTarget[0],
			gameBoardSubBoardTarget[3],
			gameBoardSubBoardTarget[6]]

#returns the color of the winner (b or w) or n if neither win
def checkWinningStateRows(gameBoardState):
	for r in range (0,3):
		#block 1 and 2
		if gameBoardState[0][3 * r + 0] == gameBoardState[0][3 * r + 1] == gameBoardState[0][3 * r + 2] == gameBoardState[1][3 * r + 0] == gameBoardState[1][3 * r + 0]:
			return gameBoardState[0][0]
		if gameBoardState[0][3 * r + 1] == gameBoardState[0][3 * r + 2] == gameBoardState[1][3 * r + 0] == gameBoardState[1][3 * r + 1] == gameBoardState[1][3 * r + 2]:
			return gameBoardState[0][2]
		#block 3 and 4
		if gameBoardState[2][3 * r + 0] == gameBoardState[2][3 * r + 1] == gameBoardState[2][3 * r + 2] == gameBoardState[3][3 * r + 0] == gameBoardState[3][3 * r + 0]:
			return gameBoardState[2][3 * r + 0]
		if gameBoardState[2][3 * r + 1] == gameBoardState[2][3 * r + 2] == gameBoardState[3][3 * r + 0] == gameBoardState[3][3 * r + 1] == gameBoardState[3][3 * r + 2]:
			return gameBoardState[2][3 * r + 1]
	return 'n'

def checkWinningStateCols(gameBoardState):
	#s stands for squareSets
	for s in range (0,2):
		for r in range (0,3):
			if gameBoardState[0+s][0+r] == gameBoardState[0+s][3+r] == gameBoardState[0+s][6+r] == gameBoardState[2+s][0+r] == gameBoardState[2+s][3+r]:
				return gameBoardState[0][0+r]
			if gameBoardState[0+s][3+r] == gameBoardState[0+s][6+r] == gameBoardState[2+s][0+r] == gameBoardState[2+s][3+r] == gameBoardState[2+s][6+r]:
				return gameBoardState[0][2+r]
	return 'n'

if __name__ == "__main__":
	printBoard(rotateGame(testBoard, 4, 'L'))
	printBoard(rotateGame(testBoard, 1, 'R'))
	print (checkWinningStateCols(testBoardWin))
	print (checkWinningStateRows(testBoardWin))
	#print (getMoveFromUser(gameBoardState))
	#printBoard(gameBoardState)