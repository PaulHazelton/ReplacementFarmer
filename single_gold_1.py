# Notes
# 
# A node has 4 directions, each direction has one of 3 states:
# - home: When we first discover a node going East, set West to home.
# - new:  When we first discover a node, all possible exits (besides home) are marked as new.
# - dead: When we return to a node going East, set West to dead.
# 
# We simply move "forward" until we arrive at a node
# - If there's only 1 way to go, go that way (turn around from dead end)
# - If there's 2 ways to go, don't go backwards (keep track of last move direction)
#
# When leaving a node:
# - If there's any new paths, take the one that yields the minimum distance to treasure
# - If there are no new paths, go home
# 
# ----

import util_afford
import util_exceptions
import util_maze

# Constants
directions = [North, East, South, West]

# Public functions ----

def run_to_target(target: int):

	if (_is_complete(target)):
		return _target_met(target)

	clear()
	change_hat(Hats.Gold_Hat)

	_cycle(target)

	return _target_met(target)

# Primary Functionality ----

def _cycle(target: int):

	clear()

	while _is_complete(target) == False:

		util_maze.build_maze(get_world_size())
		_solve_maze()
		harvest()

		# setup()
		# use_item(Items.Weird_Substance, substance_amount())
	return

# Helpers ----

# Move until we find treasure
def _solve_maze():
	
	treasurePos: tuple[int, int] = measure() # type: ignore
	maze_graph: dict[tuple[int, int], dict[Direction, string]] = {}
	last_move_dir = None

	while treasurePos != util_maze.pos():
		
		last_move_dir = _go_next_direction(maze_graph, treasurePos, last_move_dir)
	
	return

def _go_next_direction(maze_graph: dict[tuple[int, int], dict[Direction, string]], treasurePos: tuple[int, int], last_move_dir: Direction | None) -> Direction:

	best_dir = _best_move(maze_graph, treasurePos, last_move_dir)

	move(best_dir)

	return best_dir

def _get_possible_moves() -> list[Direction]:

	possible_moves: list[Direction] = []
	
	for dir in directions:
		if (can_move(dir)):
			possible_moves.append(dir) #[dir] = distance(pos_plus(dir), treasurePos)
	
	return possible_moves

def _best_move(maze_graph: dict[tuple[int, int], dict[Direction, string]], treasurePos: tuple[int, int], last_move_dir: Direction | None) -> Direction:

	pos = util_maze.pos()

	# Which moves are physically possible
	possible_moves: list[Direction] = _get_possible_moves()
	num_of_possible_moves = len(possible_moves)

	if (num_of_possible_moves == 0):
		util_exceptions.throw("best_move found no possible move!")

	# One way to go (dead end)
	if (num_of_possible_moves == 1):
		return possible_moves[0]

	# Two ways to go, don't go backwards
	if (num_of_possible_moves == 2):
		
		# First move ever, go close to treasure
		if (last_move_dir == None):
			return _min_dist_move(possible_moves, treasurePos)

		# Don't go backwards
		came_from = util_maze.opposite(last_move_dir)
		if (possible_moves[0] == came_from):
			return possible_moves[1]
		else:
			return possible_moves[0]
		# for dir in possible_moves:
		# 	if (dir != came_from):
		# 		return dir
	# end if

	# num_of_possible_moves >= 3, this is a node ----

 	# Mark new node
	if ((pos in maze_graph) == False):
		_mark_new_node(maze_graph, possible_moves, last_move_dir)
	# Update existing node
	else:
		_update_node(maze_graph, last_move_dir)

	node = maze_graph[pos]

	return _leave_node(node, treasurePos)

def _leave_node(node: dict[Direction, string], treasurePos: tuple[int, int]) -> Direction:

	possible_moves: list[Direction] = []
	home_dir: Direction | None = None

	for dir in node:
		label = node[dir]

		if (label == "new"):
			possible_moves.append(dir)
		elif (label == "home"):
			home_dir = dir
	# end for
	num_possible_moves = len(possible_moves)

	# If no new paths, go home. If no home, exceptions.throw
	if (num_possible_moves == 0):
		if (home_dir == None):
			util_exceptions.throw("Can't leave node!")
			return North
		else:
			return home_dir

	# If there are any new paths, take best one (min distance to treasure)
	if (num_possible_moves == 1):
		return possible_moves[0]

	return _min_dist_move(possible_moves, treasurePos)

# possible_moves should be at least 2
def _min_dist_move(possible_moves: list[Direction], treasurePos: tuple[int, int]) -> Direction:

	min = 1000
	best_dir: Direction | None = None

	for dir in possible_moves:
		dist = util_maze.distance(util_maze.pos_plus(dir), treasurePos)
		if (dist < min):
			min = dist
			best_dir = dir

	if (best_dir == None):
		util_exceptions.throw("min_dist_move found no possible move!")

	return best_dir #type: ignore

def _mark_new_node(maze_graph: dict[tuple[int, int], dict[Direction, string]], possible_moves: list[Direction], last_move_dir: Direction | None) -> None:

	pos = util_maze.pos()
	direction_labels: dict[Direction, string] = {}

	for dir in directions:
		label: string = ""
		
		if (last_move_dir != None and dir == util_maze.opposite(last_move_dir)):
			label = "home"
		elif (dir in possible_moves):
			label = "new"
		else:
			label = "dead"

		direction_labels[dir] = label

	maze_graph[pos] = direction_labels

	quick_print("node:", pos, "moves:", direction_labels)

	return

def _update_node(maze_graph: dict[tuple[int, int], dict[Direction, string]], last_move_dir: Direction | None):

	if (last_move_dir == None):
		util_exceptions.throw("Updating existing node, but last_move_dir is None!")

	pos = util_maze.pos()
	came_from = opposite(last_move_dir) # type: ignore

	direction_labels: dict[Direction, string] = maze_graph[pos]
	direction_labels[came_from] = "dead"

	maze_graph[pos] = direction_labels

	return

# Aliases ----

def _is_complete(target: int) -> bool:
	return util_afford.is_complete(Items.Gold, target)

def _target_met(target: int) -> bool:
	return util_afford.target_met(Items.Gold, target)
