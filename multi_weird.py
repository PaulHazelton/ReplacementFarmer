import affordance
import farm_traversal
import wait_utils

def run_to_target(target: int) -> bool:

	if affordance.is_complete(target, Items.Weird_Substance):
		return affordance.target_met(Items.Weird_Substance, target)

	clear()
	change_hat(Hats.Purple_Hat)

	_setup()

	_cycle(target)

	return affordance.target_met(Items.Weird_Substance, target)

def _setup():

	farm_traversal.for_each_row_multi(_plant_row, None)

	return

def _cycle(target: int):

	farm_traversal.for_each_row_multi(_harvest_replant_row, target)

	return

def _plant_row(args):

	for _ in range(get_world_size()):

		if (get_pos_y() % 2 == get_pos_x() % 2):
			till()
			plant(Entities.Carrot)
			use_item(Items.Fertilizer)

		move(East)

	return

def _harvest_replant_row(target):

	while not affordance.is_complete(target, Items.Weird_Substance):

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