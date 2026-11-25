import farm_traversal
import text_util
import debug

def main(target):
	clear()

	change_hat(Hats.Pumpkin_Hat)

	can_afford = _is_affordable()

	if can_afford == False:
		return

	totalPumpkin = num_items(Items.Pumpkin)

	print(totalPumpkin, "/", target, "Pumpkin")

	farm_traversal.all_cells(_seed)
	
	while can_afford and totalPumpkin < target:

		_pumpkin_it_up()
	
		can_afford = _is_affordable()
		totalPumpkin = num_items(Items.Pumpkin)

	# print("Got pumpkins!")

def _is_affordable():
	totalCarrots = num_items(Items.Carrot)

	return totalCarrots > 100

def _pumpkin_it_up():
	dead_pumpkins = []

	farm_traversal.all_cells_stateful(_replant_dead_pumpkin, dead_pumpkins)

	while len(dead_pumpkins) > 0:

		new_dead_pumps = []
		for target in dead_pumpkins:

			farm_traversal.move_to(target)
			_wait_for_growth()
			
			if (get_entity_type() == Entities.Dead_Pumpkin):
				plant(Entities.Pumpkin)
				new_dead_pumps.append((get_pos_x(), get_pos_y()))

		dead_pumpkins = new_dead_pumps

	farm_traversal.move_to((0, 0))
	harvest()
	farm_traversal.all_cells(_replant)

def _seed():
	till()
	plant(Entities.Pumpkin)

def _replant():
	plant(Entities.Pumpkin)

def _replant_dead_pumpkin(list):
	_wait_for_growth()
	if (get_entity_type() == Entities.Dead_Pumpkin):
		plant(Entities.Pumpkin)
		list.append((get_pos_x(), get_pos_y()))

def _wait_for_growth():
	done = False
	while done == False:
		done = get_entity_type() == Entities.Dead_Pumpkin or can_harvest() == True
