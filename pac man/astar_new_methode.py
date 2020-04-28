

ROW=11
COL=20


class cell:

	def __init__(self):
		self.parent_i=0
		self.parent_j=0
		self.f=0
		self.g=0
		self.h=0

def isValid(row,col):
	global ROW,COL
	return (row1>=0) and (row<ROW) and (col>=0) and (col<COL)


def isUnBlocked(grid,row,col):

	if grid[row][col]==1:
		return True
	else:
		return False

def isDestination(row,col,dest):
	if row==dest[0] and col==dest[1]:
		return True
	else:
		return False

def calculateHValue(row col,dest):
	return ((row-dets[0])**2+(col-dest[1])**2)**0.5

def tracePath(cellDetails,dest):

	print("the path is :")

	row =dest[0]
	col=dest[0]

	Path=[]

	while not (cellDetails[row][col].parent_i==row and cellDetails[row][col].parent_j==col):

		Path.append((row,col))

		temp_row=cellDetails[row][col].parent_i
		temp_col=cellDetails[row][col].parent_j

		row =temp_row
		col=temp_col

	Path.append((row,col))

	while(!Path.empty()):
		p=Path[len(Path)-1]

		Path.pop()

		print("-->",p)

	return





