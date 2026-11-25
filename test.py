import multi_sunflower
import multi_grass
import multi_wood
import multi_carrots
import multi_pumpkins
import multi_cactus
import multi_weird
import maze_cheeser

def main():

	# run_single(multi_carrots.run_to_target, 10000000)

	run_single(multi_grass.run_to_target, num_items(Items.Hay) + 1000) #type: ignore

	return

def run_single(task: Callable, target: int):

	if (task(target)):
		print("Done")
	else:
		print("Can't Afford")

	return

if __name__ == "__main__":
	main()
