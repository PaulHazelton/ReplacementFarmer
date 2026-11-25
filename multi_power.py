import util_afford
import util_wait

def run_to_target(target: int) -> bool:

	if _is_complete(target):
		return _target_met(target)

	clear()
	change_hat(Hats.Sunflower_Hat)

	_cycle(target)

	return _target_met(target)

# Primary Functionality ----

def _cycle(target: int):

	while not _is_complete(target):

		_seed_field()

		for x in [15, 14, 13, 12, 11, 10, 9, 8, 7]:
			_harvest_all_with_value(x)

	return

# Helpers ----

def _seed_field():

	width = get_world_size()

	for _ in range(width - 1):
		spawn_drone(_seed_row, width)
		move(North)

	_seed_row(width)
	move(North)

	return

def _seed_row(width: int):

	for _ in range(width):
		if (get_ground_type() != Grounds.Soil):
			till()
		if (get_water() < 0.5 and num_items(Items.Water) > 10000):
			use_item(Items.Water)
		plant(Entities.Sunflower)
		move(East)

	return

def _harvest_all_with_value(value: int):

	width = get_world_size()

	for _ in range(width - 1):
		spawn_drone(_harvest_all_with_value_in_row, value)
		move(North)

	_harvest_all_with_value_in_row(value)
	move(North)

	util_wait.wait_till_im_last()

	return

def _harvest_all_with_value_in_row(value: int):

	width = get_world_size()

	for _ in range(width):
		
		if measure() == value:
			util_wait.wait_until_harvestable()
			harvest()
		move(East)

	return

# Aliases ----

def _target_met(target: int) -> bool:
	return num_items(Items.Power) >= target

def _is_complete(target: int) -> bool:
	return util_afford.can_afford(Entities.Sunflower) == False or _target_met(target)
