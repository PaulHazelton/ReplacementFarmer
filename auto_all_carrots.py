import harvest_when_ready
import on_all_cells

def main(target):
	clear()

	change_hat(Hats.Carrot_Hat)

	can_afford = is_affordable()
	if can_afford:
		print("Rich boy")
	else:
		print("Poor")
		return

	totalCarrot = num_items(Items.Carrot)
	
	print(totalCarrot, "/", target, "Carrot")

	on_all_cells.main(seed)

	while can_afford:
		
		on_all_cells.main(plant_carrot)
		can_afford = is_affordable()

def plant_carrot():
	harvest_when_ready.main()
	plant(Entities.Carrot)

def is_affordable():
	totalHay = num_items(Items.Hay)
	totalWood = num_items(Items.Wood)

	return totalHay > 100 and totalWood > 100

def seed():
	till()
	plant(Entities.Carrot)
