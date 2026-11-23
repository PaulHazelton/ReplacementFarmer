import auto_all_grass
import multi_grass

def main():

	# auto_all_grass.main(num_items(Items.Hay) * 2)
	multi_grass.run_to_target(1000000) #type: ignore

	# maze_runner.main(num_items(Items.Gold) + 256) #type: ignore
	# maze_runner_2.main(num_items(Items.Gold) + 256) #type: ignore
	print("Done!")

	return

if __name__ == "__main__":
	main()
