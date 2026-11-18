import harvest_when_ready
import farm_traversal

def main(target):
	
	can_afford = is_affordable()
	if can_afford == False:
		return

	clear()
	change_hat(Hats.Carrot_Hat)
	
	totalCarrot = num_items(Items.Carrot)
	
	print(totalCarrot, "/", target, "Carrot")

	farm_traversal.all_cells(seed)

	while can_afford and totalCarrot < target:
		
		farm_traversal.all_cells(plant_carrot)
		can_afford = is_affordable()
		totalCarrot = num_items(Items.Carrot)

	# if totalCarrot >= target:
	# 	print("Got carrots!")


def plant_carrot():
	if (can_harvest() == False):
		water()

	harvest_when_ready.main()
	plant(Entities.Carrot)
	return

def water():
	if (get_water() < 0.25 and num_items(Items.Water) > 1000):
		use_item(Items.Water)

def is_affordable():
	totalHay = num_items(Items.Hay)
	totalWood = num_items(Items.Wood)

	return totalHay > 100 and totalWood > 100

def seed():
	till()
	plant(Entities.Carrot)
