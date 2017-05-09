import ArcList

def readg(filename):
	file = open(filename, 'r')
	file_line = []
	num_list = []
	for line in file:
		line_list = line.split(' ')
		num_line = [int(el) for el in line_list]
		num_list.append(num_line)
	#print num_list
	num_of_nodes = num_list.pop(0)[0]
	left = []
	right = []
	cost = []
	for line in num_list:
		left.append(line[0])
		right.append(line[1])
		cost.append(line[2])
	arclist = ArcList.Arclist(num_of_nodes,cost,left,right)
	return arclist 
	
def main():
	readg('input.txt')

if __name__ == '__main__':
	main()