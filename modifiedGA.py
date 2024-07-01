'''
Ali Can Canbay - acanbay
21/11/2022

This Python module comprises a modified Genetic Algorithm where a new intermediate step, gene variation, 
is introduced, and a mutation defined by a Gaussian distribution with a standard deviation that adjusts 
based on the results of each generation. It is capable of optimizing multiple parameters (even in cases of 
correlation between them - in such instances, it is advisable to maintain a high number of generations).

===Setting the optimization object
    
    mGA = algorithm( popSize, nGen, nVar, mins, maxs, problem, optimType, info )

    Required parameters:
        popSize   : Population size (must be at least 10)
        nGen      : Number of generations
        nVar      : Number of variables
        mins      : Minimum value in the parameter space of possible values for the variables
        maxs      : Maximum value in the parameter space of possible values for the variables
        problem   : The problem to be used in optimization

        Warning!
        The values of mins and maxs should consist of as many as nVar value.
        The problem should take variables as parameters and return the result of the function.

    Non-required parameters:
        seed      : Sets the initial value of the random number generator as a function of the given number.
                    Using the same seed will always yield the same result.
                    integer

        optimType : Optimization type - 'minimum' or 'maximum' (defaul value is 'minimum')
                    'minimum', optimizes the problem to the minimum value.
                    'maximum', optimizes the problem to the maximum value.

        info      : Enable or disable showing information during calculation. 
                    bool (default value is True)

===Optimizing and getting results
        
    results, values = mGA.optimize()

    It returns the most optimal result and the parameters associated with this results.

===Saving the results

    mGA.saveResults( name, graph, xlabel, ylabel, title )

    Non-required parameters:
        name      : Name of the file/graph which the results will be written (default value is 'results')
        graph     : Specifies whether to create a plot (default value is False)
        xlabel    : Label of the x-axis on the graph (default value is 'Generations')
        ylabel    : Label of the y-axis on the graph (default value is 'Fitness')
        title     : Title of the graph (default is empty)
'''
import random
import math
import time
import sys
class algorithm():
    def __init__(self,popSize,nGen,nVar,mins,maxs,problem,seed=None,optimType='minimum',info=True):
        self.sigma = math.pi/3

        if type(mins)==int or type(mins)==float:
            mins = [mins]
        if type(maxs)==int or type(maxs)==float:
            maxs = [maxs]
        #
        if seed != None:
            if type(seed) != int:
                print()
                print('Seed value must be an integer!')
                print()
                sys.exit(1)
            else:
                random.seed(seed)
        #
        if popSize < 10:
            print()
            print('Population size must be at least 10!')
            print()
            sys.exit(1)
        elif not( len(mins) == len(maxs) == nVar ):
            print()
            print('Maximums and minimums should contain as many values as the number of parameters!')
            print()
            sys.exit(1)
        elif optimType.lower() not in ['minimum', 'maximum', 'minimize', 'maximize']:
            print()
            print("Optimization type must be 'minimum' or 'maximum'")
            print()
            sys.exit(1)
        if optimType.lower() == 'minimize':
            optimType = 'minimum'
        elif optimType.lower() == 'maximize':
            optimType = 'maximum'
        #
        self.popSize = popSize
        self.nGen = nGen
        self.nVar = nVar
        self.minX = mins
        self.maxX = maxs
        self.problem = problem
        self.type = optimType
        self.info = info
        #
        self.X = self.generatePopulation()
        self.selection = int( popSize*10/100 )
        self.values = []
        self.results = []

    def generatePopulation(self):
        X=[]
        for i in range(self.popSize):
            chromosome = []
            for val in range(self.nVar):
                chromosome.append( random.uniform(self.minX[val],self.maxX[val]) )
            X.append(chromosome[:])
        return X
    
    def rouletteChoice(self, pool):
        index = abs( int( random.gauss(0,self.selection) ) )
        return pool[index]

    def crossover(self, parent1, parent2):
        if self.nVar == 1:
            ratio = 0.5
        else:
            ratio = 1/self.nVar
        offSpring = []
        for i in range(self.nVar):
            if random.random() < ratio:
                offSpring.append( (parent1[i]+parent2[i])/2 )
            else:
                if random.random() < 0.5:
                    offSpring.append( parent1[i] )
                else:
                    offSpring.append( parent2[i] )
        return offSpring
    
    def mutation(self, offSpring):
        if self.nVar == 1:
            ratio = 0.5
        else:
            ratio = 1/self.nVar
        for i in range(self.nVar):
            if random.random() < ratio:
                gene = offSpring[i] * random.gauss(1, self.sigma)
                if self.minX[i] < gene < self.maxX[i]:
                    offSpring[i] = gene
        return offSpring

    def nextGeneration(self):
        population = self.X[:]

        ## Fitness
        if self.type == 'minimum':
            population=sorted(population, key=self.problem)
        else:
            population=sorted(population, key=self.problem, reverse=True)
        
        new_population=population[:1]
        for i in range(self.popSize-1):
            parent1 = self.rouletteChoice(population)
            parent2 = self.rouletteChoice(population)

            offSpring = self.crossover( parent1, parent2 )
            offSpring = self.mutation(offSpring)
            new_population.append(offSpring)
        self.X=new_population

        ## Find new sigma
        if len(self.results)>1:
            dx = math.sqrt( sum( [ (self.values[-2][i] - self.values[-1][i])**2 for i in range(self.nVar) ] ) )
            dy = self.results[-2] - self.results[-1] 
            if dx != 0 and dy>0:
                deriv = dy/dx
                if deriv > math.pi/3:
                    deriv = math.pi/3
                self.sigma=deriv

    def optimize(self):
        start_time = time.time()
        for n in range(self.nGen):
            self.nextGeneration()
            self.values.append( self.X[0] )
            self.results.append( self.problem( self.values[-1] ) )       
            if self.info:
                print(f'{n+1}. Generation:  Result={self.results[-1]},  Values={self.values[-1]}')
        end_time = time.time()
        hour, rem = divmod(end_time-start_time, 3600)
        minute, second = divmod(rem, 60)
        str_time = '{:0>2}:{:0>2}:{:05.2f}'.format(int(hour),int(minute),second)
        self.str_time = str_time
        if self.info:
            print()
            print('Result =', self.results[-1])
            print('Values =', self.values[-1])
            print()
            print(f'Calculation time: {str_time}')
            print()
        return self.results[-1], self.values[-1]

    def saveResults(self,name='results',graph=False,xlabel='Generations',ylabel='Fitness',title=''):
        output_file = open(f'./{name}.txt', 'w')
        output_file.writelines(['Best Solutions:\n'])
        output_file.writelines([f'\t Result\t: {self.results[-1]}\n'])
        output_file.writelines([f'\t Values\t: {self.values[-1]}\n\n\n'])
        output_file.writelines(['\nAll Solutions:\n'])
        for n in range(self.nGen):
            output_file.writelines([f'{n+1}. Generation:  Result={self.results[n]},  Values={self.values[n]}\n'])
        output_file.writelines([f'\nCalculation time: {self.str_time}\n'])
        output_file.close()

        if graph:
            import matplotlib.pyplot as plt
            xs = range(1,self.nGen+1)
            plt.plot(xs,self.results)
            if title != '':
                plt.title(f'{title}')
            plt.xlabel(f'{xlabel}', horizontalalignment='right', x=1.0)
            plt.ylabel(f'{ylabel}', horizontalalignment='right', y=1.0)
            plt.xlim([0,self.nGen])
            if max(self.results)/min(self.results)>=1e3:
                plt.yscale('log')
            plt.grid(True, which='both', alpha=0.3)
            plt.savefig(f'{name}.png',dpi=400)
