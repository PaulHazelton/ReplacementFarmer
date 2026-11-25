import util_afford
import util_traversal
import util_wait

def run_to_target(target: int) -> bool:

	if (_is_complete(target)):
		return _target_met(target)

	clear()
	change_hat(Hats.Pumpkin_Hat)

	_setup()

	_cycle(target)

	return _target_met(target)

# Primary Functionality ----

def _setup():

	util_traversal.for_each_row_multi(_till_row, None)

	return

def _cycle(target: int):

	while not _is_complete(target):

		util_traversal.for_each_row_multi(_ensure_all_grown_in_row, None)

		util_wait.wait_till_im_last()

		harvest()

		util_traversal.go_home()

	return

# Helpers ----

def _till_row(args):
	for _ in range(get_world_size()):
		till()
		move(East)
	return

def _plant_row():
	for _ in range(get_world_size()):
		plant(Entities.Pumpkin)
		move(East)
	return

def _ensure_all_grown_in_row(args):

	_plant_row()

	dead_pumpkins: list[tuple[int, int]] = []

	util_traversal.all_cells_in_row(_replant_dead_pumpkin, dead_pumpkins)

	while len(dead_pumpkins) > 0:
	
		new_dead_pumps = []
		for target in dead_pumpkins:

			util_traversal.move_to(target)
			_wait_for_growth()
			
			if (get_entity_type() == Entities.Dead_Pumpkin):
				plant(Entities.Pumpkin)
				new_dead_pumps.append((get_pos_x(), get_pos_y()))

		dead_pumpkins = new_dead_pumps
	
	return

def _replant_dead_pumpkin(list):
	_wait_for_growth()
	if (get_entity_type() == Entities.Dead_Pumpkin):
		plant(Entities.Pumpkin)
		_water_if_should(0.8)
		list.append((get_pos_x(), get_pos_y()))

def _wait_for_growth():
	done = _done_growing()

	if not done:
		_water_if_should(0.4)

	while done == False:
		done = _done_growing()

def _done_growing() -> bool:
	return get_entity_type() == Entities.Dead_Pumpkin or can_harvest() == True

def _water_if_should(threshold: float):
	if (get_water() < threshold and num_items(Items.Water) > 10000):
		use_item(Items.Water)
	return

# Aliases ----

def _is_complete(target: int) -> bool:
	return util_afford.is_complete(Items.Pumpkin, target)

def _target_met(target: int) -> bool:
	return util_afford.target_met(Items.Pumpkin, target)
