import util_exceptions
import util_wait

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

# Row

def all_cells_in_row(action, args):
	for x in range(get_world_size()):
		action(args)
		move(East)
	return

# Target Seeking

def go_home():
	move_to((0, 0))
	return

def move_to(target: tuple[int, int]):
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

# All Cells multi-farm
def all_cells_multi(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

def for_each_row_multi(task: Callable, args) -> None:

	for _ in range(get_world_size() - 1):
		spawn_drone(task, args)
		move(North)

	task(args)
	move(North)

	return

# Checkered Multi
# def checkered_cells_multi(odd_action, even_action):

# 	for _ in range(max_drones() - 1):
# 		spawn_drone(_process_row, task)
# 		move(North)

# 	_process_row(task)
# 	move(North)
# 	wait_utils.wait_till_im_last()

# 	return

# def _process_row_checkered(odd_action, even_action):
# 	return

# Generate points evenly distributed across the field
def get_even_distributed_points(count: int) -> list[tuple[int, int]]:
	
	if (count == 8):
		return _distribute_8()
	elif (count == 16):
		return _distribute_16()
	elif (count == 25):
		return _distribute_25()
	elif (count == 32):
		if (get_world_size() == 8):
			return _distribute_32_size_8()
		else:
			return _distribute_32_big()
	else:
		message = "_even_distributed_points: count of " + str(count) + " Not implimented!"
		util_exceptions.throw(message)
		return None #type: ignore

def get_divided_box_corner_points(count: int) -> list[tuple[int, int]]:

	points: list[tuple[int, int]] = []

	width = get_world_size()
	n = max_drones()

	x0 = 0
	x1 = width // 2

	num_rows = n // 2
	box_height = width // num_rows

	for y in range(num_rows):
		points.append((x0, y * box_height))
		points.append((x1, y * box_height))

	return points

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

def _distribute_25() -> list[tuple[int, int]]:

	points: list[tuple[int, int]] = []

	size: int = get_world_size()
	s = (size - 1) // 4

	for i in range(5):
		for j in range(5):
			points.append((i * s, j * s))

	return points

def _distribute_32_size_8() -> list[tuple[int, int]]:

	points: list[tuple[int, int]] = []

	for x in range(8):
		y_offset = 0
		if (x % 2 == 1):
			y_offset = 1

		for y in range(4):
			points.append((x, y_offset + y * 2))

	return points

def _distribute_32_big() -> list[tuple[int, int]]:

	points: list[tuple[int, int]] = []

	size: int = get_world_size()
	s = (size - 1) // 7

	for x in range(8):
		if (x % 2 == 0):
			for y in range(4):
				points.append((1 + x * s, 1 + y * 2 * s))
		else:
			for y in range(4):
				points.append((1 + x * s, 1 + s + (y * 2 * s)))

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

def Test_move_to():
	clear()
	do_a_flip()

	move_to((5, 5))
	do_a_flip()
	move_to((0, 0))
	do_a_flip()
	move_to((5, 0))
	do_a_flip()
	move_to((0, 5))
	do_a_flip()

	return

def Test_distribute():
	
	def _task(point: tuple[int, int]):
		move_to(point)
		util_wait.wait_forever()
		return
	
	clear()
	set_world_size(8)

	n = max_drones()
	points = get_even_distributed_points(n)

	for i in range(n - 1):
		spawn_drone(_task, points[i])

	_task(points[n - 1])

	return
