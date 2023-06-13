def pascal_triangle(row, col):
    if col == 0 or col == row:
        return 1
    else:
        return pascal_triangle(row - 1, col - 1) + pascal_triangle(row - 1, col)

def print_direction(direction, lines):

    longest = len(lines[-1])

    if direction == "normal":
        for i in range(len(lines)):
            print(" "*((longest-len(lines[i]))//2), end="")
            print(lines[i])
    elif direction == "reversed":
        for i in range(len(lines)-1,-1,-1):
            print(" "*((longest-len(lines[i]))//2), end="")
            print(lines[i])
    elif direction == "right":
        for i in range(len(lines)):
            print(lines[i])
    else:
        for i in range(len(lines)):
            print(" "*((longest-len(lines[i]))), end="")
            print(lines[i])

def print_pascal_triangle(n, direction):
    lines = []
    for i in range(n):
        line = str('')
        for j in range(i + 1):
            line  += f"{str(pascal_triangle(i, j))} "
        lines.append(line)
    print_direction(direction, lines)

if __name__ == "__main__" :
    setup = ['normal','reversed', 'left', 'right']
    
    while True:
        try :
            num_rows = int(input("Height of Pascal's triangle: "))
            if num_rows  < 1 :
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter an interger greater than or equal to 1.")
    
    while True:
        try :
            direction = input("Direction of triangle ('normal','reversed', 'left' or 'right'): ")
            if direction  not in setup :
                raise ValueError
            break
        except ValueError:
            print("Invalid input for direction. Please enter 'normal','reversed', 'left' or 'right'.")
    print_pascal_triangle(num_rows, direction)