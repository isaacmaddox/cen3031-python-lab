# Python Lab

This lab will hopefully give you a good understanding of some basic Python features to get you ready for the rest of the assignments for this semester.

### Data

The data used for this app can be found in app/data.py. You can reference this during development to see the shape of data

## Getting started

To get the lab working, run the following commands:

```bash
git clone https://github.com/isaacmaddox/cen3031-python-lab
cd cen3031-python-lab
uv sync # Install dependencies
uv pip install -e . # Register project scripts
```

## Running problems

You can run individual problems to test your output as you go along:

```bash
uv run all # Runs all problems, excluding the bonus
uv run problem-1 # Runs only problem 1
uv run bonus # Runs only the bonus
```

## Checking your work

To check your work for correctness, you can use pytest:

```bash
uv run pytest
```
