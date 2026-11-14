while True:
	if can_harvest():
		harvest()
		plant(Entities.Carrot)
		move(North)