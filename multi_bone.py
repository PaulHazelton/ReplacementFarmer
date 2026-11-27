# Notes:
#
# We split the farm into 2 columns, and max_drones // 2 rows.
# Each drone has a rectangle assigned, width is world_size / 2, height is 2.
# 
# ----

import util_afford
import util_traversal
import util_wait

def run_to_target(target: int) -> bool:

	if (_is_complete(target)):
		return _target_met(target)

	_run(target)

	return _target_met(target)

# Primary Functionality ----

def _run(target: int):

	clear()

	n = 32
	points = util_traversal.get_divided_box_corner_points(n)

	for i in range(n - 1):
		point = points[i]
		spawn_drone(_drone_task, point, target)
		
	_leader_task(points[n - 1], target)

	return

def _setup():

	clear()

	# Till everything

	util_traversal.all_cells_multi(till)

	return

def _takedown():
	clear()
	util_traversal.go_home()
	return

def _cycle(point: tuple[int, int]):

	

	# change_hat(Hats.Dinosaur_Hat)

	# util_traversal.all_cells(_noop)

	# change_hat(Hats.Straw_Hat)

	# util_traversal.go_home()

	return

# Tasks ----

def _leader_task(point: tuple[int, int], target: int):

	util_traversal.move_to(point)

	_process_rectangle(till)

	change_hat(Hats.Dinosaur_Hat)

	_process_rectangle(_noop)
	_process_rectangle(_noop)
	_process_rectangle(_noop)
	_process_rectangle(_noop)

	util_wait.wait_forever()

	return

def _drone_task(point: tuple[int, int], target: int):

	util_traversal.move_to(point)

	_process_rectangle(till)

	_process_rectangle(_noop)
	_process_rectangle(_noop)
	_process_rectangle(_noop)
	_process_rectangle(_noop)

	util_wait.wait_forever()

	return

# Helpers ----

def _process_rectangle(action: Callable):

	width = get_world_size() // 2

	for _ in range(width - 1):
		action()
		move(East)

	action()
	move(North)

	for _ in range(width - 1):
		action()
		move(West)

	action()
	move(South)

	return

def _noop():
	return

# Aliases ----

def _is_complete(target: int) -> bool:
	return util_afford.is_complete(Items.Bone, target)

def _target_met(target: int) -> bool:
	return util_afford.target_met(Items.Bone, target)
