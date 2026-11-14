import farm_traversal
import harvest_when_ready

def main(target):
	clear()

	change_hat(Hats.Straw_Hat)

	totalHay = num_items(Items.Hay)

	print(totalHay, "/", target, "Hay")

	while totalHay < target:
		farm_traversal.all_cells(harvest_when_ready.main)
		totalHay = num_items(Items.Hay)

	print("Got hay!")
