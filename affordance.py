# Constants??

min_power = 10000
cost_scaler = 2

# Cost ----

# Input: target: What item are we trying to make?
# Returns: true if we can afford a cycle, false otherwise.
def can_afford(target: Item) -> bool:

	# Require minimum power level for any farm other than power farm
	if (target != Items.Power and num_items(Items.Power) < min_power):
		return False

	cost: dict[Item, int] = _get_cost_dict(target)

	area = get_world_size()
	area = area * area

	# Require affording one entity per cell in field, multiplied by cost_scaler
	for item in cost:
		if num_items(item) < (cost[item] * area * cost_scaler):
			return False

	return True

def _get_cost_dict(target: Item) -> dict[Item, int]:

	if (target == Items.Weird_Substance):
		return _weird_cost()
	elif (target == Items.Gold):
		return _gold_cost()
	else:
		return get_cost(_map_item_to_entity(target))

def _weird_cost():
	cost = get_cost(Entities.Carrot)
	cost[Items.Fertilizer] = 1
	return cost

def _gold_cost():
	return {Items.Weird_Substance:get_required_substance_amount()}

def _map_item_to_entity(item: Item) -> Entity:
	
	map_dict = {
		Items.Hay:Entities.Grass,
		Items.Wood:Entities.Tree,
		Items.Carrot:Entities.Carrot,
		Items.Pumpkin:Entities.Pumpkin,
		Items.Cactus:Entities.Cactus,
		Items.Power:Entities.Sunflower,
	}

	return map_dict[item]

# Assumes we are filling the field with a single maze
def get_required_substance_amount():

	size = get_world_size()
	substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
	
	return substance

# Target / Complete (keep?) ----

def target_met(item: Item, target: int) -> bool:
	return num_items(item) >= target

def is_complete(item: Item, target: int) -> bool:
	return target_met(item, target) or can_afford(item) == False

def water_if_should():
	if (get_water() < 0.4 and num_items(Items.Water) > 10000):
		use_item(Items.Water)
	return