import auto_all_grass
import auto_all_wood
import auto_all_carrots
import auto_pumpkins
import farm_traversal
import harvest_when_ready
import text_util

def main():

	clear()
	do_a_flip()

	farm_traversal.move_to((5, 5))
	do_a_flip()
	farm_traversal.move_to((0, 0))
	do_a_flip()
	farm_traversal.move_to((5, 0))
	do_a_flip()
	farm_traversal.move_to((0, 5))
	do_a_flip()

	return

if __name__ == "__main__":
	main()
