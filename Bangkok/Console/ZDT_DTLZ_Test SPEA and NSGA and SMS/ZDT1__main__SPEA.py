'''
Created on 17/08/2014

@author: quatrosem
'''
from emoa import GA
from deap import base
from deap import creator
from deap import tools
import array
import random
import json
import numpy
from deap.benchmarks.tools import diversity, convergence







if __name__=='__main__':

    #optimal_front = json.load(open("zdt1_front.json"))
    # Use 500 of the 1000 points in the json file
    #optimal_front = sorted(optimal_front[i] for i in range(0, len(optimal_front), 2))
    #optimal_front = json.load(open("zdt2_front.json"))
    #optimal_front = json.load(open("zdt3_front.json"))
    #optimal_front = json.load(open("zdt4_front.json"))
    optimal_front = json.load(open("zdt6_front.json"))


    NGEN = 500
    MU = 0.1
    CXPB = 0.3

    # stats = tools.Statistics(lambda ind: ind.fitness.values)
    # stats.register("avg", numpy.mean, axis=0)
    # stats.register("std", numpy.std, axis=0)
    # stats.register("min", numpy.min, axis=0)
    # stats.register("max", numpy.max, axis=0)
    #
    # logbook = tools.Logbook()
    # logbook.header = "gen", "evals", "std", "min", "avg", "max"

    #declare Genetic Algorithm for the problem
    ga = GA(CXPB=CXPB, MUTPB=MU, NGEN = NGEN,  num_population=100)
    #ga.ZDT1_init_SPEA3D()
    #ga.ZDT1_init_SPEA()
    #ga.ZDT2_init_SPEA()
    #ga.ZDT3_init_SPEA()
    #ga.ZDT4_init_SPEA()
    ga.ZDT6_init_SPEA()
    archive = ga.SetPopulationFakeBench(novo=10) #ATENCAOOOOOOO

    fitnesses = ga.GetFitness(archive)
    ga.AttachFitness(archive,fitnesses)




    ####################
    # first generation #
    ####################
    #set Population
    pareto=tools.ParetoFront()
    pop=ga.SetPopulation(ga.num_population)





    # Evaluate the entire population
    fitnesses = ga.GetFitness(pop)
    ga.AttachFitness(pop,fitnesses)
    pareto.update(pop)
    print "  generation: ",format(0, '03d')

    #record = stats.compile(pop)
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #logbook.record(gen=0, evals=len(invalid_ind), **record)
    #logbook.record(gen=0, evals=len(fitnesses), **record)
    #print(logbook.stream)



    for i in range(1,ga.NGEN):

        # Select the next generation individuals
        ga.Selection_SPEA(pop, archive)
        pareto.update(pop)

        #record = stats.compile(pop)
        #logbook.record(gen=i+1, evals=len(pop), **record)
        #print(logbook.stream)
        print "  generation: ",format(i, '03d')





    pop.sort(key=lambda x: x.fitness.values)

    #print(stats)
    print("Convergence: ", convergence(pop, optimal_front))
    print("Diversity: ", diversity(pop, optimal_front[0], optimal_front[-1]))

    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    import numpy


    front = numpy.array([ind.fitness.values for ind in archive])


    #optimal_front = numpy.array(optimal_front)
    #plt.scatter(optimal_front[:,0], optimal_front[:,1], c="r")
    plt.scatter(front[:,0], front[:,1], c="b")
    plt.axis("tight")
    # plt.ylim([-0.2,1.2])
    # plt.xlim([-0.2,1.2])

    plt.show()

    # fig1 = plt.figure()
    # ax = fig1.add_subplot(111, projection='3d')
    # ax.set_xlim([-0.2,1.2])
    # ax.set_ylim([-0.2,1.2])
    # ax.set_zlim([-0.2,1.2])
    # ax.scatter(front[:,0], front[:,1], front[:,2], marker='+', c='lightgrey', alpha=1, label='Pareto front')
    # plt.show()
    #
    #
