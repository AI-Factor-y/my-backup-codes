







def create_level():
	file=open("data_file.txt")

	lines=file.readlines()
	print(len(lines))

	arr=[]
	for i in range(len(lines)):
		arr.append([])

	for i in range(len(lines)):
		for _ in range(len(lines[1])-1):
			arr[i].append(0)
	k=0
	for x,line in enumerate(lines):
		
		for y,elem in enumerate(line):
			if elem=='=':
				arr[x][y]=1
			elif elem=='+':
				arr[x][y]=1
			elif elem=='-':
				arr[x][y]=8
			elif elem=='g':
				arr[x][y]=4+k
				k+=1
			elif elem=='p':
				arr[x][y]=3
			elif elem=='*':
				arr[x][y]=2

	return arr


