import block_puzzle

# implementation of greedy best-first search for the block puzzle.
# h(x) = the number of misplaced blocks
# INPUT: representation of the board state in string format
# OUTPUT: the action sequence required to reach the goal state with minimal path cost. if unsolvable, returns -1
# LOG: output to bin after search showing process used to find the returned action sequence
def misplaced_blocks_greedy_best_first_search(state):
    search = SearchTree(state)
    print("Searching for solution using greedy best-first search algorithm...")
    print("h(x) = # of misplaced blocks...")

    while search.frontier:
        node_to_expand = search.frontier.pop(0)
        old_state = node_to_expand.state

        puzzle = block_puzzle.BlockPuzzle(old_state)
        puzzle.up()
        if puzzle.is_complete():
            solution = node_to_expand.action_sequence
            solution.append("U")
            print("Solution found!")
            return solution
        new_state = puzzle.to_string()
        if (new_state != old_state 
            and new_state not in search.visited_states):
            #Heuristic Evaluation
            heuristic = number_of_misplaced_blocks(new_state)
            if not search.frontier:
                new_node = Node(new_state, heuristic, node_to_expand, "U")
                search.frontier.append(new_node)
                search.visited_states.append(new_state)
            else:
                for i in range(len(search.frontier)):
                    if search.frontier[i].heuristic > heuristic:
                        new_node = Node(new_state, heuristic, node_to_expand, "U")
                        search.frontier.insert(i, new_node)
                        search.visited_states.append(new_state)
                        break
                    if i == len(search.frontier)-1:
                        new_node = Node(new_state, heuristic, node_to_expand, "U")
                        search.frontier.append(new_node) 

        puzzle = block_puzzle.BlockPuzzle(old_state)
        puzzle.down()
        if puzzle.is_complete():
            solution = node_to_expand.action_sequence
            solution.append("D")
            print("Solution found!")
            return solution
        new_state = puzzle.to_string()
        if (new_state != old_state 
            and new_state not in search.visited_states):
            #Heuristic Evaluation
            heuristic = number_of_misplaced_blocks(new_state)
            if not search.frontier:
                new_node = Node(new_state, heuristic, node_to_expand, "D")
                search.frontier.append(new_node)
                search.visited_states.append(new_state)
            else:
                for i in range(len(search.frontier)):
                    if search.frontier[i].heuristic > heuristic:
                        new_node = Node(new_state, heuristic, node_to_expand, "D")
                        search.frontier.insert(i, new_node)
                        search.visited_states.append(new_state)
                        break
                    if i == len(search.frontier)-1:
                        new_node = Node(new_state, heuristic, node_to_expand, "D")
                        search.frontier.append(new_node) 

        puzzle = block_puzzle.BlockPuzzle(old_state)
        puzzle.left()
        if puzzle.is_complete():
            solution = node_to_expand.action_sequence
            solution.append("L")
            print("Solution found!")
            return solution
        new_state = puzzle.to_string()
        if (new_state != old_state 
            and new_state not in search.visited_states):
            #Heuristic Evaluation
            heuristic = number_of_misplaced_blocks(new_state)
            if not search.frontier:
                new_node = Node(new_state, heuristic, node_to_expand, "L")
                search.frontier.append(new_node)
                search.visited_states.append(new_state)
            else:
                for i in range(len(search.frontier)):
                    if search.frontier[i].heuristic > heuristic:
                        new_node = Node(new_state, heuristic, node_to_expand, "L")
                        search.frontier.insert(i, new_node)
                        search.visited_states.append(new_state)
                        break
                    if i == len(search.frontier)-1:
                        new_node = Node(new_state, heuristic, node_to_expand, "L")
                        search.frontier.append(new_node) 

        puzzle = block_puzzle.BlockPuzzle(old_state)
        puzzle.right()
        if puzzle.is_complete():
            solution = node_to_expand.action_sequence
            solution.append("R")
            print("Solution found!")
            return solution
        new_state = puzzle.to_string()
        if (new_state != old_state 
            and new_state not in search.visited_states):
            #Heuristic Evaluation
            heuristic = number_of_misplaced_blocks(new_state)
            if not search.frontier:
                new_node = Node(new_state, heuristic, node_to_expand, "R")
                search.frontier.append(new_node)
                search.visited_states.append(new_state)
            else:
                for i in range(len(search.frontier)):
                    if search.frontier[i].heuristic > heuristic:
                        new_node = Node(new_state, heuristic, node_to_expand, "R")
                        search.frontier.insert(i, new_node)
                        search.visited_states.append(new_state)
                        break
                    if i == len(search.frontier)-1:
                        new_node = Node(new_state, heuristic, node_to_expand, "R")
                        search.frontier.append(new_node) 
    
    return -1

