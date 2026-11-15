import auto_all_grass
import auto_all_wood
import auto_all_carrots
import auto_pumpkins
import farm_traversal
import harvest_when_ready
import text_util

def main():

	# clear()
	#auto_all_grass.main(10000)
	#auto_all_wood.main(10000)
	#auto_all_carrots.main(1000)
	# auto_pumpkins.main(2000)

	#farm_traversal.checkered_cells(till)

	# my_list = []
	# my_list.append((1, 2))
	# my_list.append((1, 3))
	# my_list.append((1, 4))
	# text_util.print_list(my_list)

	clear()
	
	farm_traversal.move_to((3, 3))
	do_a_flip()
	farm_traversal.move_to((2, 2))
	do_a_flip()
	farm_traversal.move_to((5, 0))
	do_a_flip()
	farm_traversal.move_to((0, 5))
	do_a_flip()

	# print(abs(-8))

if __name__ == "__main__":
	main()
