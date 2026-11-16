import harvest_when_ready
import farm_traversal
import wait_utils
import text_util
import debug

def main() -> None:

	# Setup ----
	clear()
	change_hat(Hats.Purple_Hat)

	size = get_world_size()
	area = size * size
	coord_petal_dict: dict[tuple[int, int], int] = {}

	farm_traversal.all_cells_stateful(seed, coord_petal_dict)
	flowers_left = area

	# Harvest ----

	best_flowers = find_best_flowers(coord_petal_dict)

	while (flowers_left - len(best_flowers)) >= 10:

		while len(best_flowers) > 0:
			next_flower_coord = seek_harvestable_flower(best_flowers)
			harvest()
			best_flowers.remove(next_flower_coord)
			coord_petal_dict.pop(next_flower_coord)
			flowers_left -= 1
		
		best_flowers = find_best_flowers(coord_petal_dict)

		# for coord in best_flowers:
		# 	farm_traversal.move_to(coord)
		# 	harvest_when_ready.main()
		# 	coord_petal_dict.pop(coord)
		# 	flowers_left -= 1

	# for i in range(area - 10):
		# best_flower_coord = pop_max(coord_petal_dict)
		# farm_traversal.move_to(best_flower_coord)
		# harvest_when_ready.main()
		# plant(Entities.Sunflower)
		# coord_petal_dict[(get_pos_x(), get_pos_y())] = measure() # type: ignore

	# Debug
	quick_print("There are", len(coord_petal_dict), "flowers left")

	return

def seed(dict: dict[tuple[int, int], int]) -> None:
	till()
	plant(Entities.Sunflower)
	dict[(get_pos_x(), get_pos_y())] = measure() # type: ignore
	return

def harvest() -> None:
	harvest_when_ready.main()
	return

def seek_harvestable_flower(coords: list[tuple[int, int]]) -> tuple[int, int]:

	while True:
		for coord in coords:
			farm_traversal.move_to(coord)
			if (can_harvest()):
				return coord

	# wait_utils.wait_until_harvestable()	
	# return (get_pos_x(), get_pos_y())

# Mathy Helpers

# Returns: coordinates of sunflower with max petals (or first with 15 petals)
def pop_max(dict: dict[tuple[int, int], int]) -> tuple[int, int]:
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
def find_best_flowers(dict: dict[tuple[int, int], int]) -> list[tuple[int, int]]:
	max_petals = max_petals_in_field(dict)

	# Add all coords with max petals to list
	best_flowers: list[tuple[int, int]] = []

	for key in dict:
		petals = dict[key]
		if (petals == max_petals):
			best_flowers.append(key)

	return best_flowers

def max_petals_in_field(dict: dict[tuple[int, int], int]) -> int:
	max_petals = 0
	for key in dict:
		petals = dict[key]
		if petals == 15:
			return petals
		if petals > max_petals:
			max_petals = petals
	return max_petals