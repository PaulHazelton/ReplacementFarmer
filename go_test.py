import util_mappers

def main():

	test_item = Items.Power
	target = num_items(test_item) * 1.1
	routine = util_mappers.item_to_routine(test_item)

	run_single(routine, target) #type: ignore

	return

def run_single(task: Callable, target: int):

	if (task(target)):
		print("Done")
	else:
		print("Can't Afford")

	return

if __name__ == "__main__":
	main()
