import harvest_when_ready

def main(target):
	clear()

	totalWood = num_items(Items.Wood)

	print(totalWood, "/", target, "Wood")

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
