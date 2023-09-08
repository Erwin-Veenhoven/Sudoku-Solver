import time


# Returns an empty 9x9 board
def get_empty_board():
    board = []
    row = []

    for i in range(9):
        row.append(0)
    for i in range(9):
        board.append(list.copy(row))
    
    return list.copy(board)

# Prints a board in the console
def print_board(board, empty_field = '-'):
    for row_ind in range(len(board)):
        for col_ind in range(len(board[0])):
            if col_ind == 0:
                print('|', end = '')
            if board[row_ind][col_ind] == 0:
                print(f' {empty_field} |', end = '')
            else:
                print(f' {board[row_ind][col_ind]} |', end = '')
        print('\n')

# Returns the next possible number for a cell
def get_next_possible_num(board, pos):
    possible_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Remove all numbers that are equal or lower to the current number
    for i in range(board[pos[0]][pos[1]]):
        possible_nums.remove(i + 1)

    # Check columns
    for col_ind in range(len(board[0])):
        if board[pos[0]][col_ind] in possible_nums:
            possible_nums.remove(board[pos[0]][col_ind])

    # Check rows
    for row_ind in range(len(board)):
        if board[row_ind][pos[1]] in possible_nums:
            possible_nums.remove(board[row_ind][pos[1]])

    # Check the squares
    start_pos = (pos[0] - pos[0] % 3, pos[1] - pos[1] % 3)
    for row_ind in range(3):
        for col_ind in range(3):
            if board[row_ind + start_pos[0]][col_ind + start_pos[1]] in possible_nums:                
                possible_nums.remove(board[row_ind + start_pos[0]][col_ind + start_pos[1]])

    # If there are no possible numbers return None
    if len(possible_nums) == 0:
        return None
    
    # Return the number
    return possible_nums[0]

def solve(board, show_steps = False):
    # Put all the cells that have to be solved in an array
    empty_fields = []

    for row_ind in range(len(board)):
        for col_ind in range(len(board[0])):
            if board[row_ind][col_ind] == 0:
                empty_fields.append((row_ind, col_ind))


    index = 0       # Stores current cell we are trying to solve
    unsolved = True
    
    while unsolved:
        pos = empty_fields[index]               # Get the board position of the empty cell
        num = get_next_possible_num(board, pos) # Calculate the next possible number for this cell
        
        if num == None:
            # If there was no possible number anymore decrement index back to the previous cell
            board[pos[0]][pos[1]] = 0
            index -= 1
        else:
            # If there was a possible number put it on the board and increment the index
            board[pos[0]][pos[1]] = num
            index += 1
            
        # If show_steps is on print the current board
        if show_steps:
            print_board(board)
            print('\n')
            
        # If all the empty cells have been solved finish process
        if index == len(empty_fields):
            unsolved = False
            print_board(board)
            if not show_steps:
                print('Done!')        

# Different boards
'''
board = [
    [1,0,0,0,0,0,0,0,6],
    [0,0,6,0,2,0,7,0,0],
    [7,8,9,4,5,0,1,0,3],
    [0,0,0,8,0,7,0,0,4],
    [0,0,0,0,3,0,0,0,0],
    [0,9,0,0,0,4,2,0,1],
    [3,1,2,9,7,0,0,4,0],
    [0,4,0,0,1,2,0,7,8],
    [9,0,8,0,0,0,0,0,0]
]
'''
'''
board = [
    [7,4,0,0,0,0,0,0,5],
    [0,0,0,0,1,2,9,0,0],
    [0,5,0,8,0,0,0,3,0],
    [0,8,0,0,0,0,0,0,0],
    [0,0,7,0,0,0,0,0,6],
    [0,0,0,0,0,0,0,0,0],
    [0,0,9,0,8,0,0,0,0],
    [0,0,0,1,0,0,0,6,9],
    [0,0,0,0,6,0,0,4,0]
]
'''

board = [
    [4,0,6,5,0,2,8,0,9],
    [0,0,0,0,4,0,0,3,0],
    [0,0,0,0,0,0,0,0,5],
    [6,0,0,8,0,0,1,0,0],
    [5,0,0,0,7,0,0,8,0],
    [3,0,2,9,0,4,0,6,0],
    [0,2,0,6,0,0,0,0,1],
    [0,0,0,0,5,3,9,4,0],
    [8,3,0,0,9,0,0,0,2]
]

#board = get_empty_board()

if (__name__ == "__main__"):
    print_board(board)
    print('\n')
    
    input()                                                         # Wait for user input before solving
    start_time = time.time()                                        # Start timer
    solve(board)                                                    # Solve board
    print(f'time: {round((time.time() - start_time) * 1000, 3)}ms') # print result