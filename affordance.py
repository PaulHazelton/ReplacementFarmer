def can_afford(entity: Entity) -> bool:
	cost = get_cost(entity)
	area = get_world_size()
	area = area * area

	for item in cost:
		if num_items(item) < (cost[item] * area * 10):
			return False

	return True
