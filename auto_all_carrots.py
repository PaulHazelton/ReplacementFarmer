import harvest_when_ready

def main(target):
	clear()

	can_afford = is_affordable()
	if can_afford:
		print("Rich boy")
	else:
		print("Poor")
		return

	totalCarrot = num_items(Items.Carrot)
	
	print(totalCarrot, "/", target, "Carrot")

	till_all()

	while can_afford:
		for i in range(get_world_size()):
			harvest_when_ready.main()
			if (plant(Entities.Carrot) == False):
				print("You're broke!")
				return
			move(North)
		move(East)

		can_afford = is_affordable()

def is_affordable():
	totalHay = num_items(Items.Hay)
	totalWood = num_items(Items.Wood)

	return totalHay > 100 and totalWood > 100

def till_all():
	for x in range(get_world_size()):
		for i in range(get_world_size()):
			till()
			if (plant(Entities.Carrot) == False):
				print("You're broke!")
				return
			move(North)
		move(East)
