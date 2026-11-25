def wait_until_harvestable():
	while True:
		if can_harvest():
			break
	return

def wait_forever():
	while True:
		do_a_flip()
	return

def wait_until_maze_exists():
	while True:
		entity = get_entity_type()
		if (entity == Entities.Hedge or entity == Entities.Treasure):
			break
	return

def wait_till_im_last():
	while num_drones() > 1:
		# do_a_flip()
		# measure()
		continue
	return

def wait_until(predicate: Callable):
	while not predicate():
		continue
	return

def harvest_when_ready():
	while True:
		if can_harvest():
			harvest()
			break
	return