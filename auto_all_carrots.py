import harvest_when_ready

def main():
	clear()

	for x in range(get_world_size()):
		for i in range(get_world_size()):
			till()
			if (plant(Entities.Carrot) == False):
				print("You're broke!")
				return
			move(North)
		move(East)

	while True:
		for i in range(get_world_size()):
			harvest_when_ready.main()
			if (plant(Entities.Carrot) == False):
				print("You're broke!")
				return
			move(North)
		move(East)

if __name__ == "__main__":
	main()
