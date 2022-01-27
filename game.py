cell_list = list(' ' for i in range(0, 10))

win_indices = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

x_win = 0
o_win = 0

user_input = 'X'

result = False

def print_grid():

    print("---------")
    for row in range(0, 3):
        print("|", end=" ")
        for col in range(row * 3, (row * 3) + 3):
            print(cell_list[col], end=" ")
        print("|")
    print("---------")
    
print_grid()

while not result:

    coordinates = input("Enter the coordinates: ").split()

    row_coordinate = int(coordinates[0])
    col_coordinate = int(coordinates[1])
    index = (row_coordinate - 1) * 3 + (col_coordinate - 1)

    flag = True

    while flag:
        
        if not (isinstance(row_coordinate, int) or isinstance(col_coordinate, int)):
            
            print("You should enter numbers!")
            
            coordinates = input("Enter the coordinates: ").split()

            row_coordinate = int(coordinates[0])
            col_coordinate = int(coordinates[1])
            index = (row_coordinate - 1) * 3 + (col_coordinate - 1)
            
        elif row_coordinate > 3 or col_coordinate > 3:
            
            print("Coordinates should be from 1 to 3!")
            
            coordinates = input("Enter the coordinates: ").split()

            row_coordinate = int(coordinates[0])
            col_coordinate = int(coordinates[1])
            index = (row_coordinate - 1) * 3 + (col_coordinate - 1)
            
        elif cell_list[index] != ' ':
            print("This cell is occupied! Choose another one!")
            
            coordinates = input("Enter the coordinates: ").split()

            row_coordinate = int(coordinates[0])
            col_coordinate = int(coordinates[1])
            index = (row_coordinate - 1) * 3 + (col_coordinate - 1)
            
        else:
            flag = False
            
    if user_input == 'X':
        cell_list[index] = 'X'
        user_input = 'O'
        
    else:
        cell_list[index] = 'O'
        user_input = 'X'
        
    print_grid()
        
    x_count = cell_list.count("X")
    o_count = cell_list.count("O")

    for win in win_indices:
        if cell_list[win[0]] == 'X' and cell_list[win[1]] == 'X'and cell_list[win[2]] == 'X':
            x_win += 1
        elif cell_list[win[0]] == 'O' and cell_list[win[1]] == 'O'and cell_list[win[2]] == 'O':
            o_win += 1
            
    if x_win == 1 and o_win < 1:
        print("X wins")
        result = True
        
    elif o_win == 1 and x_win < 1:
        print("O wins")
        result = True
        
    elif (x_count + o_count) == 9 and (x_win + o_win < 1):
        print(" Draw")
        result = True
