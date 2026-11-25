import util_afford
import util_traversal
import util_wait

def run_to_target(target: int) -> bool:

	if _is_complete(target):
		return _target_met(target)

	clear()
	change_hat(Hats.Carrot_Hat)

	_setup()
	
	_cycle(target)

	return _target_met(target)

# Primary Functionality ----

def _setup():

	util_traversal.for_each_row_multi(_plant_row, None)

	return

def _cycle(target: int):

	util_traversal.for_each_row_multi(_harvest_replant_row, target)

	return

# Helpers ----

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
			util_wait.harvest_when_ready()
	
		plant(Entities.Carrot)

		move(East)

	return

def _water_if_should():
	if (get_water() < 0.4 and num_items(Items.Water) > 10000):
		use_item(Items.Water)
	return

# Aliases ----

def _is_complete(target: int) -> bool:
	return util_afford.is_complete(Items.Carrot, target)

def _target_met(target: int) -> bool:
	return util_afford.target_met(Items.Carrot, target)
