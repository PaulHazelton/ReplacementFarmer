import affordance
import farm_traversal
import wait_utils

def run_to_target(target: int) -> bool:

	if _is_complete(target):
		return _target_met(target)

	clear()
	change_hat(Hats.Tree_Hat)

	_setup()

	while not _is_complete(target):
		_cycle()

	return _target_met(target)

def _target_met(target: int) -> bool:
	return num_items(Items.Power) >= target

def _is_complete(target: int) -> bool:
	return affordance.can_afford(Entities.Sunflower) == False or _target_met(target)

def _setup():

	farm_traversal.all_cells_multi(_plant)
	
	return

def _cycle():

	farm_traversal.all_cells_multi(_harvest_replant)

	return

def _plant():
	plant(Entities.Bush)
	return

def _harvest_replant():
	wait_utils.harvest_when_ready()
	plant(Entities.Bush)
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