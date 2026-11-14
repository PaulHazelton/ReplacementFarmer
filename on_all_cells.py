def main(action):
	for x in range(get_world_size()):
		process_column(action)
		move(East)

	if (get_pos_y() != 0):
		move(North)

def process_column(action):
	for y in range(get_world_size() - 1):
		action()
		move(north_or_south())
	action()

def north_or_south():
	if (get_pos_x() % 2 == 0):
		return North
	else:
		return South