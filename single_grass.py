import farm_traversal
import wait_utils

def main(target):
	clear()

	change_hat(Hats.Straw_Hat)

	totalHay = num_items(Items.Hay)

	print(totalHay, "/", target, "Hay")

	while totalHay < target:
		farm_traversal.all_cells(wait_utils.harvest_when_ready)
		totalHay = num_items(Items.Hay)

	# print("Got hay!")
