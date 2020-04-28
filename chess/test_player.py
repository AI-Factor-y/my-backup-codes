from network import Network 

arr=[2]
n=Network()
while True:

	p=n.send(arr)
	try:
		for i in range(8):
			print(p[i])
	except:
		pass




