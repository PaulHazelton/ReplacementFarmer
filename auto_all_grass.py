import harvest_when_ready

def main(target):
	clear()

	totalHay = num_items(Items.Hay)

	print(totalHay, "/", target, "Hay")

	while totalHay < target:
		for i in range(get_world_size() - 1):
			harvest_when_ready.main()
			move(north_or_south())
		harvest_when_ready.main()
		move(East)

		totalHay = num_items(Items.Hay)

	print("Got hay!")
