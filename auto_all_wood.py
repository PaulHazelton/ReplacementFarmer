import harvest_when_ready
import on_all_cells

def main(target):
	clear()

	change_hat(Hats.Brown_Hat)

	totalWood = num_items(Items.Wood)

	print(totalWood, "/", target, "Wood")

	while totalWood < target:
		on_all_cells.main(bush_it_up)
		totalWood = num_items(Items.Wood)

	print("Got wood!")

def bush_it_up():
	harvest_when_ready.main()
	plant(Entities.Bush)

# main(target)
# if __name__ == "__main__":
# 	main()
