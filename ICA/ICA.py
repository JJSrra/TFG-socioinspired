# Imperialist Competitive Algorithm: A Socio Politically Inspired Optimization Strategy
# Developed By: Esmaeil Atashpaz Gargari
# Translated to Python By: Juanjo Sierra

import numpy as np
from GenerateNewCountries import *
from CreateInitialEmpires import *
from AssimilateColonies import *
from RevolveColonies import *
from PosessEmpire import *
from UniteSimilarEmpires import *
from ImperialisticCompetition import *

def ICA(CostFunction, dim=10, ncountries=200, nimperialists=8, decades=2000,
        evaluation_criteria=False, max_eval=10000, revolution_rate=0.3, assimilation_coef=2,
        assimilation_angle_coef=np.pi/4, zeta=0.1, damp_ratio=0.99, stop_if_just_one_empire=False,
        uniting_threshold=0.02, lower_bound=0, upper_bound=10, initial_population_lower_bound=None,
        initial_population_upper_bound=None):

    # Zarib is used to prevent the weakest empire to have a probability of zero
    zarib = 1.05
    # Alpha is the importance of the mean minimun compared to the global minimum. Must be << 1
    alpha = 0.1
    # Domain of the problem, tuple including lower and upper bounds
    domain = (lower_bound, upper_bound)
    initial_domain = (initial_population_lower_bound, initial_population_upper_bound)

    # Generation of the initial countries
    initial_countries = GenerateNewCountries(ncountries, dim, domain, initial_domain)
    
    # New countries' cost/fitness is calculated
    fitness = np.apply_along_axis(CostFunction, 1, initial_countries)
    
    # Get initial evaluations if evaluations criteria is active
    if evaluation_criteria:
        evaluations = len(fitness)

    # And now the countries get sorted by their fitness
    order = np.argsort(fitness)
    fitness = fitness[order]
    initial_countries = initial_countries[order]

    # Initial empires are defined
    imperialists, imperialists_fitness, colonies, colonies_fitness, empires_total_cost = CreateInitialEmpires(initial_countries,
                                fitness, nimperialists, zeta)

    current_decade = 0

    # Main loop
    evaluations_marker = 0
    evaluation_marks = np.array([])
    while (evaluation_criteria and (evaluations < max_eval)) or (not evaluation_criteria and (current_decade < decades)):
        revolution_rate = damp_ratio*revolution_rate

        for i in range(0,len(imperialists)):
            # Assimilation: movement of colonies towards imperialists (Assimilation Policy)
            colonies[i], colonies_fitness[i], assimilation_evaluations = AssimilateColonies(imperialists[i],
                                colonies[i], domain, assimilation_coef, CostFunction)

            # Empire posession: if a colony has a lower cost than its imperialist, they switch positions
            imperialists[i], imperialists_fitness[i], colonies[i], colonies_fitness[i] = PosessEmpire(imperialists[i],
                                imperialists_fitness[i], colonies[i], colonies_fitness[i])

            # Revolution: a sudden change in the socio-political characteristics
            colonies[i], colonies_fitness[i], revolution_evaluations = RevolveColonies(colonies[i],
                                colonies_fitness[i], domain, initial_domain, revolution_rate, CostFunction)

            # Empire posession again
            imperialists[i], imperialists_fitness[i], colonies[i], colonies_fitness[i] = PosessEmpire(imperialists[i],
                                imperialists_fitness[i], colonies[i], colonies_fitness[i])

            # Compute the current cost for each empire
            empires_total_cost[i] = imperialists_fitness[i] + zeta * np.mean(colonies_fitness[i])

        # Similar empires are merged into a bigger empire
        imperialists, imperialists_fitness, colonies, colonies_fitness, empires_total_cost = UniteSimilarEmpires(imperialists,
                                imperialists_fitness, colonies, colonies_fitness, empires_total_cost, domain, uniting_threshold, zeta)

        # The imperialistic competition takes place
        imperialists, imperialists_fitness, colonies, colonies_fitness, empires_total_cost = ImperialisticCompetition(imperialists,
                                imperialists_fitness, colonies, colonies_fitness, empires_total_cost)

        if len(imperialists) == 1 and stop_if_just_one_empire:
            break

        if evaluation_criteria:
            new_evaluations = assimilation_evaluations + revolution_evaluations
            evaluations += new_evaluations
        else:
            current_decade += 1

        if evaluations >= evaluations_marker:
            evaluation_marks = np.insert(evaluation_marks, len(evaluation_marks), min(imperialists_fitness))
            evaluations_marker += max_eval / 10 

        #print("Decade {:4}, best solution: {:e}".format(decade, min(imperialists_fitness)))

    return np.append(evaluation_marks, min(imperialists_fitness))