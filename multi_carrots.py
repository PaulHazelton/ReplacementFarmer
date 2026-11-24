import affordance
import farm_traversal
import wait_utils

def run_to_target(target: int) -> bool:

	if _is_complete(target):
		return _target_met(target)

	clear()
	change_hat(Hats.Carrot_Hat)

	_setup()
	
	# while not _is_complete(target):
	_cycle(target)

	return _target_met(target)

def _setup():

	farm_traversal.for_each_row_multi(_plant_row, None)

	return

def _cycle(target: int):

	farm_traversal.for_each_row_multi(_harvest_replant_row, target)

	return

def _target_met(target: int):
	return num_items(Items.Carrot) >= target

def _is_complete(target: int):
	return _target_met(target) or affordance.can_afford(Entities.Carrot) == False

def _plant_row(args):
	for _ in range(get_world_size()):

		till()
		plant(Entities.Carrot)

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
	
		plant(Entities.Carrot)

		move(East)

	return

def _water_if_should():
	if (get_water() < 0.4 and num_items(Items.Water) > 10000):
		use_item(Items.Water)
	return