import util_exceptions

# Constants ----

directions = [North, East, South, West]

# Public Functions ----

def substance_amount(maze_size: int):

	substance = maze_size * 2**(num_unlocked(Unlocks.Mazes) - 1)
	
	return substance

def build_maze(maze_size: int):
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, substance_amount(maze_size))
	return

# Move until we find treasure
def solve_maze():
	
	treasurePos: tuple[int, int] = measure() # type: ignore
	maze_graph: dict[tuple[int, int], dict[Direction, string]] = {}
	last_move_dir = None

	while not _done_solving(treasurePos):
		
		last_move_dir = _go_next_direction(maze_graph, treasurePos, last_move_dir)
	
	return

def in_a_maze() -> bool:
	entity = get_entity_type()
	return (entity == Entities.Hedge or entity == Entities.Treasure)

def over_treasure() -> bool:

	m = measure()

	# If we're not in a maze (farm was cleared recently), measure() gives None
	if (m == None):
		return False

	x, y = m #type: ignore

	return get_pos_x() == x and get_pos_y() == y

def collect_treasure(maze_size: int):
	if not use_item(Items.Weird_Substance, substance_amount(maze_size)):
		harvest()

def next_to_treasure() -> Direction | None:

	treasurePos: tuple[int, int] = measure() # type: ignore

	for dir in directions:
		if (_pos_plus(dir) == treasurePos):
			return dir

	return None

# Prefer in the order North, East, South, West, arbitrary
# We are hovering over the treasure, there may be more than 1 drone on this tile.
# Only one should harvest
# Input: dir: direction I came from
def am_i_preferred(came_from: Direction) -> bool:

	# Go around clockwise, find the first direction we can move, that's the chosen one direction
	# If came_from == chosen_one_direction, return True, False otherwise.

	for dir in directions:
		if (can_move(dir)):
			return came_from == dir

	# Should never get here
	util_exceptions.throw("am_i_preferred: found closed box in maze?")
	return False

# Helpers ----

def _go_next_direction(maze_graph: dict[tuple[int, int], dict[Direction, string]], treasurePos: tuple[int, int], last_move_dir: Direction | None) -> Direction:

	best_dir = _best_move(maze_graph, treasurePos, last_move_dir)

	move(best_dir)

	return best_dir

def _done_solving(treasurePos: tuple[int, int]) -> bool:

	return _get_pos() == treasurePos or get_entity_type() != Entities.Hedge

# Calculating Moves ----

def _best_move(maze_graph: dict[tuple[int, int], dict[Direction, string]], treasurePos: tuple[int, int], last_move_dir: Direction | None) -> Direction:

	pos = _get_pos()

	# Which moves are physically possible
	possible_moves: list[Direction] = _get_possible_moves()
	num_of_possible_moves = len(possible_moves)

	# Should never happen
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
		came_from = _opposite(last_move_dir)
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

def _get_possible_moves() -> list[Direction]:

	possible_moves: list[Direction] = []
	
	for dir in directions:
		if (can_move(dir)):
			possible_moves.append(dir) #[dir] = distance(pos_plus(dir), treasurePos)
	
	return possible_moves

# possible_moves should be at least 2
def _min_dist_move(possible_moves: list[Direction], treasurePos: tuple[int, int]) -> Direction:

	min = 1000
	best_dir: Direction | None = None

	for dir in possible_moves:
		dist = _distance(_pos_plus(dir), treasurePos)
		if (dist < min):
			min = dist
			best_dir = dir

	if (best_dir == None):
		util_exceptions.throw("min_dist_move found no possible move!")

	return best_dir #type: ignore

# Nodes ----

def _mark_new_node(maze_graph: dict[tuple[int, int], dict[Direction, string]], possible_moves: list[Direction], last_move_dir: Direction | None) -> None:

	pos = _get_pos()
	direction_labels: dict[Direction, string] = {}

	for dir in directions:
		label: string = ""
		
		if (last_move_dir != None and dir == _opposite(last_move_dir)):
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

	curr_pos = _get_pos()
	came_from = _opposite(last_move_dir) # type: ignore

	direction_labels: dict[Direction, string] = maze_graph[curr_pos]
	direction_labels[came_from] = "dead"

	maze_graph[curr_pos] = direction_labels

	return

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

# Low level helpers ----

def _opposite(dir: Direction) -> Direction:
	if (dir == North):
		return South
	if (dir == East):
		return West
	if (dir == South):
		return North
	if (dir == West):
		return East
	return North

def _distance(a: tuple[int, int], b: tuple[int, int]) -> int:

	ax, ay = a
	bx, by = b

	return abs(ax - bx) + abs(ay - by) # type: ignore

def _pos_plus(dir: Direction) -> tuple[int, int]:
	if (dir == North):
		return (get_pos_x(), get_pos_y() + 1)
	if (dir == East):
		return (get_pos_x() + 1, get_pos_y())
	if (dir == South):
		return (get_pos_x(), get_pos_y() - 1)
	if (dir == West):
		return (get_pos_x() - 1, get_pos_y())
	return (0, 0)

def _get_pos() -> tuple[int, int]:
	return (get_pos_x(), get_pos_y())
