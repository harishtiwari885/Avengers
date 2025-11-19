def tony(matrix):
    transposed = [list(row) for row in zip(*matrix)]
    return transposed

matrix = [[1 , 2] , [3 , 4] , [5 , 6]]
print("Original Matrix")
for row in matrix:
    print(row)

a = tony(matrix)
print("Transposed Matrix")
for row in a:
    print(row)