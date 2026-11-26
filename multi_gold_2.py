# Notes
# Spread drones out in a checkered pattern. Must have 2k^2 drones where k is an integer (32 is perfect)
# Treasure is garanteed to be under a drone, or next to a drone.
# Any drone next to treasure moves to it if it can.
# To prevent a race condition, we use `am_i_preferred`, which prioritized based on the direction the drone came from, starting at North going clockwise.
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

	set_world_size(8)

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
	
	util_traversal.move_to(point)
	do_a_flip()

	while not _is_complete(target):

		util_maze.build_maze(get_world_size())
		
		while util_maze.in_a_maze():
			if util_maze.over_treasure():
				util_maze.collect_treasure(get_world_size())
			else: 
				dir = util_maze.next_to_treasure()
				if (dir != None and can_move(dir)):
					move(dir)
					opp = util_maze._opposite(dir)
					if (util_maze.am_i_preferred(opp)):
						util_maze.collect_treasure(get_world_size())
					move(opp)

		# util_maze.solve_maze()
		# _collect_treasure()
	
	clear()

	return

def _drone_task(point: tuple[int, int]):
	
	util_traversal.move_to(point)
	util_wait.wait_until_maze_exists()
	
	while True:
		if util_maze.over_treasure():
			util_maze.collect_treasure(get_world_size())
		else: 
			dir = util_maze.next_to_treasure()
			if (dir != None and can_move(dir)):
				move(dir)
				opp = util_maze._opposite(dir)
				if (util_maze.am_i_preferred(opp)):
					util_maze.collect_treasure(get_world_size())
				move(opp)
	
	return

# Aliases ----

def _is_complete(target: int) -> bool:
	return util_afford.is_complete(Items.Gold, target)

def _target_met(target: int) -> bool:
	return util_afford.target_met(Items.Gold, target)
