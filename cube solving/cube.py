
import random
import numpy as np
size=3



bot=[]
b=[]
f=[]
l=[]
r=[]
top=[]
for _ in range(size):
	bot.append([])
	b.append([])
	f.append([])
	l.append([])
	r.append([])
	top.append([])



names=['w','y','b','r','g','o',]

b_size=40




def fill_sides():
	global bot,b,f,l,r,top,size


	bot=[]
	b=[]
	f=[]
	l=[]
	r=[]
	top=[]
	for _ in range(size):
		bot.append([])
		b.append([])
		f.append([])
		l.append([])
		r.append([])
		top.append([])


	for i in range(size):
		
		for _ in range(size):	
			bot[i].append('w')
			b[i].append('y')
			f[i].append('b')
			l[i].append('r')
			r[i].append('g')
			top[i].append('o')

def normalizer():
	global bot,b,f,l,r,top,size
	for i in range(size):
		for j in range(size):
			for k in names:
				if k==bot[i][j]:
					bot[i][j]=names.index(k)/5
				if k==b[i][j]:
					b[i][j]=names.index(k)/5
				if k==f[i][j]:
					f[i][j]=names.index(k)/5
				if k==l[i][j]:
					l[i][j]=names.index(k)/5
				if k==r[i][j]:
					r[i][j]=names.index(k)/5
				if k==top[i][j]:
					top[i][j]=names.index(k)/5

def denormalize():
	global bot,b,f,l,r,top,size
	for i in range(size):
		for j in range(size):
			bot[i][j]=names[bot[i][j]]
			b[i][j]=names[b[i][j]]
			f[i][j]=names[f[i][j]]
			l[i][j]=names[l[i][j]]
			r[i][j]=names[r[i][j]]
			top[i][j]=names[top[i][j]]




def side_swap(side,rotation):
	global size
	if (rotation=='a'):
  
		i=side-1
		for j in range(size):

			temp_l=l[i][j]
			temp_bot=bot[i][j]
			temp_r=r[i][j]
			temp_top=top[i][j]
			bot[i][j]=temp_l
			r[i][j]=temp_bot
			top[i][j]=temp_r
			l[i][j]=temp_top
	if (rotation=='c'):
		i=side-1    
		for j in range(size):
	    
			temp_l=l[i][j]
			temp_bot=bot[i][j]
			temp_r=r[i][j]
			temp_top=top[i][j]
			bot[i][j]=temp_r
			r[i][j]=temp_top
			top[i][j]=temp_l
			l[i][j]=temp_bot

def top_swap(side,rotation):
	global size
	if (rotation=='c'):
		j=side-1
	    
		for i in range(size):
			temp_f=f[i][j]
			temp_top=top[i][j]
			temp_b=b[i][j]
			temp_bot=bot[i][j]
			top[i][j]=temp_f
			b[i][j]=temp_top
			bot[i][j]=temp_b
			f[i][j]=temp_bot

    
  
	if (rotation =='a'):
  
		j=side-1;
    
		for i in range(size):

			temp_f=f[i][j]
			temp_top=top[i][j]
			temp_b=b[i][j]
			temp_bot=bot[i][j]
			top[i][j]=temp_b
			b[i][j]=temp_bot
			bot[i][j]=temp_f
			f[i][j]=temp_top

def cube_state():
		
	total_cube=[]
	for _ in range(6):
		total_cube.append([])

	for i in range(6):
		for j in range(size):
			for k in range(size):
				if i==0:
					total_cube[i].append(bot[j][k])
				if i==1:
					total_cube[i].append(b[j][k])
				if i==2:
					total_cube[i].append(f[j][k])
				if i==3:
					total_cube[i].append(l[j][k])
				if i==4:
					total_cube[i].append(r[j][k])
				if i==5:
					total_cube[i].append(top[j][k])

	return total_cube
	



def print_mat():
	global size
	print("\nback face\n")
	for i in range(size):
		

		print(b[i])

  
	print("\nbottom face \n")
	for i in range(size):
		
		print(bot[i])

  
	print("\nfront face \n")
	for i in range(size):

		print(f[i])


  
	print("\nleft face \n")
	for i in range(size):

		print(l[i])

  
	print("\nright face \n")
	for i in range(size):

		print(r[i])



	print("\ntop face \n")
	for i in range(size):

		print(top[i])

