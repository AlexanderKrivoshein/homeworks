# Реализовать две функции: write_to_file(data) и read_file_data(). Которые соотвественно: пишут данные в файл и читают данные из файла.

def read_file_data(file_name):
	print('Read file: begin\n')
	with open(file_name) as file:
		return file.read()

def write_to_file(data, file_name, mode='w'):
	with open(file_name, mode=mode) as file:
		file.write(data)

if __name__ == '__main__':
	print(read_file_data('README.md'))
	print('\nWrite file: befin')
	write_to_file('my text', 'file_to_write.txt')