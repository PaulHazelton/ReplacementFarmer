import single_gold_1
import single_gold_2
import multi_gold_1
import multi_gold_2
import util_mappers
import single_grass
import util_traversal

def main():

	# test_item = Items.Cactus
	# target = num_items(test_item) * 2
	# routine = util_mappers.item_to_routine(test_item)

	# run_single(routine, target) #type: ignore

	# single_gold_1.run_to_target(num_items(Items.Gold) * 2) #type: ignore
	# single_gold_2.run_to_target(num_items(Items.Gold) * 2) #type: ignore
	# multi_gold_1.run_to_target(num_items(Items.Gold) * 2) #type: ignore
	multi_gold_2.run_to_target(num_items(Items.Gold) * 2) #type: ignore

	# util_traversal.Test_distribute()

	return

def run_single(task: Callable, target: int):

	if (task(target)):
		print("Done")
	else:
		print("Can't Afford")

	return

if __name__ == "__main__":
	main()
