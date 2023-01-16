# metaheuristics-python
A repo with challenges to solve using metaheuristiccs

## Introduction

Example output from genetic sorting (lower fitnes is better):

```
Initial specimen  (fitnes: 5): [9, 1, 5, 8, 7, 3, 6, 2, 0, 4]
Genetic algorithm searching...
Best specimen found after 13 epochs (fitnes: 0): [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
0.07164903% of universe explored (~2600 specimens)
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
