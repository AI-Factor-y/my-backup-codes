
import random

target="abhinav"

population_size=100
mutation_rate=0.02
letters="abcdefghijklmnopqrstuvwxyz "
letters=[letter for letter in letters]

gene_size=len(target)
class DNA:

	def __init__(self):
		global gene_size
		self.gene_size=gene_size
		self.gene=""
		self.fitness=0
		for i in range(self.gene_size):
			self.gene+=random.choice(letters)
		self.gene=[genes for genes in self.gene]

	def calc_fitness(self):
		global target
		score=0
		for x,g in enumerate(self.gene):
			if g==target[x]:
				score+=1

		self.fitness=score/self.gene_size

		
	def crossover(self,pair):

		midpoint=random.randint(0,self.gene_size)
		child=DNA()
		for i in range(self.gene_size):
			if i<midpoint:
				child.gene[i]=self.gene[i]
			else:
				child.gene[i]=pair.gene[i]

		return child

	def mutation(self):

		for i in range(self.gene_size):
			if random.random()<mutation_rate:
				self.gene[i]=random.choice(letters)


	def create_string(self):
		string="".join(self.gene)

		return string






population=[]
counter=0
def genetic_alg():
	global population,counter,population_size

	counter+=1

	for i in range(population_size):
		population.append(DNA())

	
	for i in range(population_size):
		
		population[i].calc_fitness()


	#checking for target string:
	for i in range(population_size):
		print(population[i].create_string())
		if population[i].create_string()==target:
			print(f"target found at {counter} iteration")
			exit()

	mating_pool=[]

	for i in range(population_size):
		fitness_percent=int(population[i].fitness*100)

		for j in range(fitness_percent):
			mating_pool.append(population[i])
	

	for i in range(population_size):

		parent_1=random.choice(mating_pool)
		parent_2=random.choice(mating_pool)

		child=parent_1.crossover(parent_2)

		population[i]=child

	for i in range(population_size):

		population[i].mutation()

while True:
	genetic_alg()



