# Soccer League Competition Algorithm (For Continuous Decision Variables)
# Developed By: Naser Moosavian
# Translated to Python By: Juanjo Sierra

import numpy as np
from CreateInitialLeague import *
from Competition import *

if __name__ == "__main__":

    # Define Cost Funcion

    # Define settings of the problem
    settings = {'number_of_function_evaluation': 50000, 'dim': 10, 'nteams': 5,
                'lower_bound': 0, 'upper_bound': 10, 'neval': 0, 'max_it': 10**8,
                'mutation_probability': 0.1, 'mutation_rate': 0.2}

    # Number of main and subs players are equal to the dimension of the problem,
    # although this may change
    settings['nmain'] = settings['dim']
    settings['nsubs'] = settings['dim']

    league_main, league_subs, fitness_main, fitness_subs = CreateInitialLeague(settings)

    Competition(league_main, league_subs, fitness_main, fitness_subs, settings)