# Assume an even size field

import util_afford
import util_traversal
import util_wait
import util_snake

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

	_seek_apples()

	change_hat(Hats.Straw_Hat)

	util_traversal.go_home()

	return

# Snake Stuff ----

def _seek_apples():

	while util_snake.zig_zag():
		continue

	return

# Aliases ----

def _is_complete(target: int) -> bool:
	return util_afford.is_complete(Items.Bone, target)

def _target_met(target: int) -> bool:
	return util_afford.target_met(Items.Bone, target)
