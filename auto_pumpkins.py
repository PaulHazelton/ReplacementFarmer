import harvest_when_ready
import farm_traversal
import text_util
import debug

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

	while len(dead_pumpkins) > 0:

		# do_a_flip()
		# print(len(dead_pumpkins), "spots to check")

		new_dead_pumps = []
		for target in dead_pumpkins:

			farm_traversal.move_to(target)
			
			if (get_entity_type() == Entities.Dead_Pumpkin):
				# do_a_flip()
				plant(Entities.Pumpkin)
				new_dead_pumps.append((get_pos_x(), get_pos_y()))
			else:
				quick_print("At", debug.pos_string(), "dead pump is good now")

		dead_pumpkins = new_dead_pumps

	print("Done???????")
	# farm_traversal.all_cells(harvest_or_skip)


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
