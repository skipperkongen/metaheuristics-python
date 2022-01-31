import random

def get_instance(n=100):
    l = list(range(n))
    random.shuffle(l)
    return l

def check_solution(l):
    for i,j in zip(l, [0] + l[:-1]):
        assert i > j
