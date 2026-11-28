import util_mappers

def main():

	# _test_item(Items.Hay)
	# _test_item(Items.Wood)
	# _test_item(Items.Carrot)
	# _test_item(Items.Pumpkin)
	# _test_item(Items.Cactus)
	_test_item(Items.Bone)
	# _test_item(Items.Weird_Substance)
	# _test_item(Items.Gold)
	# _test_item(Items.Power)

	return

def _test_item(item: Item):

	target = num_items(item) * 1.1
	routine = util_mappers.item_to_routine(item)

	_routine_with_debug(routine, target) #type: ignore

	return

def _routine_with_debug(task: Callable, target: int):

	if (task(target)):
		print("Done")
	else:
		print("Can't Afford")

	return

if __name__ == "__main__":
	main()
