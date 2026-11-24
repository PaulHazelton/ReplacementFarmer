import affordance
import farm_traversal
import wait_utils

def run_to_target(target: int) -> bool:

	if _is_complete(target):
		return _target_met(target)

	clear()
	change_hat(Hats.Tree_Hat)

	_setup()

	# while not _is_complete(target):
	_cycle(target)

	return _target_met(target)

def _target_met(target: int) -> bool:
	return num_items(Items.Wood) >= target

def _is_complete(target: int) -> bool:
	return affordance.can_afford(Entities.Tree) == False or _target_met(target)

def _setup():

	farm_traversal.for_each_row_multi(_plant_row, None)
	
	return

def _cycle(target: int):

	farm_traversal.for_each_row_multi(_harvest_replant_row, target)

	return

def _plant_row(args):

	for _ in range(get_world_size()):

		if (get_pos_y() % 2 == get_pos_x() % 2):
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)

		_water_if_should()

		move(East)

	return

def _harvest_replant_row(target):

	while not _is_complete(target):

		if (can_harvest()):
			harvest()
		else:
			_water_if_should()
			wait_utils.harvest_when_ready()
	
		if (get_pos_y() % 2 == get_pos_x() % 2):
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)

		move(East)

	return

def _water_if_should():
	if (get_water() < 0.4 and num_items(Items.Water) > 10000):
		use_item(Items.Water)
	return

# def _seed_row(width: int):

# 	for _ in range(width):
# 		plant(Entities.Bush)
# 		move(East)

# 	return

# def _harvest(width: int):

# 	for _ in range(width):
# 		plant(Entities.Bush)
# 		move(East)

# 	return