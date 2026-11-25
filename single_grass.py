import util_traversal
import util_wait

def main(target):
	clear()

	change_hat(Hats.Straw_Hat)

	totalHay = num_items(Items.Hay)

	print(totalHay, "/", target, "Hay")

	while totalHay < target:
		util_traversal.all_cells(util_wait.harvest_when_ready)
		totalHay = num_items(Items.Hay)

	# print("Got hay!")
