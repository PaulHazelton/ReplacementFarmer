import harvest_when_ready

def main(target):
	clear()

	# targetWood = str(target)
	# totalWood = str(num_items(Items.Wood))

	# print(totalWood + "/" + targetWood + " wood")

	totalWood = num_items(Items.Wood)

	print(totalWood, "/", target, "wood")

	while totalWood < target:
		for i in range(get_world_size()):
			harvest_when_ready.main()
			plant(Entities.Bush)
			move(North)
		move(East)

		totalWood = num_items(Items.Wood)

	print("Got wood!")

# main(target)
# if __name__ == "__main__":
# 	main()
