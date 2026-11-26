import util_mappers
import single_gold_2
import single_grass

def main():

	# test_item = Items.Pumpkin
	# target = num_items(test_item) * 2
	# routine = util_mappers.item_to_routine(test_item)

	# run_single(routine, target) #type: ignore

	# single_grass.main(20000000)
	# single_gold_1.run_to_target(num_items(Items.Gold) * 2) #type: ignore
	single_gold_2.run_to_target(num_items(Items.Gold) * 2) #type: ignore

	return

def run_single(task: Callable, target: int):

	if (task(target)):
		print("Done")
	else:
		print("Can't Afford")

	return

if __name__ == "__main__":
	main()
