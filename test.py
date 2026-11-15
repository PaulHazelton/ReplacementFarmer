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
	auto_pumpkins.main(2000)

	# clear()
	# till()
	# plant(Entities.Pumpkin)

	# wait_for_growth()

	# print("done!")

def wait_for_growth():
	done = False
	while done == False:
		done = get_entity_type() == Entities.Dead_Pumpkin or can_harvest() == True

if __name__ == "__main__":
	main()
