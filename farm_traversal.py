import exceptions

# All Cells

def all_cells(action):
	for x in range(get_world_size()):
		_process_column(action)
		move(East)

	if (get_pos_y() != 0):
		move(North)

def _process_column(action):
	for y in range(get_world_size() - 1):
		action()
		move(_north_or_south())
	action()

def all_cells_stateful(action, state):
	for x in range(get_world_size()):
		_process_column_stateful(action, state)
		move(East)

	if (get_pos_y() != 0):
		move(North)

def _process_column_stateful(action, state):
	for y in range(get_world_size() - 1):
		action(state)
		move(_north_or_south())
	action(state)

# Every Other Cell (Checkered)

def checkered_cells(odd_action, even_action):
	for x in range (get_world_size()):
		_process_column_checkered(odd_action, even_action)
		move(East)

	if (get_pos_y() != 0):
		move(North)

def _process_column_checkered(odd_action, even_action):
	for y in range(get_world_size() - 1):
	
		if (get_pos_y() % 2 == get_pos_x() % 2):
			odd_action()
		else:
			even_action()
	
		move(_north_or_south())
	
	if (get_pos_y() % 2 == get_pos_x() % 2):
		odd_action()
	else:
		even_action()

# Target Seeking

def go_home():
	move_to((0, 0))
	return

def move_to(target):
	size = get_world_size()
	x0, y0 = get_pos_x(), get_pos_y()
	x1, y1 = target
	
	xDist = _shortest_distance_to_target(x0, x1, size)
	yDist = _shortest_distance_to_target(y0, y1, size)

	xDir = East
	if (xDist < 0):
		xDir = West

	yDir = North
	if (yDist < 0):
		yDir = South

	for _ in range(abs(xDist)):
		move(xDir)

	for _ in range(abs(yDist)):
		move(yDir)

# Multi Farming

# Generate points evenly distributed across the field
def get_even_distributed_points(count: int) -> list[tuple[int, int]]:
	
	if (count == 8):
		return _distribute_8()
	elif (count == 16):
		return _distribute_16()
	else:
		exceptions.throw("_even_distributed_points: count Not implimented!")
		return None #type: ignore

def _distribute_8() -> list[tuple[int, int]]:

	points: list[tuple[int, int]] = []

	size: int = get_world_size()
	s1: int = size - 1
	s2: int = size // 3
	s3: int = s2 + s2

	points.append((0, 0))
	points.append((s1, 0))
	points.append((0, s1))
	points.append((s1, s1))

	points.append((s2, s2))
	points.append((s3, s2))
	points.append((s2, s3))
	points.append((s3, s3))

	return points

def _distribute_16() -> list[tuple[int, int]]:

	points: list[tuple[int, int]] = []

	size: int = get_world_size()
	s = (size - 1) // 3

	for i in range(4):
		for j in range(4):
			points.append((i * s, j * s))

	return points

# Input: pos: scaler value (x or y) of position
# Input: target: scaler value (x or y) of target
# Input: size: scaler value, size of world
# Returns: int. Shortest distance to target, considering world wrapping.
# Positive indicated North or East, Negative indicates South or West
def _shortest_distance_to_target(pos, target, size):
	# Straight path (positive or neg)
	dist = target - pos

	# Wrapping path (positive or neg)
	## Wrap off the right
	if target < pos:
		wrapDist = (size + target) - pos
	## Wrap off the left
	else:
		wrapDist = -(pos - (target - size))

	# Straight path is shorter
	if abs(dist) < abs(wrapDist):
		return dist
	# Wrapping path is shorter
	else:
		return wrapDist

# Shared

def _north_or_south():
	if (get_pos_x() % 2 == 0):
		return North
	else:
		return South

# Tests

def Test():
	# clear()
	# do_a_flip()

	# farm_traversal.move_to((5, 5))
	# do_a_flip()
	# farm_traversal.move_to((0, 0))
	# do_a_flip()
	# farm_traversal.move_to((5, 0))
	# do_a_flip()
	# farm_traversal.move_to((0, 5))
	# do_a_flip()

	return
