import multi_sunflower
import multi_grass
import multi_wood
import multi_carrots
import multi_pumpkins
import multi_cactus
import multi_weird
import maze_cheeser

base = 1000000
powerTarget = base // 10 #type: ignore
hayTarget = 10 * base
woodTarget = 10 * base
carrotTarget = 10 * base
pumpkinTarget = 10 * base
cactusTarget = 10 * base
weirdSubstanceTarget = 10 * base
goldTarget = 10 * base

def main():

	while all_targets_met() == False:

		if (num_items(Items.Power) < powerTarget):
			multi_sunflower.run_to_target(powerTarget)

		if (num_items(Items.Hay) < hayTarget):
			multi_grass.run_to_target(hayTarget)

		if (num_items(Items.Wood) < woodTarget):
			multi_wood.run_to_target(woodTarget)

		if (num_items(Items.Carrot) < carrotTarget):
			multi_carrots.run_to_target(carrotTarget)

		if (num_items(Items.Pumpkin) < pumpkinTarget):
			multi_pumpkins.run_to_target(pumpkinTarget)

		if (num_items(Items.Cactus) < woodTarget):
			multi_cactus.run_to_target(cactusTarget)

		if (num_items(Items.Weird_Substance) < weirdSubstanceTarget):
			multi_weird.run_to_target(weirdSubstanceTarget)

		if (num_items(Items.Gold) < goldTarget):
			maze_cheeser.run_to_target(goldTarget)

	print("All Targets Met!")

def all_targets_met():
	x = True
	x = x and (num_items(Items.Power) >= powerTarget)
	x = x and (num_items(Items.Hay) >= hayTarget)
	x = x and (num_items(Items.Wood) >= woodTarget)
	x = x and (num_items(Items.Carrot) >= carrotTarget)
	x = x and (num_items(Items.Pumpkin) >= pumpkinTarget)
	x = x and (num_items(Items.Weird_Substance) >= weirdSubstanceTarget)
	x = x and (num_items(Items.Gold) >= goldTarget)
	return x

if __name__ == "__main__":
	main()
