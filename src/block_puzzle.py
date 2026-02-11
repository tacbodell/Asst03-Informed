import random

#CLASS - Represents a single instance of a 24-puzzle problem.
class BlockPuzzle:
    # CONSTRUCTOR
    # PARAMS - STATE (optional): a pre-positioned state of the board to initialize to
    def __init__(self, state=0):
        self.board = [[-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1]]
        self.reset()
        if state:
            self.set_state(state)

    # Sets position to goal position
    def reset(self):
        number_to_write = 1
        limit = 24
        for r in range(5):
            for c in range(5):
                if (number_to_write > limit):
                    number_to_write = 0
                self.board[r][c] = number_to_write
                number_to_write += 1

    #Sets board to a certain state
    #PARAMS - s: String, a state to set the board to  
    def set_state(self, s):
        arr = list(map(int, s.split()))
        if len(arr) != 25:
            print("Invalid string! Cannot load position.")
        else:
            for row in range(5):
                for value in range(5):
                    self.board[row][value] = arr.pop(0)

    #Print the board to the standard output
    def display(self):
        for row in self.board:
            for value in row:
                # print each number in a field of width 2
                if (value != 0):
                    print(f"{value:2}", end=" ")
                else:
                    print("  ", end=" ")
            print()
        print()

    #Set the board state to a random legal state
    def scramble(self):
        random_number = random.randint(0,24)
        used_numbers = []
        for row in range(5):
            for value in range(5):
                while(random_number in used_numbers):
                    random_number = random.randint(0,24)
                self.board[row][value] = random_number
                used_numbers.append(random_number)

    #Check if board state is goal state.
    #RETURNS - True if goal state, false, if not
    def is_complete(self):
        if self.to_string() == "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 0 ":
            return True
        return False
    
    #Returns a compact string representing the current board state to be loaded into other games.
    def to_string(self):
        string = ""
        for row in range(5):
            for value in range(5):
                block_value = self.board[row][value]
                string = string + str(block_value) + " "
        return string

    #Find and return the first blank square in the position.
    def find_blank(self):
        for row in range(5):
            for value in range(5):
                if self.board[row][value] == 0:
                    return (row,value)

    #move the blank upward. if impossible, do nothing.
    def up(self):
        blank_row = self.find_blank()[0]
        blank_col = self.find_blank()[1]
        shift_row = blank_row - 1
        shift_col = blank_col
        
        if blank_row < 1:
            pass
        else:
            value = self.board[shift_row][shift_col]
            self.board[blank_row][blank_col] = value
            self.board[shift_row][shift_col] = 0

    #move the blank down. if impossible, do nothing.
    def down(self):
        blank_row = self.find_blank()[0]
        blank_col = self.find_blank()[1]
        shift_row = blank_row + 1
        shift_col = blank_col
        
        if blank_row > 3:
            pass
        else:
            value = self.board[shift_row][shift_col]
            self.board[blank_row][blank_col] = value
            self.board[shift_row][shift_col] = 0

    #move the blank left. if impossible, do nothing.     
    def left(self):
        blank_row = self.find_blank()[0]
        blank_col = self.find_blank()[1]
        shift_row = blank_row
        shift_col = blank_col - 1
        
        if blank_col < 1:
            pass
        else:
            value = self.board[shift_row][shift_col]
            self.board[blank_row][blank_col] = value
            self.board[shift_row][shift_col] = 0
            
    #move the blank right. if impossible, do nothing.
    def right(self):
        blank_row = self.find_blank()[0]
        blank_col = self.find_blank()[1]
        shift_row = blank_row
        shift_col = blank_col + 1
        
        if blank_col > 3:
            pass
        else:
            value = self.board[shift_row][shift_col]
            self.board[blank_row][blank_col] = value
            self.board[shift_row][shift_col] = 0
            

