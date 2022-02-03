import random

def combine(a, b):
    return [
        random.choice([i,j])
        for i,j
        in zip(a,b)
    ]

def permute(specimen, n_swaps=1):
    # copy
    copy = list(specimen)
    # perform random swaps
    for _ in range(n_swaps):
        # randomly swap two positions
        i = random.randint(0, len(copy)-1)
        j = random.randint(0, len(copy)-1)
        # i = random.randint(0, len(copy)-2)
        # j = i + 1
        temp = copy[i]
        copy[i] = copy[j]
        copy[j] = temp
    return copy

def permute_eps(specimen, fitness, n_swaps=1, epsilon=0.1):
    # copy
    copy = list(specimen)
    # perform random swaps
    for _ in range(n_swaps):
        # randomly swap two positions
        i = random.randint(0, len(copy)-1)
        j = random.randint(0, len(copy)-1)
        # i = random.randint(0, len(copy)-2)
        # j = i + 1
        temp = copy[i]
        copy[i] = copy[j]
        copy[j] = temp
    if fitness(copy) < fitness(specimen) or random.random() > epsilon:
        return copy
    return list(specimen)

def mean(l):
    return sum(l) / len(l)
