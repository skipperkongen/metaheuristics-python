# metaheuristics-python
A repo with challenges to solve using metaheuristiccs

```
$ python src/metaheuristics/sorting.py
Problem (fitness: 5): [9, 8, 5, 7, 2, 6, 0, 4, 1, 3]
Best solution found after 55 epochs (fitness: 0): [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
0.30313051% of universe explored (~11000 specimens)
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
