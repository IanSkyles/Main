
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

if __name__ == "__main__":
	printBoard(gameBoardState)