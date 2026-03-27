
matrix = [
    [1, 2, 3],   
    [4, 5, 6]   
]

print("Complete Matrix:")
print(matrix)

print("\nMatrix Elements Row by Row:")

for i in range(len(matrix)):
    
    for j in range(len(matrix[i])):
        
        print(matrix[i][j], end=" ")
    print()
    


