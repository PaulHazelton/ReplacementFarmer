def wait_until_harvestable():
	while True:
		if can_harvest():
			break

def wait_forever():
	while True:
		do_a_flip()

def wait_until_maze_exists():
	while True:
		if (get_entity_type() == Entities.Hedge):
			break