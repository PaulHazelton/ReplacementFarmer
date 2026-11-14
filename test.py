import auto_all_grass
import auto_all_wood
import auto_all_carrots
import on_all_cells
import harvest_when_ready

def main():

	#clear()
	#print("x:", get_pos_x(), "y:", get_pos_y())

	#auto_all_grass.main(10000)
	clear()
	on_all_cells.main(till)

if __name__ == "__main__":
	main()
