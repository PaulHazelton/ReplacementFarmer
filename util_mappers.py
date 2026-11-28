import multi_power
import multi_grass
import multi_wood
import multi_carrots
import multi_pumpkins
import multi_cactus
import multi_weird
import multi_gold_2
import single_bone_2

def item_to_entity(item: Item) -> Entity:

	# Omitted:
	# - Gold
	# - Weird Substance
	
	map_dict = {
		Items.Hay:Entities.Grass,
		Items.Wood:Entities.Tree,
		Items.Carrot:Entities.Carrot,
		Items.Pumpkin:Entities.Pumpkin,
		Items.Cactus:Entities.Cactus,
		Items.Power:Entities.Sunflower,
		Items.Bone:Entities.Apple
	}

	return map_dict[item]

def item_to_hat(item: Item) -> Hat:

	map_dict = {
		Items.Hay:Hats.Straw_Hat,
		Items.Wood:Hats.Tree_Hat,
		Items.Carrot:Hats.Carrot_Hat,
		Items.Pumpkin:Hats.Pumpkin_Hat,
		Items.Cactus:Hats.Cactus_Hat,
		Items.Power:Hats.Sunflower_Hat,
		Items.Gold:Hats.Gold_Hat,
		Items.Weird_Substance:Hats.Purple_Hat
	}

	return map_dict[item]

def item_to_routine(item: Item) -> Callable:

	map_dict = {
		Items.Power:multi_power.run_to_target,
		Items.Hay:multi_grass.run_to_target,
		Items.Wood:multi_wood.run_to_target,
		Items.Carrot:multi_carrots.run_to_target,
		Items.Pumpkin:multi_pumpkins.run_to_target,
		Items.Cactus:multi_cactus.run_to_target,
		Items.Weird_Substance:multi_weird.run_to_target,
		Items.Gold:multi_gold_2.run_to_target,
		Items.Bone:single_bone_2.run_to_target
	}

	return map_dict[item]
