# Returns: true if target met, false otherwise
def run_to_target(target: int) -> bool:

	if _complete(target):
		return True

	clear()

	change_hat(Hats.Straw_Hat)

	n = max_drones()

	for _ in range(n - 1):
		spawn_drone(_harvest_row, target)
		move(North)

	_harvest_row(target)

	return True

def _complete(target: int) -> bool:
	return num_items(Items.Hay) >= target

def _harvest_row(target: int):
	
	while not _complete(target):
		harvest()
		move(East)
	
	return