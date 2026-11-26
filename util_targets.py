def get_target(item: Item, base: int) -> int:

	map_dict = {
		Items.Power:100000,
		Items.Hay:base,
		Items.Wood:base,
		Items.Carrot:base,
		Items.Pumpkin:base,
		Items.Cactus:base,
		Items.Weird_Substance:base,
		Items.Gold:base
	}

	return map_dict[item]

def get_target_items() -> list[Item]:
	return [
		Items.Power,
		Items.Hay,
		Items.Wood,
		Items.Carrot,
		Items.Pumpkin,
		Items.Cactus,
		Items.Weird_Substance,
		Items.Gold
	]
