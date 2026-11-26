import util_mappers
import util_targets

base = 10000000

def main():

	target_items = util_targets.get_target_items()
	all_targets_met = False

	while all_targets_met == False:

		all_targets_met = True

		for item in target_items:
			
			target = util_targets.get_target(item, base)

			if (num_items(item) < target):
				all_targets_met = False
				routine = util_mappers.item_to_routine(item)
				routine(target)

	clear()
	print("All Targets Met!")

if __name__ == "__main__":
	main()
