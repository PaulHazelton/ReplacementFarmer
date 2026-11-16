def wait_until_harvestable():
	while True:
		if can_harvest():
			break