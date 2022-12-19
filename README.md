# 2022-advent-of-code-python
This repository is my solution for [Advent of Code 2022](https://adventofcode.com/2022) game in Python

## Supported Python version
This project is developed and tested on Python v3.11.0

### Pyenv
I recommend to use `pyenv` for handling correct Python version on your system.

## How to run?
```
python ./tasks/99/test.py
```

Some tasks (e.g.: [#11](https://github.com/Trawais/2022-advent-of-code-python/blob/main/tasks/11/solution.py#L8) ) are sensitive to environment variable `DEBUG`.
If `DEBUG` is set, some additional debug output is printed to stdout.
Example command with debug output turned on
```
DEBUG=1 python ./tasks/11/test.py
```

## How to prepare folder for the task?
You can use prepared command from Makefile:
```
TASK=99 make prepare
```
