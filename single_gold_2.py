# Notes
# Evenly distribute dones across field before summoning a maze.
# Each drone uses the same algorithm from single_gold_1 to solve the maze.
# ----

import util_afford
import util_maze
import util_traversal
import util_wait

# Public functions ----

def run_to_target(target: int) -> bool:

	if (_is_complete(target)):
		return _target_met(target)

	clear()
	change_hat(Hats.Gold_Hat)

	_cycle(target)

	return _target_met(target)

# Primary Functionality ----

def _cycle(target: int):

	# set_world_size(4)

	_distribute_helpers(target)

	clear()

	return

# Helpers ----

def _distribute_helpers(target: int):

	n = max_drones()

	points = util_traversal.get_even_distributed_points(n)

	for i in range(n - 1):
		spawn_drone(_drone_task, points[i])

	_leader_task(points[n - 1], target)

	return

def _leader_task(point: tuple[int, int], target: int):
	while not _is_complete(target):
		util_traversal.move_to(point)
		do_a_flip()
		util_maze.build_maze(get_world_size())
		util_maze.solve_maze()
		harvest()
	return

def _drone_task(point: tuple[int, int]):
	while True:
		util_traversal.move_to(point)
		util_wait.wait_until_maze_exists()
		util_maze.solve_maze()
		harvest()
	return

# Maze solving helpers

# Aliases ----

def _is_complete(target: int) -> bool:
	return util_afford.is_complete(Items.Gold, target)

def _target_met(target: int) -> bool:
	return util_afford.target_met(Items.Gold, target)
