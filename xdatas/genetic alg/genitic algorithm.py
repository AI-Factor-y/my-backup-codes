import random
import string
import sys

from fuzzywuzzy import fuzz

in_str = 'AbhinaV'
in_str_len = len(in_str)
population = 20
generations = 10000


class Agent:

    def __init__(self, length):

        self.string = ''.join(random.choice(string.ascii_letters) for _ in range(length))               #creating random strings of prescribed length
        self.fitness = -1                   # setting fitness value default as one

    def __str__(self):

        return f'String: {self.string} Fitness: {self.fitness}'


def init_agents(population, length):

    return [Agent(length) for _ in range(population)]  #returning all the agents


def fitness(agents):

    for agent in agents:

        agent.fitness = fuzz.ratio(agent.string, in_str)  # made the fitness for each agent

    return agents


def selection(agents):

    agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True)  # sorting the agents based on their fitness values in the reverse order
    print('\n'.join(map(str, agents)))
    agents = agents[:int(0.2 * len(agents))]  #taking top 20 percent of the agents for reproduction

    return agents              # returns the updated agents


def crossover(agents):

    offspring = []

    for _ in range((population - len(agents)) // 2):  # general loop for crossover

        parent1 = random.choice(agents)
        parent2 = random.choice(agents)
        child1 = Agent(in_str_len)
        child2 = Agent(in_str_len)
        split = random.randint(0, in_str_len)
        child1.string = parent1.string[0:split] + parent2.string[split:in_str_len]
        child2.string = parent2.string[0:split] + parent1.string[split:in_str_len]

        offspring.append(child1)
        offspring.append(child2)

    agents.extend(offspring)

    return agents


def mutation(agents):

    for agent in agents:

        for idx, param in enumerate(agent.string):

            if random.uniform(0.0, 1.0) <= 0.1:

                g_start = agent.string[0:idx]
                g_middle = random.choice(string.ascii_letters)
                g_end = agent.string[idx+1:in_str_len]

                agent.string = g_start + g_middle + g_end

    return agents


def ga():

    agents = init_agents(population, in_str_len)

    for generation in range(generations):

        print('Generation: ' + str(generation))

        agents = fitness(agents)
        agents = selection(agents)
        agents = crossover(agents)
        agents = mutation(agents)

        if any(agent.fitness >= 90 for agent in agents):

            print('Threshold met!')
            sys.exit(0)


if __name__ == '__main__':

    ga()
