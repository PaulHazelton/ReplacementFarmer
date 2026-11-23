import affordance
import wait_utils

# Returns: true if target met, false otherwise
def run_to_target(target: int) -> bool:

	if not affordance.can_afford(Entities.Sunflower):
		return False

	clear()
	change_hat(Hats.Sunflower_Hat)

	_do_thing()

	return True

def _do_thing():

	_seed_field()

	_harvest_all_with_value(15)

	return

def _seed_field():

	width = get_world_size()

	for _ in range(max_drones() - 1):
		spawn_drone(_seed_row, width)
		move(North)

	_seed_row(width)
	move(North)

	return

def _seed_row(width: int):

	for _ in range(width):
		till()
		plant(Entities.Sunflower)
		move(East)

	return

def _harvest_all_with_value(value: int):

	for _ in range(max_drones() - 1):
		spawn_drone(_harvest_all_with_value_in_row, value)
		move(North)

	_harvest_all_with_value_in_row(value)
	move(North)

	return

def _harvest_all_with_value_in_row(value: int):

	width = get_world_size()

	for _ in range(width):
		if measure() == value:
			wait_utils.wait_until_harvestable()
			harvest()
		move(East)

	return
