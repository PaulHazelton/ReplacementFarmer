def substance_amount(maze_size: int):

	substance = maze_size * 2**(num_unlocked(Unlocks.Mazes) - 1)
	
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

def distance(a: tuple[int, int], b: tuple[int, int]) -> int:

	ax, ay = a
	bx, by = b

	return abs(ax - bx) + abs(ay - by) # type: ignore

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

def build_maze(maze_size: int):
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, substance_amount(maze_size))
	return

def pos() -> tuple[int, int]:
	return (get_pos_x(), get_pos_y())
