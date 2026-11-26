import util_mappers
import util_targets

million = 1000000
billion = 1000000000

def main():

	base = 10 * million
	clear()

	while base <= billion:

		print("Base Target:", base)

		_attain_all_targets(base)

		do_a_flip()
		pet_the_piggy()

		base = base * 2

	_attain_all_targets(billion)

	return

def _attain_all_targets(base: int):

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
	
	return

if __name__ == "__main__":
	main()
