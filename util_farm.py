import util_afford
import util_mappers

def run_to_target(target: int, item: Item, routine: Callable) -> bool:

	# Local Functions ----

	def _is_complete() -> bool:
		return util_afford.is_complete(Items.Hay, target)

	def _target_met() -> bool:
		return util_afford.target_met(Items.Hay, target)

	# Processing ----

	if _is_complete():
		return _target_met()

	clear()
	change_hat(util_mappers.item_to_hat(item))

	routine(target, _is_complete)

	return _target_met()
