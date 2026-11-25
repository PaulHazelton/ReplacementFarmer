import util_afford

def run_to_target(target: int) -> bool:

	if _is_complete(target):
		return _target_met(target)

	clear()
	change_hat(Hats.Straw_Hat)

	_cycle(target)

	return _target_met(target)

# Primary Functionality ----

def _cycle(target: int):

	n = max_drones()
	
	for _ in range(n - 1):
		spawn_drone(_harvest_row, target)
		move(North)

	_harvest_row(target)

	return

# Helpers ----

def _harvest_row(target: int):
	
	while not _is_complete(target):
		harvest()
		move(East)
	
	return

# Aliases ----

def _is_complete(target: int) -> bool:
	return util_afford.is_complete(Items.Hay, target)

def _target_met(target: int) -> bool:
	return util_afford.target_met(Items.Hay, target)
