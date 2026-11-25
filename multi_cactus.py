import farm_traversal
import exceptions
import wait_utils
import affordance

def run_to_target(target: int) -> bool:

	if _is_complete(target):
		return _target_met(target)

	clear()
	change_hat(Hats.Cactus_Hat)

	_cycle(target)

	return _target_met(target)

# Primary Functionality ----

def _cycle(target: int):

	while not _is_complete(target):

		_bubble_sort_field()
		harvest()
		farm_traversal.go_home()

	return

# Helpers ----

def _bubble_sort_field():

	_plant_and_horizontal_sort()

	farm_traversal.move_to((0, 0))

	_vertical_sort()

	return

def _plant_and_horizontal_sort():

	if (get_pos_x() != 0):
		exceptions.throw("_plant_and_horizontal_sort, x != 0")

	for _ in range(get_world_size() - 1):
	
		if (num_drones() < max_drones()):
			spawn_drone(_plant_sort_row)
		else:
			_plant_sort_row()
			wait_utils.wait_till_im_last()
		move(North)

	_plant_sort_row()
	wait_utils.wait_till_im_last()
	
	return

def _vertical_sort():

	for _ in range(get_world_size() - 1):
		
		if (num_drones() < max_drones()):
			spawn_drone(_bubble_sort_col)
		else:
			_bubble_sort_col()
			wait_utils.wait_till_im_last()
		move(East)

	_bubble_sort_col()
	wait_utils.wait_till_im_last()

	return

def _plant_sort_row():
	_plant_row()
	_bubble_sort_row()
	return

def _bubble_sort_col():

	x = get_pos_x()
	unsorted_width = get_world_size()

	while (unsorted_width > 1):
		_bubble_dir(unsorted_width, North)
		farm_traversal.move_to((x, 0))
		unsorted_width -= 1

	return

def _bubble_sort_row():

	y = get_pos_y()
	unsorted_width = get_world_size()

	while (unsorted_width > 1):
		_bubble_dir(unsorted_width, East)
		farm_traversal.move_to((0, y))
		unsorted_width -= 1

	return

# Drone must be at y = 0
def _bubble_dir(row_size: int, direction):

	for _ in range(row_size - 1):

		# If should swap, swap
		if (measure() > measure(direction)): #type: ignore
			swap(direction)

		move(direction)

	return

# Drone must be at y = 0
def _plant_row():

	for _ in range(get_world_size()):
		if (get_ground_type() != Grounds.Soil):
			till()
		plant(Entities.Cactus)
		move(East)

	return

# Aliases ----

def _is_complete(target: int) -> bool:
	return affordance.is_complete(Items.Cactus, target)

def _target_met(target: int) -> bool:
	return affordance.target_met(Items.Cactus, target)
