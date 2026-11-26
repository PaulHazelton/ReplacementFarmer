# Notes
# 
# A node has 4 directions, each direction has one of 3 states:
# - home: When we first discover a node going East, set West to home.
# - new:  When we first discover a node, all possible exits (besides home) are marked as new.
# - dead: When we return to a node going East, set West to dead.
# 
# We simply move "forward" until we arrive at a node
# - If there's only 1 way to go, go that way (turn around from dead end)
# - If there's 2 ways to go, don't go backwards (keep track of last move direction)
#
# When leaving a node:
# - If there's any new paths, take the one that yields the minimum distance to treasure
# - If there are no new paths, go home
# 
# ----

import util_afford
import util_maze

# Public functions ----

def run_to_target(target: int) -> bool:

	if (_is_complete(target)):
		return _target_met(target)

	clear()
	change_hat(Hats.Gold_Hat)

	_cycle(target)

	return _target_met(target)

# Primary Functionality ----

def _cycle(target: int):

	while not _is_complete(target):

		util_maze.build_maze(get_world_size())
		util_maze.solve_maze()
		harvest()

		# setup()
		# use_item(Items.Weird_Substance, substance_amount())
	return

# Aliases ----

def _is_complete(target: int) -> bool:
	return util_afford.is_complete(Items.Gold, target)

def _target_met(target: int) -> bool:
	return util_afford.target_met(Items.Gold, target)
