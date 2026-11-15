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

def _north_or_south():
	if (get_pos_x() % 2 == 0):
		return North
	else:
		return South

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
