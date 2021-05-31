# O(m + n) space solution
def setZeroes(matrix):
	m = len(matrix)
	n = len(matrix[0])
	rows = [1]*m
	cols = [1]*n
	
	for i in range(m):
		for j in range(n):
			if matrix[i][j] == 0:
				rows[i] = 0
				cols[j] = 0
				
	for i in range(m):
		if rows[i] == 0:
			matrix[i] = [0]*n
	
	for j in range(n):
		if cols[j] == 0:
			for i in range(m):
				matrix[i][j] = 0
				
	return matrix

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
