import random

target = "to be or not to be that is the only question"

class DNA:
    gene_length = 44
    genes = [-1 for i in range(gene_length)]
    fitness = 0
    
    
    def __init__(self):
        for i in range(self.gene_length):
            self.genes[i] = chr(random.randint(65,122))
            
        score = 0
        
        for i in range(self.gene_length):
        
            if self.genes[i] == target[i]:
                score += 1
            self.fitness = score/len(target)
        
    
            
    def crossOver(self , partner):
        
        child = DNA()
        
        midpoint = random.randint(0,self.gene_length-1)
        
        for i in range(self.gene_length):
            if i>midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]
        
        return child

    def mutate(self , mutataionRate):
        
        for i in range(self.gene_length):
            if random.random() < mutataionRate:
                self.genes[i] = chr(random.randint(65,122))
    

        