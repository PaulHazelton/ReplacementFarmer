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

# Target
def move_to(target):
	x0, y0 = get_pos_x(), get_pos_y()
	x1, y1 = target
	xDiff = x1 - x0
	yDiff = y1 - y0

	xDir = East
	if (xDiff < 0):
		xDir = West
		xDiff = -xDiff

	yDir = North
	if (yDiff < 0):
		yDir = South
		yDiff = -yDiff

	for _ in range(xDiff):
		move(xDir)

	for _ in range(yDiff):
		move(yDir)

# Shared

def _north_or_south():
	if (get_pos_x() % 2 == 0):
		return North
	else:
		return South
