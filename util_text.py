def print_list(list, name = None):

	if (name == None):
		quick_print("Printing list:")
	else:
		quick_print(name + ":")
	
	quick_print(list)

	# contents = "Printing list: ["

	# if (name != None):
	# 	contents = name + ": ["
	
	# for item in list:
	# 	contents += item + ", "
	
	# contents += "]"
	
	# quick_print(contents)