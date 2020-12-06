def change(path):
	with open(path, 'r') as file:
		data = file.read()
	data_1 = data.split('\n')
	data_2 = []
	for i in data_1:
		data_2.append('GeneID:' + i + '\n')
	with open(path, 'w') as file:
		for i in data_2:
			file.writelines(i)