# implementation of greedy best-first search for the block puzzle.
# h(x) = the sum of distances between blocks and their goal position
# INPUT: representation of the board state in string format
# OUTPUT: the action sequence required to reach the goal state with minimal path cost. if unsolvable, returns -1
# LOG: output to bin after search showing process used to find the returned action sequence
def sum_of_displacements_greedy_best_first_search(state):
    search = SearchTree(state)
    print("Searching for solution using greedy best-first search algorithm...")
    print("h(x) = # sum of block displacements...")

    while search.frontier:
        node_to_expand = search.frontier.pop(0)
        old_state = node_to_expand.state

        puzzle = block_puzzle.BlockPuzzle(old_state)
        puzzle.up()
        if puzzle.is_complete():
            solution = node_to_expand.action_sequence
            solution.append("U")
            print("Solution found!")
            return solution
        new_state = puzzle.to_string()
        if (new_state != old_state 
            and new_state not in search.visited_states):
            #Heuristic Evaluation
            heuristic = sum_of_displacements(new_state)
            if not search.frontier:
                new_node = Node(new_state, heuristic, node_to_expand, "U")
                search.frontier.append(new_node)
                search.visited_states.append(new_state)
            else:
                for i in range(len(search.frontier)):
                    if search.frontier[i].heuristic > heuristic:
                        new_node = Node(new_state, heuristic, node_to_expand, "U")
                        search.frontier.insert(i, new_node)
                        search.visited_states.append(new_state)
                        break
                    if i == len(search.frontier)-1:
                        new_node = Node(new_state, heuristic, node_to_expand, "U")
                        search.frontier.append(new_node) 

        puzzle = block_puzzle.BlockPuzzle(old_state)
        puzzle.down()
        if puzzle.is_complete():
            solution = node_to_expand.action_sequence
            solution.append("D")
            print("Solution found!")
            return solution
        new_state = puzzle.to_string()
        if (new_state != old_state 
            and new_state not in search.visited_states):
            #Heuristic Evaluation
            heuristic = sum_of_displacements(new_state)
            if not search.frontier:
                new_node = Node(new_state, heuristic, node_to_expand, "D")
                search.frontier.append(new_node)
                search.visited_states.append(new_state)
            else:
                for i in range(len(search.frontier)):
                    if search.frontier[i].heuristic > heuristic:
                        new_node = Node(new_state, heuristic, node_to_expand, "D")
                        search.frontier.insert(i, new_node)
                        search.visited_states.append(new_state)
                        break
                    if i == len(search.frontier)-1:
                        new_node = Node(new_state, heuristic, node_to_expand, "D")
                        search.frontier.append(new_node) 

        puzzle = block_puzzle.BlockPuzzle(old_state)
        puzzle.left()
        if puzzle.is_complete():
            solution = node_to_expand.action_sequence
            solution.append("L")
            print("Solution found!")
            return solution
        new_state = puzzle.to_string()
        if (new_state != old_state 
            and new_state not in search.visited_states):
            #Heuristic Evaluation
            heuristic = sum_of_displacements(new_state)
            if not search.frontier:
                new_node = Node(new_state, heuristic, node_to_expand, "L")
                search.frontier.append(new_node)
                search.visited_states.append(new_state)
            else:
                for i in range(len(search.frontier)):
                    if search.frontier[i].heuristic > heuristic:
                        new_node = Node(new_state, heuristic, node_to_expand, "L")
                        search.frontier.insert(i, new_node)
                        search.visited_states.append(new_state)
                        break
                    if i == len(search.frontier)-1:
                        new_node = Node(new_state, heuristic, node_to_expand, "L")
                        search.frontier.append(new_node) 

        puzzle = block_puzzle.BlockPuzzle(old_state)
        puzzle.right()
        if puzzle.is_complete():
            solution = node_to_expand.action_sequence
            solution.append("R")
            print("Solution found!")
            return solution
        new_state = puzzle.to_string()
        if (new_state != old_state 
            and new_state not in search.visited_states):
            #Heuristic Evaluation
            heuristic = sum_of_displacements(new_state)
            if not search.frontier:
                new_node = Node(new_state, heuristic, node_to_expand, "R")
                search.frontier.append(new_node)
                search.visited_states.append(new_state)
            else:
                for i in range(len(search.frontier)):
                    if search.frontier[i].heuristic > heuristic:
                        new_node = Node(new_state, heuristic, node_to_expand, "R")
                        search.frontier.insert(i, new_node)
                        search.visited_states.append(new_state)
                        break
                    if i == len(search.frontier)-1:
                        new_node = Node(new_state, heuristic, node_to_expand, "R")
                        search.frontier.append(new_node) 
    
    return -1

### -----HELPER FUNCTIONS----- ###

#Gets the number of blocks that are not on their goal position
#PARAMS - state: the current state of the board as a string
#RETURN - number of misplaced blocks
def number_of_misplaced_blocks(state):
    puzzle = block_puzzle.BlockPuzzle(state)
    number_of_misplaced_blocks = 0
    number_to_check = 0
    for row in range(5):
        for value in range(5):
            number_to_check += 1
            if puzzle.board[row][value] != number_to_check:
                number_of_misplaced_blocks += 1
    return number_of_misplaced_blocks

#Gets the total sum of distance from goals of every block in the given state
#PARAMS - state: the current state of the board as a string
#RETURN - sum of distances as an integer
def sum_of_displacements(state):
    sum = 0
    puzzle = block_puzzle.BlockPuzzle(state)
    for row in range(5):
        for col in range(5):
            value = puzzle.board[row][col]
            goal_row = value // 5
            goal_col = (value % 5) - 1
            distance = (abs(row - goal_row) + abs(col - goal_col))
            sum += distance
    return sum

### -----DATA STRUCTURES------ ###

class Node:
    def __init__(self, state="", heuristic=-1, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.heuristic = heuristic
        if parent:
            self.path_cost = parent.path_cost + 1
            self.action_sequence = parent.action_sequence + [action]
        else:
            self.path_cost = 0
            self.action_sequence = []

class SearchTree:
    def __init__(self, state):
        self.root = Node(state)
        self.frontier = [self.root]
        self.visited_states = [state]



    