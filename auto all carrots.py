clear()
for x in range(get_world_size()):
	for i in range(get_world_size()):
		till()
		plant(Entities.Carrot)
		move(North)
	move(East)

while True:
	for i in range(get_world_size()):
		while True:
			if can_harvest():
				harvest()
				plant(Entities.Carrot)
				break
		move(North)
	move(East)
# Heyo!