import util_traversal
import util_wait

def main(target):
	clear()

	change_hat(Hats.Brown_Hat)

	totalWood = num_items(Items.Wood)

	print(totalWood, "/", target, "Wood")

	while totalWood < target:
		util_traversal.checkered_cells(tree_it_up, bush_it_up)
		totalWood = num_items(Items.Wood)

	# print("Got wood!")

def tree_it_up():
	util_wait.harvest_when_ready()
	plant(Entities.Tree)

	water_tree()

def water_tree():
	if (get_water() < 0.5):
		use_item(Items.Water)

def bush_it_up():
	util_wait.harvest_when_ready()
	plant(Entities.Bush)

# main(target)
# if __name__ == "__main__":
# 	main()
