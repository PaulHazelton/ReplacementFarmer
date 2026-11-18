# Constants
directions = [North, East, South, West]

# Public functions
def main(target: int):

	if (is_complete(target)):
		return

	setup()

	treasurePos: tuple[int, int] = measure() # type: ignore
	maze_map: dict[tuple[int, int], int] = {}
	maze_graph: dict[tuple[int, int], list[Direction]] = {}
	last_move_dir = None

	mark_visited(maze_map, treasurePos)
	mark_node(maze_graph, get_possible_moves())

	while True:
		if (treasurePos == pos()):
			harvest()
			break
		last_move_dir = go_next_direction(maze_map, maze_graph, treasurePos, last_move_dir)

	do_a_flip()
	
	return

# Maze solving helpers

def go_next_direction(maze_map: dict[tuple[int, int], int], maze_graph: dict[tuple[int, int], list[Direction]], treasurePos: tuple[int, int], last_move_dir: Direction | None) -> Direction:

	# There's only 4 possible directions
	# Take the first accessible one that is closer distance

	# Direction to move; distance
	possible_moves: list[Direction] = get_possible_moves()

 	# and (pos_plus(dir) in maze_map) == False
	if (len(possible_moves) > 2): # type: ignore
		mark_node(maze_graph, possible_moves)

	best_dir = best_move(possible_moves, treasurePos, last_move_dir)

	move(best_dir)
	mark_visited(maze_map, treasurePos)

	return best_dir

def get_possible_moves() -> list[Direction]:

	possible_moves: list[Direction] = []
	
	for dir in directions:
		if (can_move(dir)):
			possible_moves.append(dir) #[dir] = distance(pos_plus(dir), treasurePos)
	
	return possible_moves

def best_move(possible_moves: list[Direction], treasurePos: tuple[int, int], last_move_dir: Direction | None) -> Direction:

	num_of_possible_moves = len(possible_moves)

	if (num_of_possible_moves == 0):
		throw("best_move found no possible move!")

	if (num_of_possible_moves == 1):
		return possible_moves[0]

	# First move and >= 2 options
	if (last_move_dir == None):
		return min_dist_move(possible_moves, treasurePos)

	# Don't go where you just came from
	# Should only be 1, 2, or 3 sensable moves (2, 3, or 4 possible moves, with one removed)
	sensable_moves = possible_moves_but_not_backwards(possible_moves, last_move_dir)

	num_sensable_moves = len(sensable_moves)

	if (num_sensable_moves == 1):
		return sensable_moves[0]

	# 2 or 3 sensable moves, random for now.
	move_index: int = random() * num_sensable_moves // 1 #type: ignore
	return sensable_moves[move_index]

# Don't go where you just came from
# Returns another list of possible moves, but with one direction removed
# Must have at least 2 possible moves when calling this
def possible_moves_but_not_backwards(possible_moves: list[Direction], last_move_dir: Direction) -> list[Direction]:
	
	sensable_moves: list[Direction] = []

	came_from = opposite(last_move_dir)

	for dir in possible_moves:
		if (dir != came_from):
			sensable_moves.append(dir)

	return sensable_moves

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
		throw("min_dist_move found no possible move!")

	return best_dir #type: ignore

def mark_node(maze_graph: dict[tuple[int, int], list[Direction]], possible_moves: list[Direction]) -> None:

	quick_print("node:", pos())

	do_a_flip()
	# if (get_entity_type() != Entities.Carrot):
	# 	plant(Entities.Carrot)

	maze_graph[pos()] = possible_moves

	return

def mark_visited(maze_map: dict[tuple[int, int], int], treasurePos: tuple[int, int]):
	
	if (get_ground_type() != Grounds.Soil):
		till()
	
	maze_map[pos()] = distance(pos(), treasurePos)
	return

def pos() -> tuple[int, int]:
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

def throw(error: string):
	while True:
		print(error)
		do_a_flip()