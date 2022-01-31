import random
from metaheuristics.sorting import solve_genetic, fitness, get_seed

def test_sorting():
    input = get_seed()
    output = solve_genetic(input)
    assert fitness(output) == 0
