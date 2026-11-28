# Notes:
# Assume an even size field.
# 
# The normal zig zag algorithm:
# Go all the way up, right one, all the way down but leave the bottom row empty, right one, repeat.
# Repeat that until you get to the rightmost end, then use the bottom row to go back to 0,0
# 
# Invariants:
# - If in row 0, move left all the way back to 0,0
# - If in row 1, move right
# - If in top row, move right
# - If in even column, move up
# - If in odd column, move down
# 
# How we make it faster:
# 
# If snake length is too long, just fall back to the normal zig zag algorithm.
# If it's short enough:
# - Follow zig zag to the next decision_node
#   - A decision_node is any cell in the top row
# - If apple in is an odd column, move right to apple_y, resume zig zag
# - If apple is in an even column, move right to apple_y - 1, resume zig zag
# - The whole time we must keep the invariants above.
# ----

import util_afford
import util_exceptions
import util_snake
import util_traversal
import util_wait

def run_to_target(target: int) -> bool:

	if (_is_complete(target)):
		return _target_met(target)

	_run(target)

	return _target_met(target)

# Primary Functionality ----

def _run(target: int):

	def _setup():

		clear()
		set_world_size(8)

		# Till everything
		util_traversal.all_cells_multi(till)

		util_wait.wait_till_im_last()

		return

	def _takedown():
		clear()
		util_traversal.go_home()
		set_world_size(0) # type: ignore
		return

	_setup()

	while not _is_complete(target):
		_cycle()

	_takedown()

	return

def _cycle():

	change_hat(Hats.Dinosaur_Hat)

	apple_pos: tuple[int, int] = measure() # type: ignore

	_seek_apples(apple_pos)

	change_hat(Hats.Straw_Hat)

	util_traversal.go_home()

	return

# Snake Stuff ----

# Seeks apples until we can't move forward anymore
def _seek_apples(initial_apple_pos: tuple[int, int]):

	snake_length: int = 1
	threshold_length: int = 20

	apple_pos: tuple[int, int] = initial_apple_pos

	while snake_length < threshold_length:

		_move_to_next_apple(apple_pos)

		apple_pos = measure() # type: ignore

		snake_length += 1

	print("LENGTH!")

	while _zig():
		continue

	return

def _move_to_next_apple(apple_pos: tuple[int, int]):
	
	pos = util_snake.get_pos()

	while not util_snake.points_are_equal(pos, apple_pos):
		if not _zig():
			break
		pos = util_snake.get_pos()
	
	return

# Move one cell in the right direction following invariants.
# Assume that the invariants above have been followed so far.
# Make no assumptions about starting location
def _zig() -> bool:

	end = get_world_size() - 1
	x, y = get_pos_x(), get_pos_y()

	# Consider corners first
	if (x == 0 and y == 0):
		return move(North)
	if (x == 0 and y == end):
		return move(East)
	if (x == end and y == end):
		return move(South)
	if (x == end and y == 0):
		return move(West)

	# Sort of like corners, excluding bottom row
	if (y == 1 and x == 0):
		return move(North)
	if (y == 1 and x == end):
		return move(South)

	# Turn-around on the bottom
	if (y == 1 and x % 2 == 0):
		return move(North)
	if (y == 1 and x % 2 == 1):
		return move(East)

	# Turn-around on top row
	if (y == end and x % 2 == 0):
		return move(East)
	if (y == end and x % 2 == 1):
		return move(South)

	# Bottom row not in a corner
	if (y == 0):
		return move(West)

	# Normal up and down
	if (x % 2 == 0):
		return move(North)
	else:
		return move(South)

	return

# Aliases ----

def _is_complete(target: int) -> bool:
	return util_afford.is_complete(Items.Bone, target)

def _target_met(target: int) -> bool:
	return util_afford.target_met(Items.Bone, target)
