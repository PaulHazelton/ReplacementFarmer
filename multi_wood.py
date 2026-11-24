import affordance
import farm_traversal

def run_to_target(target: int) -> bool:

	if _is_complete(target):
		return _target_met(target)

	clear()
	change_hat(Hats.Tree_Hat)

	while not _is_complete(target):
		_cycle()

	return _target_met(target)

def _target_met(target: int) -> bool:
	return num_items(Items.Power) >= target

def _is_complete(target: int) -> bool:
	return affordance.can_afford(Entities.Sunflower) == False or _target_met(target)

def _cycle():

	width = get_world_size()

	farm_traversal.all_cells_multi(_seed_row, width)
	farm_traversal.all_cells_multi(_seed_row, width)

	return
	
def _seed_row(width: int):

	for _ in range(width):
		plant(Entities.Bush)
		move(East)

	return