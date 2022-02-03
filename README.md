# metaheuristics-python
A repo with challenges to solve using metaheuristiccs

Example output from genetic sorting (lower fitness is better): 

```
Initial specimen  (fitness: 4): [6, 9, 3, 5, 8, 1, 4, 2, 0, 7]
Genetic algorithm searching...
Best specimen found after 83 epochs (fitness: 0): [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
0.4574515% of universe explored (~16600 specimens)
Universe contains 3628800 specimens
```

## Install

Create and activate venv (or use your own):

```bash
python3.9 -m venv venv
source venv/bin/activate
```

Install into active environment:

```bash
pip install -e '.[test]'
```

## Run

Run genetic sorting:

```bash
python src/metaheuristics/sorting.py
```

Test sorting:

```bash
make test_sorting
```
