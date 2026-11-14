import on_all_cells
import harvest_when_ready

def main(target):
	clear()

	change_hat(Hats.Straw_Hat)

	totalHay = num_items(Items.Hay)

	print(totalHay, "/", target, "Hay")

	while totalHay < target:
		on_all_cells.main(harvest_when_ready.main)
		totalHay = num_items(Items.Hay)

	print("Got hay!")
