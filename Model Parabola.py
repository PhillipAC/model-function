class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

def ToReducedRowEchelonForm( M):
    if not M: return
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while M[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        M[i],M[r] = M[r],M[i]
        lv = M[r][lead]
        M[r] = [ mrx / float(lv) for mrx in M[r]]
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
        lead += 1
		
def setup_Matrix(points):
	matrix = [[0,0,0,0] for i in range (3)]
	for j in range(3):
		for i in range(3):
			matrix[j][i] = points[j].x**(2-i)
	for i in range(3):
		matrix[i][3] = points[i].y
	return matrix
	
def read_Matrix(matrix):
	for i in range(3):
		for j in range(4):
			print(matrix[i][j], end=" ")
		print ("\n", end="")
		
def read_Resulting_Equation(matrix):
	for i in range(3):
		if(i != 0):
			if(matrix[i][3] >= 0):
				print("+", end=" ")
			else:
				print("-", end=" ")
		print (str(abs(matrix[i][3])), end="")
		if(i == 1):
			print("x", end = " ")
		elif(i != 2):
			print("x^" + str(2-i), end=" ")
			
def parabola_From_Points(point1, point2, point3, read):
	points = [point1, point2, point3]
	matrix = setup_Matrix(points)
	ToReducedRowEchelonForm( matrix )
	if (read == True):
		read_Resulting_Equation( matrix)
	return [matrix[0][3],matrix[1][3],matrix[2][3]]
	
		
point1 = Point(2,3.5)
point2 = Point(3,4)
point3 = Point(4,5)

parabola_From_Points(point1, point2, point3, True)
