# O(1) space solution
def setZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    first_row_zero = False
    first_col_zero = False
    
    for i in range(m):
        if matrix[i][0] == 0:
            first_col_zero = True
            
    for i in range(n):
        if matrix[0][i] == 0:
            first_row_zero = True
            
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
                
    for i in range(1,m):
        if matrix[i][0] == 0:
            matrix[i] = [0]*n
                
    for i in range(1,n):
        if matrix[0][i] == 0:
            for j in range(m):
                matrix[j][i] = 0
                
    if first_row_zero:
        matrix[0] = [0]*n
        
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0

    return matrix
            

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
