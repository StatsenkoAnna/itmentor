def read_cfg(filename):
	with open(filename, 'r', encoding='utf-8') as cfg_file:
		data = cfg_file.read()
		data = eval(data)
	return data
