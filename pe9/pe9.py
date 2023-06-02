import random


def generate_path(N, M):
    # This function generates a random path through an NxM maze, represented as a dictionary. The keys are (i, j) tuples representing
    # coordinates of each cell in the maze and the values are integers: 0 for empty, 1 for obstacle, and 2 for path. The path starts 
    # from (0,0) and ends at (N-1,M-1), and the direction (right or down) at each step is chosen randomly. Exceptions for TypeError 
    # and KeyError are handled.

    # your code here
    maze = {}
    for i in range(N):
        for j in range(M):
            maze[(i, j)] = 0  # Initialize all cells as empty
    
    row, col = 0, 0
    maze[(row, col)] = 2
    while row < N-1 or col < M-1:
        if row == N-1:
            col +=1
        elif col == M-1:
            row +=1
        else:
            step = random.choice(['down','right'])
            if step == 'down':
                 row +=1
            else:     
                 col +=1
        maze[(row, col)] = 2
    return maze


def add_obstacles(maze, min_obstacles, N, M):
    # This function randomly adds obstacles (represented as 1) to the empty cells (represented as 0) in the given maze until at least
    # min_obstacles have been added. If a KeyError occurs while trying to set an obstacle, it is caught and a message is printed.

    # your code here
    obs = 0
    while obs < min_obstacles:
        row = random.randint(0, N-1)
        col = random.randint(0, M-1)
        if maze[(row, col)] == 0:
            maze[(row, col)] = 1
            obs += 1
        else:    
            continue
        
    return maze

def set_obstacle(maze, N, M):
    # This function allows a user to manually set an obstacle in the maze. The user is prompted to input the coordinates of the cell
    # where they want to place the obstacle. If the cell is part of the path or an obstacle is already present, an error message is 
    # displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    # your code here
    while True:
        try:
            add_item = list(map(int, input("Enter the coordinate to set an obstacle (i, j):").split(",")))
            if len(add_item) != 2:
                raise ValueError
            row, col = add_item
            if maze[(row, col)] == 2:
                print('Obstacle can not be place on the path')
            elif maze[(row, col)] == 1:
                print('Obstacle already exists at this location')
            else:
                maze[(row, col)] = 1
                print(f"Obstacle place at ({row},{col})")
                return maze
        except ValueError:
            print("ValueError in set_obstacle function. Need to be coordinates")
        except KeyError:
            print("KeyError in set_obstacle function. 'Invalid coordinates. Please input coordinates within the range'")

def remove_obstacle(maze, N, M):
    # This function allows a user to manually remove an obstacle from the maze. The user is prompted to input the coordinates of the 
    # cell where they want to remove the obstacle. If the cell is part of the path or there's no obstacle at the given cell, an error 
    # message is displayed. If the coordinates are out of bounds or not integers, a KeyError or ValueError is raised, respectively.

    # your code here
    while True:
        try:
            remove_item = list(map(int, input("Enter the coordinate to remove an obstacle (i, j):").split(",")))
            if len(remove_item) != 2:
                raise ValueError
            row, col = remove_item
            if maze[(row, col)] == 2:
                print('Obstacle does not exist on the path')
            elif maze[(row, col)] == 0:
                print('Obstacle does not exist at this location')
            else:
                maze[(row, col)] = 0
                print(f"Obstacle remove at ({row},{col})")
                return maze
        except ValueError:
            print("ValueError in remove_obstacle function. Need to be coordinates")
        except KeyError:
            print("KeyError in remove_obstacle function. 'Invalid coordinates. Please input coordinates within the range'")

def print_maze(maze, N, M):
    # This function prints the current state of the maze in a grid-like format. Each cell is represented by a 3-character string: 
    # '   ' for empty cells, ' X ' for obstacles, and ' O ' for path cells. If a KeyError occurs while trying to access a cell, it is 
    # caught and a message is printed.

    # your code here
    print("+" + "---+" * M)
    for i in range(N):
        row_str = "|"
        for j in range(M):
            if maze[(i,j)] == 0:
                row_str += "   "
            elif maze[(i,j)] == 1:
                row_str += " X "
            elif maze[(i,j)] == 2:
                row_str += " O "
            row_str += "|"
        print(row_str)
        print("+" + "---+" * M)

def read_maze_blueprint(file_name):
    with open(f"./{file_name}.txt", "r") as file:
        lines = file.readlines()
        rows = len(lines)//2
        cols = len(lines[0].split("---"))-1
    return rows, cols

def generate_maze(N, M, min_obstacles):
    # Goal: Generate a maze with a clear path from the starting point to the bottom-right cell and a minimum number of obstacles using a brute-force approach.
    # Detailed Instructions:
    # 1. Call the generate_path function with the arguments N and M to generate a maze with a clear path.
    # 2. Call the add_obstacles function with the generated maze map and the argument min_obstacles to add a minimum number of obstacles randomly to the maze.
    # 3. Return the updated maze map.
    # generate a maze with a clear path from the starting point to the bottom-right cell
    maze = generate_path(N, M)

    # add the minimum number of obstacles randomly to the maze
    maze = add_obstacles(maze, min_obstacles, N, M)

    return maze

def main():
    # This function serves as the main driver of the program. It reads the maze dimensions from a file, asks the user for the minimum 
    # number of obstacles to be added, generates the path and adds the obstacles, and then enters a loop where the user can choose to 
    # set or remove obstacles, print the maze, or exit the program. Exceptions for ValueError, IOError, and NameError are handled.

    # your code here
    # prompt the user to input the values of N, M, and min_obstacles
    
    while True:
        try:
            filename = input("Enter file name:")
            N, M =  read_maze_blueprint(filename)
            break
        except IOError:
            print("IOError occurred in main function. File not found. Please enter a valid file name")
        
    max_possible_obs = N*M-(N+M-1)
    
    while True:
        try :
            min_obstacles = int(input("Enter the minimum number of obstacles (0-" + str(max_possible_obs) + "): "))
            if min_obstacles > max_possible_obs:
                raise ValueError
            break
        except ValueError:
            print("ValueError occurred in main function. Invalid number of obstacles")
    
    maze = generate_maze(N, M, min_obstacles)
            
    while True:
        print("Options:\n1. Set obstacle\n2. Remove obstacle\n3. Print Maze\n4. Exit")
        try:
            choice = int(input("Enter your option:"))
            if choice == 1:
                set_obstacle(maze, N, M)
            elif choice == 2:
                remove_obstacle(maze, N, M)
            elif choice == 3:
                print_maze(maze, N, M)
            elif choice == 4:
                break
            else:
               raise ValueError 
        except ValueError:
            print("Invalid option. Please choose a valid option.")

main()
