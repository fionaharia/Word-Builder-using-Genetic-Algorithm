import DNA
import random

population = []
totalPopulation = 10
mutationRate = 0

def setup(population,totalPopulation):
      
    mutationRate = 0.01
    
    for i in range(totalPopulation):
        population.append(DNA.DNA())

def draw():
    
    offsprings = []
    for i in range(totalPopulation):
            mother = getParent(population)
            father =getParent(population)

            while(mother == father):
                father = getParent(population)
            offspring1, offspring2 = population(mother,father)
            offsprings.append(offspring1)
            offsprings.append(offspring2)
    offsprings += population
    offsprings.sort(key = lambda x : x.fitness(),reverse=False)
    population = offsprings[:100]
    
    
def getParent(population):
    if random.random() > 0.5:
        # Tournament Selection
        return tournamentSelection(population)
    else : 
        # Biased Random Selection
        return biasedRandomSelection(population)
    
def tournamentSelection(population):
        candidate1 = population[random.randint(0,totalPopulation-1)]
        candidate2 =population[random.randint(0,totalPopulation-1)]

        while(candidate1 == candidate2):
            candidate2 = population[random.randint(0,totalPopulation-1)]
        
        if candidate1.fitness < candidate2.fitness:
            return candidate1
        else:
            return candidate2
    
def biasedRandomSelection(population):
    fitnessSum = 0
    for i in population:
        fitnessSum += i.fitness
    proportions = [fitnessSum/i.fitness for i in population]
    proportionsSum = sum(proportions)
    normalizedProportions = [p/proportionsSum for p in proportions]

    cumulativeProportions = []
    cumulativeTotal = 0
    for np in normalizedProportions:
        cumulativeTotal += np
        cumulativeProportions.append(cumulativeTotal)

    selectedValue = random.random()

    for i in range(totalPopulation):
        if selectedValue <= cumulativeProportions[i]:
            return population[i]
    return population[random.randint(0,totalPopulation - 1)] # Redundand

        
setup(population,totalPopulation)

while population[0].fitness <= 44 :
    for i in range(totalPopulation):
        print("".join(population[i].genes))
    draw()

    

   
   
   



