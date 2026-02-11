import block_puzzle
import puzzle_search

puzzle = block_puzzle.BlockPuzzle()  # or whatever size you use

print("Welcome to Block Puzzle!")
print("Would you like to start from a random position, or load from a string?")
print("Type \"new\", or \"load\":")
while(True):
    command = input("Selection:").strip().lower()
    if command == "new":
        puzzle.scramble()
        break
    elif command == "load":
        command = input("Please paste a valid string from a previous game:")
        puzzle.set_state(command)
        break
    else:
        print("Invalid input. Please type new or load.")

print("Type: up, down, left, right, string, gbfs1, gbfs2, or quit.\n")

while True:
    puzzle.display()   # or puzzle.display()

    if puzzle.is_complete() == True:
        print("Congratulations! You solved the puzzle!")
        break

    command = input("Move: ").strip().lower()

    if command == "quit":
        print("Goodbye!")
        break
    elif command == "string":
        print(puzzle.to_string())
    elif (command == "up" or command == "u"):
        puzzle.up()
    elif (command == "down" or command == "d"):
        puzzle.down()
    elif (command == "left" or command == "l"):
        puzzle.left()
    elif (command == "right" or command == "r"):
        puzzle.right()
    elif (command == "gbfs1"):
        solution = puzzle_search.misplaced_blocks_greedy_best_first_search(puzzle.to_string())
        print(f"Solution: {solution}")
    elif (command == "gbfs2"):
        solution = puzzle_search.sum_of_displacements_greedy_best_first_search(puzzle.to_string())
        print(f"Solution: {solution}")
    else:
        print("Invalid command. Use up, down, left, right.\n")