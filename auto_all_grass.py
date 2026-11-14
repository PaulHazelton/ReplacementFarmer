import harvest_when_ready

def main():
	clear()
	while True:
		for i in range(get_world_size()):
			harvest_when_ready.main()
			move(North)
		move(East)

if __name__ == "__main__":
	main()
