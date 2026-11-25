import affordance

# Returns: true if target met, false otherwise
def run_to_target(target: int) -> bool:

	if _complete(target):
		return _target_met(target)

	clear()
	change_hat(Hats.Straw_Hat)

	_cycle(target)

	return _target_met(target)

def _cycle(target: int):

	n = max_drones()
	
	for _ in range(n - 1):
		spawn_drone(_harvest_row, target)
		move(North)

	_harvest_row(target)

	return

def _harvest_row(target: int):
	
	while not _complete(target):
		harvest()
		move(East)
	
	return

# Aliases
def _complete(target: int) -> bool:
	return affordance.is_complete(Items.Hay, target)

def _target_met(target: int) -> bool:
	return affordance.target_met(Items.Hay, target)
