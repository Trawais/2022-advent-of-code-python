# 2022-advent-of-code-python
This repository is my solution for [Advent of Code 2022](https://adventofcode.com/2022) game in Python

## Supported Python version
This project is developed and tested on Python v3.11.0

### Pyenv
I recommend to use `pyenv` for handling correct Python version on your system.

## How to run?
`python ./tasks/00/test.py`

## How to prepare folder for the task?
Change `00` to your desired task number in the command below and run it.
Note: You must change it on two places.

```
TASK=00 docker run \
  --env TASK --rm -v ${PWD}:/var/www -w /var/www \
  -u $(id -u ${USER}):$(id -g ${USER}) \
  -v $PWD:/repo \
  hairyhenderson/gomplate:v3.11.3-alpine \
  --input-dir /repo/tasks/template --output-dir /repo/tasks/00
```