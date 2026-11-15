def print_list(list, name = None):
	contents = "Printing list: ["

	if (name != None):
		contents = name + ": ["
	
	for item in list:
		contents += item + ", "
	
	contents += "]"
	
	quick_print(contents)