import util_afford
import util_traversal
import util_wait
import util_maze

def run_to_target(target: int) -> bool:

	if _is_complete(target):
		return _target_met(target)

	clear()
	change_hat(Hats.Gold_Hat)

	_cycle(target)

	return _target_met(target)

# Primary Functionality ----

def _cycle(target: int):

	maze_size = _max_maze_size(max_drones())

	set_world_size(maze_size) #type: ignore

	num_drones = maze_size * maze_size
	_distribute_helpers(num_drones, target)

	return

# Helpers ----

def _distribute_helpers(num_drones: int, target: int):

	points = util_traversal.get_even_distributed_points(num_drones)

	for i in range(num_drones - 1):
		spawn_drone(_drone_task, points[i])

	_leader_task((points[num_drones - 1], target))

	# print("_distribute_helpers() end")

	return

def _leader_task(args: tuple[tuple[int, int], int]):

	point, target = args

	util_traversal.move_to(point)
	
	# Wait for other drones to get in position
	do_a_flip()

	while not _is_complete(target):
		util_maze.build_maze(get_world_size())

		while util_maze.in_a_maze():
			if util_maze.over_treasure():
				if not use_item(Items.Weird_Substance, util_maze.substance_amount(5)):
					harvest()

	clear()
	# print("Done?")
	
	return

def _drone_task(point: tuple[int, int]):
	util_traversal.move_to(point)
	util_wait.wait_until_maze_exists()
	while True:
		if util_maze.over_treasure():
			if not use_item(Items.Weird_Substance, util_maze.substance_amount(5)):
				harvest()
	return

def _max_maze_size(max_drone_count: int) -> int:

	max_size = 1

	for i in range(10):
	
		square = i * i
	
		if (square > max_drone_count):
			return max_size
		else:
			max_size = i

	return max_size

# Aliases ----

def _is_complete(target: int) -> bool:
	return util_afford.is_complete(Items.Gold, target)

def _target_met(target: int) -> bool:
	return util_afford.target_met(Items.Gold, target)
