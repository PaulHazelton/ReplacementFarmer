import auto_all_grass
import auto_all_wood
import auto_all_carrots
import auto_pumpkins
import auto_sunflower
import weird_substance
import maze_runner

powerTarget = 10000
hayTarget = 128000
woodTarget = 128000
carrotTarget = 128000
pumpkinTarget = 128000
weirdSubstanceTarget = 20000
goldTarget = 128000

def main():

	while all_targets_met() == False:

		if (num_items(Items.Power) < powerTarget):
			auto_sunflower.main(powerTarget)

		if (num_items(Items.Hay) < hayTarget):
			auto_all_grass.main(hayTarget)

		if (num_items(Items.Wood) < woodTarget):
			auto_all_wood.main(woodTarget)

		if (num_items(Items.Weird_Substance) < weirdSubstanceTarget):
			weird_substance.main(weirdSubstanceTarget)

		if (num_items(Items.Gold) < goldTarget):
			maze_runner.main(goldTarget)

		if (num_items(Items.Carrot) < carrotTarget):
			auto_all_carrots.main(carrotTarget)

		if (num_items(Items.Pumpkin) < pumpkinTarget):
			auto_pumpkins.main(pumpkinTarget)

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