def shuffle_cube(shuffle):
	for mov in shuffle:
		if mov[0]=='t':
			if mov[1]=='1':
				if mov[2]=='a':
					top_swap(1,'a')
				if mov[2]=='c':
					top_swap(1,'c')
			if mov[1]==str(size):
				if mov[2]=='a':
					top_swap(size,'a')
				if mov[2]=='c':
					top_swap(size,'c')
		if mov[0]=='s':
			if mov[1]=='1':
				if mov[2]=='a':
					side_swap(1,'a')
				if mov[2]=='c':
					side_swap(1,'c')
			if mov[1]==str(size):
				if mov[2]=='a':
					side_swap(size,'a')
				if mov[2]=='c':
					side_swap(size,'c')

def reverse_cube(shuffle):
	global size,solutions,cube_shuffles
	for mov in shuffle:
		if mov==1:
			cube_shuffles.append(cube_state())
			top_swap(1,'c')
			
			solutions.append(mov)
		if mov==0:
			cube_shuffles.append(cube_state())
			top_swap(1,'a')
			
			solutions.append(mov)
		if mov==3:
			cube_shuffles.append(cube_state())
				
			top_swap(size,'c')
			
			solutions.append(mov)

		if mov==2:
			cube_shuffles.append(cube_state())
			top_swap(size,'a')
			
			solutions.append(mov)

		if mov==5:
			cube_shuffles.append(cube_state())
		
			side_swap(1,'c')
			
			solutions.append(mov)
		if mov==4:
			cube_shuffles.append(cube_state())
			side_swap(1,'a')
			
			solutions.append(mov)

		if mov==7:
			cube_shuffles.append(cube_state())
				
			side_swap(size,'c')
			
			solutions.append(mov)
		if mov==6:
			cube_shuffles.append(cube_state())
			side_swap(size,'a')
			
			solutions.append(mov)

		

def normalize_shuffle(shuffle):
	global size,no_of_shuffles
	new_shuf1=[]
	for mov in shuffle:
		
		mov=[i for i in list(mov)]
		# print(mov)
		if mov[0]=='t':

			(mov[0])='0'
		if mov[0]=='s':
			(mov[0])='1'
		if mov[1]=='1':
			(mov[1])='0'
		if mov[1]==str(size):
			(mov[1])='1'
		if mov[2]=='c':
			(mov[2])='0'
		if mov[2]=='a':
			(mov[2])='1'
		new_shuf1.append(mov)
	new_shuf2=[]
	for mov in new_shuf1:
		# print(mov)
		mov=[int(i) for i in list(mov)]
		new_shuf2.append(mov)

	for i in range(len(new_shuf1),no_of_shuffles):
		new_shuf2.append([-1,-1,-1])
	#  possible cases 000,001,010,011,100,101,110,111
	#  t-0 s-1
	#  1-0 2-1
	#  c-0 a-1
	cases=[[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
	input_shuffle=[]
	for shuf in new_shuf2:
		# case 1
		for case in cases:
			if shuf==case:
				input_shuffle.append(cases.index(case))


			

	return input_shuffle













def shuf_gen(n):
	global size
	shuffle=[]
	# for i in range(random.randint(1,n)):

	# 		shuffle.append(random.choice(['t','s'])+random.choice(['1',str(size)])+random.choice(['a','c']))
	# return shuffle
	for i in range(n):

			shuffle.append(random.choice(['t','s'])+random.choice(['1',str(size)])+random.choice(['a','c']))
	return shuffle

#random shuffle









if __name__=="__main__":
	count=0
	no_of_shuffles=1
	cube_shuffles=[]
	solutions=[]
	while(count<1):
		fill_sides()
		normalizer()
		shuffle=shuf_gen(no_of_shuffles)
		# print(shuffle)
		shuffle_cube(shuffle)
		# print(shuffle)
		# print_mat()
		# print(cube_state())
		# cube_shuffles.append(cube_state())

		shuffle.reverse()
		shuffle=normalize_shuffle(shuffle)
		
		# print(shuffle)
		# print("==============================")
		# solutions.append(shuffle)
		reverse_cube(shuffle)
		# denormalize()
		print("_________________________")
		print_mat()
		print(count)
		
		count+=1

	print(cube_shuffles)
	# print("==========")
	print(solutions)

	np.save("cube_shuffles_3d_super",cube_shuffles,allow_pickle=True,fix_imports=True)
	np.save("solutions_3d_super",solutions,allow_pickle=True,fix_imports=True)

	# np.save("cube_shuffles_real_test_3d_super",cube_shuffles,allow_pickle=True,fix_imports=True)
	# np.save("solutions_real_test_3d_super",solutions,allow_pickle=True,fix_imports=True)

	
