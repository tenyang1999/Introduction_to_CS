size = int(input("Enter the size of grid :"))
grid = [["_"]*size for i in range(size)]
edit = True
for i in range(size):
    for j in range(size):
        print(grid[i][j],end=' ')
    print()

while edit:
    cell = input("Enter the cell coordinates to edit :")
    if cell == "done":
        edit = False
        break
    else:
        cell  = [i for i in map(int, cell.split(","))]
        
    value = input("Enter the new value of the cell:")
    grid[cell[0]][cell[1]] =value
    
    for i in range(size):
        for j in range(size):
            print(grid[i][j],end=' ')
        print() 