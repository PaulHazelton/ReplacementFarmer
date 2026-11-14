import harvest_when_ready
import farm_traversal

def main(target):
	clear()

	change_hat(Hats.Brown_Hat)

	totalWood = num_items(Items.Wood)

	print(totalWood, "/", target, "Wood")

	while totalWood < target:
		# farm_traversal.all_cells(wood_it_up)
		farm_traversal.checkered_cells(tree_it_up, bush_it_up)
		totalWood = num_items(Items.Wood)

	print("Got wood!")

def tree_it_up():
	harvest_when_ready.main()
	plant(Entities.Tree)

	water_tree()

def water_tree():
	if (get_water() < 0.5):
		use_item(Items.Water)

def bush_it_up():
	harvest_when_ready.main()
	plant(Entities.Bush)

# main(target)
# if __name__ == "__main__":
# 	main()
