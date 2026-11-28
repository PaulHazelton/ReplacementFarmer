# Completes a full zig zag cycle with no regard to apple position
# Returns: True if the cycle was completed, false otherwise (usually due to running into snake body)
def zig_zag() -> bool:

	# Vars ----

	size = get_world_size()

	# Locals ----

	def _north_or_south():
		if (get_pos_x() % 2 == 0):
			return North
		else:
			return South

	def _process_column(dir: Direction) -> bool:

		for y in range(size - 2):
			if not move(dir):
				return False

		return True

	# Processing ----

	if not move(North):
		return False

	for x in range(size - 1):
		if not _process_column(_north_or_south()):
			return False
		if not move(East):
			return False

	if not _process_column(_north_or_south()):
		return False

	if not move(South):
		return False

	for x in range(size - 1):
		if not move(West):
			return False

	return True

def points_are_equal(a: tuple[int, int], b: tuple[int, int]) -> bool:
	
	x1, y1 = a
	x2, y2 = b
	
	return x1 == x2 and y1 == y2

def get_pos() -> tuple[int, int]:
	return (get_pos_x(), get_pos_y())