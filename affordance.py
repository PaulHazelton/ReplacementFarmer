def can_afford(entity: Entity | Item) -> bool:

	cost: dict[Item, int] = {}

	if (entity == Items.Weird_Substance):
		cost = _weird_cost()
	elif (entity == Items.Gold):
		cost = _gold_cost()
	else:
		cost = get_cost(entity) #type: ignore

	area = get_world_size()
	area = area * area

	for item in cost:
		if num_items(item) < (cost[item] * area * 10):
			return False

	return True

def target_met(item: Item, target: int) -> bool:
	return num_items(item) >= target

def is_complete(target: int, item: Item, entity: Entity | Item) -> bool:
	return target_met(item, target) or can_afford(entity) == False

def _weird_cost():
	cost = get_cost(Entities.Carrot)
	cost[Items.Fertilizer] = 1
	return cost

def _gold_cost():
	return {Items.Weird_Substance:required_substance_amount()}

def required_substance_amount():

	size = get_world_size()
	substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
	return substance

def water_if_should():
	if (get_water() < 0.4 and num_items(Items.Water) > 10000):
		use_item(Items.Water)
	return