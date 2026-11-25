import affordance
import exceptions
import farm_traversal
import wait_utils


def run_to_target(target: int) -> bool:

	if affordance.is_complete(target, Items.Gold):
		return affordance.target_met(Items.Gold, target)

	clear()
	change_hat(Hats.Gold_Hat)

	_setup(target)

	return affordance.target_met(Items.Gold, target)

def _setup(target: int):

	maze_size = _max_maze_size(max_drones())

	set_world_size(maze_size) #type: ignore

	num_drones = maze_size * maze_size
	_distribute_helpers(num_drones, target)

	return

def _distribute_helpers(num_drones: int, target: int):

	points = farm_traversal.get_even_distributed_points(num_drones)

	for i in range(num_drones - 1):
		spawn_drone(_drone_task, points[i])

	_leader_task((points[num_drones - 1], target))

	# print("_distribute_helpers() end")

	return

def _leader_task(args: tuple[tuple[int, int], int]):

	point, target = args

	farm_traversal.move_to(point)
	
	# Wait for other drones to get in position
	do_a_flip()

	while not affordance.is_complete(target, Items.Gold):
		_build_maze()

		while _in_a_maze():
			if _over_treasure():
				if not use_item(Items.Weird_Substance, affordance.get_required_substance_amount()):
					harvest()

	clear()
	# print("Done?")
	
	return

def _drone_task(point: tuple[int, int]):
	farm_traversal.move_to(point)
	wait_utils.wait_until_maze_exists()
	while True:
		if _over_treasure():
			if not use_item(Items.Weird_Substance, affordance.get_required_substance_amount()):
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

def _in_a_maze() -> bool:
	entity = get_entity_type()
	return (entity == Entities.Hedge or entity == Entities.Treasure)

def _over_treasure() -> bool:

	m = measure()

	# If we're not in a maze (farm was cleared recently), measure() gives None
	if (m == None):
		return False

	x, y = m #type: ignore

	return get_pos_x() == x and get_pos_y() == y

def _maze_exhausted() -> bool:

	return measure() == None

def _build_maze():
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, affordance.get_required_substance_amount())
	return