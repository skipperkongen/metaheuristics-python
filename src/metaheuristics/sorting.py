import random
import math
import numpy as np
from metaheuristics.genetic import permute, permute_eps

def get_problem(n=100):
    l = list(range(n))
    random.shuffle(l)
    return l

def init_pop(problem, pop_size=100):
    return [problem] + [permute(problem) for _ in range(pop_size-1)]

def fitness(specimen):
    # one error per decrease step
    errors = [i < j for i, j in zip(specimen, [0] + specimen[:-1])]
    return sum(errors)

def fitness2(specimen):
    # one error per decrease step
    weights = [item/(i+1) for i, item in enumerate(specimen)]
    return sum(weights)

def next_generation(pop):
    random_fitness = lambda: fitness if random.random() < 0.8 else fitness2
    pop_fits = [fitness(spec) for spec in pop]
    weights = [(max(pop_fits)+1-fit)**5 for fit in pop_fits]
    biased = random.choices(pop, weights=weights, k=len(pop))
    #biased_fits = [select_fitness()(spec) for spec in biased]
    new_pop = [
        permute_eps(specimen, fitness2)
        for specimen in biased
    ]
    return new_pop

def get_alpha(pop):
    alpha = sorted(pop, key=lambda spec: fitness(spec))[0]
    return alpha, fitness(alpha)

def solve_genetic(problem, max_epoch=1000, pop_size=100):
    pop = init_pop(problem, pop_size=pop_size)
    #print(pop)
    epoch = 0
    best = input
    best_fit = np.inf
    while epoch < max_epoch:
        distinct = np.unique(pop, axis=0)
        alpha, alpha_fit = get_alpha(pop)
        if alpha_fit < best_fit:
            best = alpha
            best_fit = alpha_fit
        # print(f'Epoch {epoch}, alpha_fit: {alpha_fit}, pop_size: {len(pop)}, n_distinct: {len(distinct)}' )
        if best_fit == 0:
            break
        pop = next_generation(pop)
        epoch += 1
    return best, epoch
    #return sorted(input)

if __name__=='__main__':
    n = 10
    max_epoch = 2000
    pop_size = 200
    problem = get_problem(n=n)
    print(f'Problem (fitness: {fitness(problem)}): {problem}')
    best, epoch = solve_genetic(problem, max_epoch=max_epoch, pop_size=pop_size)
    n_specimens = epoch*pop_size
    space_size = math.factorial(n)
    explored = round(100.0*n_specimens/space_size, 8)
    print(f'Best solution found after {epoch} epochs (fitness: {fitness(best)}): {best}')
    print(f'{explored}% of universe explored (~{n_specimens} specimens)')
    print(f'Universe contains {space_size} specimens')
