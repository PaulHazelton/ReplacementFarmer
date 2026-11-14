import harvest_when_ready
import farm_traversal

def main(target):
	clear()

	change_hat(Hats.Purple_Hat)

	can_afford = is_affordable()

	totalPumpkin = num_items(Items.Pumpkin)

	print(totalPumpkin, "/", target, "Pumpkin")

	farm_traversal.all_cells(seed)

	farm_traversal.all_cells(read)

	# while can_afford and totalPumpkin < target:
	# 	farm_traversal.all_cells(pumpkin_it_up)
	# 	can_afford = is_affordable()
	# 	totalPumpkin = num_items(Items.Pumpkin)

	print("Got pumpkins!")

def read():
	print(get_entity_type())
	print(can_harvest())

def pumpkin_it_up():
	harvest_when_ready.main()
	plant(Entities.Pumpkin)

def seed():
	till()
	plant(Entities.Pumpkin)
	print(get_entity_type())

def is_affordable():
	totalCarrots = num_items(Items.Carrot)

	return totalCarrots > 100

# main(target)
# if __name__ == "__main__":
# 	main()
