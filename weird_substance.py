import farm_traversal
import harvest_when_ready

def main(target: int):

	if (is_complete(target)):
		return

	# Setup

	clear()
	change_hat(Hats.Purple_Hat)

	farm_traversal.checkered_cells(till, noop)
 
	while is_complete(target) == False:
		farm_traversal.checkered_cells(replant, noop)
		farm_traversal.checkered_cells(harvest, noop)
	
	return

def noop():
    return

def replant():
	plant(Entities.Carrot)
	use_item(Items.Fertilizer)
	return

def harvest():
    harvest_when_ready.main()
    return

def is_complete(target: int) -> bool:
    
    return is_affordable() == False or is_target_met(target)

def is_affordable() -> bool:
	
	if (num_items(Items.Hay) < 1000):
		return False
	if (num_items(Items.Wood) < 1000):
		return False
	if (num_items(Items.Fertilizer) < 1000):
		return False

	return True

def is_target_met(target: int) -> bool:
    
    return num_items(Items.Weird_Substance) >= target