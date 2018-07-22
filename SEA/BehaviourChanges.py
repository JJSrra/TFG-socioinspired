import numpy as np
from Manners import Manner2, Manner3, Manner4

def BehaviourChanges(population, population_fitness, history, status_best, emotion, lower_threshold, upper_threshold, k1, k2, k3):

    # Select as 'bad population' individuals with emotion index lesser than lower threshold
    bad_population = np.where(emotion < lower_threshold)

    # Select as 'average population' individuals with emotion index between lower and upper thresholds
    average_population = np.where(np.logical_and(emotion >= lower_threshold, emotion < upper_threshold))

    # Select as 'good population' individuals with emotion index greater than or equal to upper threshold
    good_population = np.where(emotion >= upper_threshold)

    # Perform appropriate change to bad population
    if(len(bad_population[0] > 0)):
        population[bad_population] += np.array([Manner2(individual, status_best, k2) 
                for individual in population[bad_population]])

    # Perform appropriate change to average population
    if(len(average_population[0] > 0)):
        population[average_population] += np.array([Manner3(individual, individual_best, status_best, population, k1, k2, k3) 
                for (individual, individual_best) in zip(population[average_population], history[average_population])])
    
    # Perform appropriate change to good population
    if (len(good_population[0] > 0)):
        population[good_population] += np.array([Manner4(individual, individual_best, population, k1, k3) 
                for (individual, individual_best) in zip(population[good_population], history[good_population])])

    return population