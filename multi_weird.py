import affordance
import farm_traversal
import wait_utils

def run_to_target(target: int) -> bool:

	if _is_complete(target):
		return _target_met(target)

	clear()
	change_hat(Hats.Traffic_Cone)

	_setup()

	_cycle(target)

	return _target_met(target)

# Primary Functionality ----

def _setup():

	farm_traversal.for_each_row_multi(_plant_row, None)

	return

def _cycle(target: int):

	farm_traversal.for_each_row_multi(_harvest_replant_row, target)

	return

# Helpers ----

def _plant_row(args):

	for _ in range(get_world_size()):

		if (get_pos_y() % 2 == get_pos_x() % 2):
			till()
			plant(Entities.Carrot)
			use_item(Items.Fertilizer)

		move(East)

	return

def _harvest_replant_row(target):

	while not _is_complete(target):

		if (get_pos_y() % 2 == get_pos_x() % 2):

			if (can_harvest()):
				harvest()
			else:
				affordance.water_if_should()
				wait_utils.harvest_when_ready()

			plant(Entities.Carrot)
			use_item(Items.Fertilizer)
	
		move(East)

	return

# Aliases ----

def _is_complete(target: int) -> bool:
	return affordance.is_complete(Items.Weird_Substance, target)

def _target_met(target: int) -> bool:
	return affordance.target_met(Items.Weird_Substance, target)
