clear()
while True:
	for i in range(get_world_size()):
		while True:
			if can_harvest():
				harvest()
				plant(Entities.Bush)
				break
		move(North)
	move(East)