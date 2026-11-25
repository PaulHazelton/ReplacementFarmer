import affordance
import farm_traversal
import wait_utils

def run_to_target(target: int) -> bool:

	if (_is_complete(target)):
		return _target_met(target)

	clear()
	change_hat(Hats.Pumpkin_Hat)

	_setup()

	while not _is_complete(target):
		_cycle(target)

	return _target_met(target)

def _setup():

	farm_traversal.for_each_row_multi(_till_row, None)

	return

def _cycle(target: int):

	farm_traversal.for_each_row_multi(_ensure_all_grown_in_row, None)

	wait_utils.wait_till_im_last()

	harvest()

	farm_traversal.go_home()

	return

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

	farm_traversal.all_cells_in_row(_replant_dead_pumpkin, dead_pumpkins)

	while len(dead_pumpkins) > 0:
	
		new_dead_pumps = []
		for target in dead_pumpkins:

			farm_traversal.move_to(target)
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

# Standard Functions
def _target_met(target: int) -> bool:
	return num_items(Items.Pumpkin) >= target

def _is_complete(target: int) -> bool:
	return _target_met(target) or not affordance.can_afford(Entities.Pumpkin)