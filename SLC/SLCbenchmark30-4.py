import optproblems.cec2005
import numpy as np
import time
from SLC import *
import os

if __name__ == "__main__":
    dim = 30
    repeats = 10
    evaluations = 10000*dim
    teams = 5
    main_players = 3
    sub_players = 3
    mutation_probability = 0.1
    mutation_rate = 0.2

    if not os.path.exists('results'):
        os.makedirs('results')

    if not os.path.exists('convergence'):
        os.makedirs('convergence')

    np.random.seed(10)

    f4 = optproblems.cec2005.F4(dim)

    time1 = time.time()
    results = np.array([SLC(f4, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-100, upper_bound=100) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-results-30-4.txt", "w") as file:
        print("F4: Shifted Schwefel's Problem 1.2 with Noise in Fitness", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)

    with open("convergence/SLC-convergence-30-4.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)   
    
    f9 = optproblems.cec2005.F9(dim)

    time1 = time.time()
    results = np.array([SLC(f9, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-5, upper_bound=5) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-results-30-9.txt", "w") as file:
        print("F9: Shifted Rastrigin's Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SLC-convergence-30-9.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f12 = optproblems.cec2005.F12(dim)

    time1 = time.time()
    results = np.array([SLC(f12, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-np.pi, upper_bound=np.pi) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-results-30-12.txt", "w") as file:
        print("F12: Schwefel's Problem 2.13", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SLC-convergence-30-12.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f21 = optproblems.cec2005.F21(dim)

    time1 = time.time()
    results = np.array([SLC(f21, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-5, upper_bound=5) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-results-30-21.txt", "w") as file:
        print("F21: Rotated Hybrid Composition Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SLC-convergence-30-21.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f22 = optproblems.cec2005.F22(dim)

    time1 = time.time()
    results = np.array([SLC(f22, dim=dim, max_eval=evaluations, nteams=teams,
        nmain=main_players, nsubs=sub_players, mutation_probability=mutation_probability,
        mutation_rate=mutation_rate, lower_bound=-5, upper_bound=5) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/SLC-results-30-22.txt", "w") as file:
        print("F22: Rotated Hybrid Composition Function with High Condition Number Matrix", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/SLC-convergence-30-22.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)
