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

import exceptions

# Constants
directions = [North, East, South, West]

# Public functions
def main(target: int):

	if (is_complete(target)):
		return

	change_hat(Hats.Gold_Hat)

	while is_complete(target) == False:


		setup()
		solve_maze()
		harvest()

		# setup()
		# use_item(Items.Weird_Substance, substance_amount())

	do_a_flip()
	
	return

# Maze solving helpers
# Move until we find treasure
def solve_maze():
	
	treasurePos: tuple[int, int] = measure() # type: ignore
	maze_graph: dict[tuple[int, int], dict[Direction, string]] = {}
	last_move_dir = None

	mark_visited()

	while treasurePos != get_current_pos():
		
		last_move_dir = go_next_direction(maze_graph, treasurePos, last_move_dir)
	
	return

def go_next_direction(maze_graph: dict[tuple[int, int], dict[Direction, string]], treasurePos: tuple[int, int], last_move_dir: Direction | None) -> Direction:

	best_dir = best_move(maze_graph, treasurePos, last_move_dir)

	move(best_dir)
	mark_visited()

	return best_dir

def get_possible_moves() -> list[Direction]:

	possible_moves: list[Direction] = []
	
	for dir in directions:
		if (can_move(dir)):
			possible_moves.append(dir) #[dir] = distance(pos_plus(dir), treasurePos)
	
	return possible_moves

def best_move(maze_graph: dict[tuple[int, int], dict[Direction, string]], treasurePos: tuple[int, int], last_move_dir: Direction | None) -> Direction:

	pos = get_current_pos()

	# Which moves are physically possible
	possible_moves: list[Direction] = get_possible_moves()
	num_of_possible_moves = len(possible_moves)

	if (num_of_possible_moves == 0):
		exceptions.throw("best_move found no possible move!")

	# One way to go (dead end)
	if (num_of_possible_moves == 1):
		return possible_moves[0]

	# Two ways to go, don't go backwards
	if (num_of_possible_moves == 2):
		
		# First move ever, go close to treasure
		if (last_move_dir == None):
			return min_dist_move(possible_moves, treasurePos)

		# Don't go backwards
		came_from = opposite(last_move_dir)
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
		mark_new_node(maze_graph, possible_moves, last_move_dir)
	# Update existing node
	else:
		update_node(maze_graph, last_move_dir)

	node = maze_graph[pos]

	return leave_node(node, treasurePos)

def leave_node(node: dict[Direction, string], treasurePos: tuple[int, int]) -> Direction:

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
			exceptions.throw("Can't leave node!")
			return North
		else:
			return home_dir

	# If there are any new paths, take best one (min distance to treasure)
	if (num_possible_moves == 1):
		return possible_moves[0]

	return min_dist_move(possible_moves, treasurePos)

# possible_moves should be at least 2
def min_dist_move(possible_moves: list[Direction], treasurePos: tuple[int, int]) -> Direction:

	min = 1000
	best_dir: Direction | None = None

	for dir in possible_moves:
		dist = distance(pos_plus(dir), treasurePos)
		if (dist < min):
			min = dist
			best_dir = dir

	if (best_dir == None):
		exceptions.throw("min_dist_move found no possible move!")

	return best_dir #type: ignore

def mark_new_node(maze_graph: dict[tuple[int, int], dict[Direction, string]], possible_moves: list[Direction], last_move_dir: Direction | None) -> None:

	pos = get_current_pos()
	direction_labels: dict[Direction, string] = {}

	for dir in directions:
		label: string = ""
		
		if (last_move_dir != None and dir == opposite(last_move_dir)):
			label = "home"
		elif (dir in possible_moves):
			label = "new"
		else:
			label = "dead"

		direction_labels[dir] = label

	maze_graph[pos] = direction_labels

	quick_print("node:", pos, "moves:", direction_labels)

	return

def update_node(maze_graph: dict[tuple[int, int], dict[Direction, string]], last_move_dir: Direction | None):

	if (last_move_dir == None):
		exceptions.throw("Updating existing node, but last_move_dir is None!")

	pos = get_current_pos()
	came_from = opposite(last_move_dir) # type: ignore

	direction_labels: dict[Direction, string] = maze_graph[pos]
	direction_labels[came_from] = "dead"

	maze_graph[pos] = direction_labels

	return

def mark_visited():
	
	# if (get_ground_type() != Grounds.Soil):
	# 	till()
	
	return

def get_current_pos() -> tuple[int, int]:
	return (get_pos_x(), get_pos_y())

def pos_plus(dir: Direction) -> tuple[int, int]:
	if (dir == North):
		return (get_pos_x(), get_pos_y() + 1)
	if (dir == East):
		return (get_pos_x() + 1, get_pos_y())
	if (dir == South):
		return (get_pos_x(), get_pos_y() - 1)
	if (dir == West):
		return (get_pos_x() - 1, get_pos_y())
	return (0, 0)

def distance(a: tuple[int, int], b: tuple[int, int]) -> int:

	ax, ay = a
	bx, by = b

	return abs(ax - bx) + abs(ay - by) # type: ignore

# Private Helpers
def setup():

	clear()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, substance_amount())

	return

def is_complete(target: int) -> bool:
	
	return is_affordable() == False or is_target_met(target)

def is_affordable() -> bool:

	if (num_items(Items.Weird_Substance) < substance_amount()):
		return False

	return True

def is_target_met(target: int) -> bool:
	
	return num_items(Items.Gold) >= target

def substance_amount():

	size = get_world_size()
	substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
	return substance

def opposite(dir: Direction) -> Direction:
	if (dir == North):
		return South
	if (dir == East):
		return West
	if (dir == South):
		return North
	if (dir == West):
		return East
	return North