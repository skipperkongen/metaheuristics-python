from metaheuristics.sorting import solve_genetic, fitness, get_problem

def test_sorting():
    problem = get_problem(n=10)
    solution, epoch = solve_genetic(problem)
    assert fitness(solution) == 0
