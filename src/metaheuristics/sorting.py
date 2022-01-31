import random
import pdb

def get_seed(n=100):
    l = list(range(n))
    random.shuffle(l)
    return l

def init_population(seed, pop_size=100):
    return [seed] + [
        random.sample(seed, len(seed))
        for _ in range(pop_size-1)
    ]

def fitness(specimen):
    errors = [i < j for i, j in zip(specimen, [0] + specimen[:-1])]
    return sum(errors)

def combine(a, b):
    # would not work, because does not preserve integrity of list
    return [
        random.choice([i,j])
        for i,j
        in zip(a,b)
    ]

def mutate(specimen, n_swaps=5):
    # perform random swaps

    for _ in range(n_swaps):
        i = random.randint(0, len(specimen)-1)
        j = random.randint(0, len(specimen)-1)
        # swap position of two random numbers
        specimen[i] = specimen[i] + specimen[j]
        specimen[j] = specimen[i] - specimen[j]
        specimen[i] = specimen[i] - specimen[j]

    return specimen

def next_generation(pop):
    weights = [1/(fitness(spec)+1) for spec in pop]
    sample_best = random.choices(pop, weights=weights, k=len(pop))
    new_pop = [
        mutate(specimen)
        for specimen in sample_best
    ]
    return new_pop

def get_best(pop):
    specimen = sorted(pop, key=lambda spec: fitness(spec))[0]
    return fitness(specimen), specimen

def solve_genetic(seed, max_epoch=1000):
    pop = init_population(seed)
    epoch = 0
    best = input
    while epoch < max_epoch:
        fitness_best, best = get_best(pop)
        print(f'Epoch {epoch}, best fitness:', fitness_best)
        if fitness_best == 0:
            break
        pop = next_generation(pop)
        epoch += 1
    return best
    #return sorted(input)
