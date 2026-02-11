import block_puzzle

# implementation of BFS in the block puzzle.
# INPUT: representation of the board state in string format
# OUTPUT: the action sequence required to reach the goal state with minimal path cost. if unsolvable, returns -1
# LOG: output to bin after search showing process used to find the returned action sequence
def breadth_first_search(state):
    search = SearchTree(state)
    print("Searching for solution using breadth-first search algorithm...")

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
            search.frontier.append(Node(new_state, node_to_expand, "U"))
            search.visited_states.append(new_state)  

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
            search.frontier.append(Node(new_state, node_to_expand, "D"))
            search.visited_states.append(new_state)  

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
            search.frontier.append(Node(new_state, node_to_expand, "L"))
            search.visited_states.append(new_state)  

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
            search.frontier.append(Node(new_state, node_to_expand, "R"))
            search.visited_states.append(new_state)  
    
    return -1

#implementation of DFS in the block puzzle.
# INPUT: representation of the board state in string format
# OUTPUT: the action sequence required to reach the goal state found from DFS. if unsolvable, returns -1
# LOG: output to bin after search showing process used to find the returned action sequence
def depth_first_search(state, limit):
    search = SearchTree(state)
    print("Searching for solution using depth-first search algorithm...")

    while search.frontier:
        node_to_expand = search.frontier.pop( len(search.frontier) - 1 )
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
            and node_to_expand.path_cost < limit):
            search.frontier.append(Node(new_state, node_to_expand, "U"))
            search.visited_states.append(new_state)  

        puzzle = block_puzzle.BlockPuzzle(old_state)
        puzzle.down()
        if puzzle.is_complete():
            solution = node_to_expand.action_sequence
            solution.append("D")
            print("Solution found!")
            return solution
        new_state = puzzle.to_string()
        if (new_state != old_state 
            and node_to_expand.path_cost < limit):
            search.frontier.append(Node(new_state, node_to_expand, "D"))
            search.visited_states.append(new_state)  

        puzzle = block_puzzle.BlockPuzzle(old_state)
        puzzle.left()
        if puzzle.is_complete():
            solution = node_to_expand.action_sequence
            solution.append("L")
            print("Solution found!")
            return solution
        new_state = puzzle.to_string()
        if (new_state != old_state 
            and node_to_expand.path_cost < limit):
            search.frontier.append(Node(new_state, node_to_expand, "L"))
            search.visited_states.append(new_state)  

        puzzle = block_puzzle.BlockPuzzle(old_state)
        puzzle.right()
        if puzzle.is_complete():
            solution = node_to_expand.action_sequence
            solution.append("R")
            print("Solution found!")
            return solution
        new_state = puzzle.to_string()
        if (new_state != old_state 
            and node_to_expand.path_cost < limit):
            search.frontier.append(Node(new_state, node_to_expand, "R"))
            search.visited_states.append(new_state)  
    
    return -1

### -----DATA STRUCTURES----- ###

class Node:
    def __init__(self, state="", parent=None, action=None):
        self.state = state
        self.parent = parent
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



    