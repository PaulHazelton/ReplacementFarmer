import harvest_when_ready
import farm_traversal
import wait_utils
import text_util
import debug

def main(target_power: int) -> None:

	if (num_items(Items.Power) >= target_power):
		return

	# Constants ----
	min_sunflowers = 10

	# Setup ----
	clear()
	change_hat(Hats.Sunflower_Hat)

	size = get_world_size()
	area = size * size
	coord_petal_dict: dict[tuple[int, int], int] = {}

	farm_traversal.all_cells_stateful(_seed, coord_petal_dict)
	
	_harvest_all_but_min(coord_petal_dict, area, min_sunflowers)

	# Loop ----

	while num_items(Items.Power) < target_power:
		farm_traversal.go_home()
		farm_traversal.all_cells_stateful(_replant, coord_petal_dict)
		_harvest_all_but_min(coord_petal_dict, area, min_sunflowers)

	# Debug
	quick_print("There are", len(coord_petal_dict), "flowers left")

	return

# Main Functions

def _seed(dict: dict[tuple[int, int], int]) -> None:
	till()
	plant(Entities.Sunflower)
	dict[(get_pos_x(), get_pos_y())] = measure() # type: ignore
	return

def _harvest_all_but_min(coord_petal_dict: dict[tuple[int, int], int], area: int, min: int):
	flowers_left = area
	best_flowers = _find_best_flowers(coord_petal_dict)

	while (flowers_left - len(best_flowers)) >= min:

		while len(best_flowers) > 0:
			next_flower_coord = _seek_harvestable_flower(best_flowers)
			harvest()
			best_flowers.remove(next_flower_coord)
			coord_petal_dict.pop(next_flower_coord)
			flowers_left -= 1
		
		best_flowers = _find_best_flowers(coord_petal_dict)
	return

def _replant(dict: dict[tuple[int, int], int]) -> None:

	pos = (get_pos_x(), get_pos_y())

	if (pos in dict):
		return

	plant(Entities.Sunflower)
	dict[(get_pos_x(), get_pos_y())] = measure() # type: ignore

	return

# Farmy Helpers

def _seek_harvestable_flower(coords: list[tuple[int, int]]) -> tuple[int, int]:

	while True:
		for coord in coords:
			farm_traversal.move_to(coord)
			if (can_harvest()):
				return coord

	# wait_utils.wait_until_harvestable()	
	# return (get_pos_x(), get_pos_y())

# Mathy Helpers

# Returns: coordinates of sunflower with max petals (or first with 15 petals)
def _pop_max(dict: dict[tuple[int, int], int]) -> tuple[int, int]:
	# For now, assume dict is not sorted.
	# Also, we know 15 is the max number of petals
	best_coord, max_petal = (0, 0), 0
	for key in dict:
		petals = dict[key]
		if petals > max_petal:
			best_coord = key
			max_petal = petals
		# Early exit, we know 15 is the max
		if (petals == 15):
			best_coord = key
			max_petal = petals
			break

	dict.pop(best_coord)
	return best_coord

# Returns: a list that holds all flowers with max petals
def _find_best_flowers(dict: dict[tuple[int, int], int]) -> list[tuple[int, int]]:
	max_petals = _max_petals_in_field(dict)

	# Add all coords with max petals to list
	best_flowers: list[tuple[int, int]] = []

	for key in dict:
		petals = dict[key]
		if (petals == max_petals):
			best_flowers.append(key)

	return best_flowers

def _max_petals_in_field(dict: dict[tuple[int, int], int]) -> int:
	max_petals = 0
	for key in dict:
		petals = dict[key]
		if petals == 15:
			return petals
		if petals > max_petals:
			max_petals = petals
	return max_petals