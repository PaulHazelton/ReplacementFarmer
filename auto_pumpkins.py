import harvest_when_ready
import farm_traversal
import text_util

def main(target):
	clear()

	change_hat(Hats.Purple_Hat)

	can_afford = is_affordable()

	if can_afford == False:
		return

	totalPumpkin = num_items(Items.Pumpkin)

	print(totalPumpkin, "/", target, "Pumpkin")
	
	pumpkin_it_up()

	# while can_afford and totalPumpkin < target:

	
	# can_afford = is_affordable()
	# totalPumpkin = num_items(Items.Pumpkin)

	print("Got pumpkins!")

def pumpkin_it_up():
	dead_pumpkins = []

	farm_traversal.all_cells(seed)

	farm_traversal.all_cells_stateful(replant_dead_pumpkin, dead_pumpkins)

	text_util.print_list(dead_pumpkins)

	# farm_traversal.all_cells(harvest_or_skip)

	clear()

def replant_dead_pumpkin(list):
	if (get_entity_type() == Entities.Dead_Pumpkin):
		plant(Entities.Pumpkin)
		list.append((get_pos_x(), get_pos_y()))

def harvest_or_skip():

	if can_harvest():
		harvest_when_ready.main()

def read():
	print(measure())
	#print(get_entity_type())
	#print(can_harvest())

def seed():
	till()
	plant(Entities.Pumpkin)
	# print(get_entity_type())

def is_affordable():
	totalCarrots = num_items(Items.Carrot)

	return totalCarrots > 100
