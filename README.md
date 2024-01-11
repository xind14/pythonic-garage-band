# Lab: Class 4 - Garage Band with OOP

## Author: Xin Deng, chatGPT

## Links and Resources

- chatGPT on what certain errors meant


## Overview - madlib-cli

Creating a Garage Band with Object Oriented Programming.


## Feature Tasks and Requirements

- Create a local git repo with project named pythonic-garage-band
- Create a new repository named pythonic-garage-band
- Link your local and remote repositories.


1. Use Python classes to model a Band made up of different kinds of musicians.
2. Start with Guitarist, Bassist, and Drummer.
3. Make use of a Musician base class to handle common functionality which particular kinds of musicians will inherit.

**Band Tests:**

1. A Band instance should have a `name` attribute which is a string.
2. A Band instance should have a `members` attribute which is a list of instances that inherit from Musician base (or super) class.
3. A Band instance should have a `play_solos` method that asks each member musician to play a solo, in the order they were added to the band.
4. A Band instance should have appropriate `__str__` and `__repr__` methods.
5. A Band should have a class method `to_list` which returns a list of previously created Band instances.

**Musician Subclass Tests:**

1. Each kind of Musician instance should have appropriate `__str__` and `__repr__` methods.
2. Each kind of Musician instance should have a `get_instrument` method that returns a string.
3. Each kind of Musician instance should have a `play_solo` method that returns a string.

## Setup

### Creating Project

```bash
mkdir example-lab
cd example-lab
touch README.md
```

### Create virtual environment

```bash
python3 -m venv .venv
```

### Activate virtual environment

#### Mac/Linux

```bash
source .venv/bin/activate
```

### Git

#### On Local System

#### Initialize local Git repository

```bash
git init
touch .gitignore
```

Add `.venv` folder to `.gitignore`

```bash
git add .
git commit -m "first commit"
```

#### On GitHub site

- Create an EMPTY repository `example-lab` on GitHub.
  - DO NOT initialize with README, license, or gitignore. Those will be added soon.
  - The next screen will have a "Quick Setup" section with a URL available to copy. Copy it ;)

#### On Local System (again)

```bash
git remote add origin the_url_you_copied_that_ends_with_git
git push -u origin main
```

#### Create modules and scripts

- mkdir example_lab

- touch example_lab/example_script.py


#### Install packages

```For example:

pip install favorite-library

Record package dependencies
pip freeze > requirements.txt

Should result in this file tree:

└── example-lab
    ├── README.md
    ├── requirements.txt
    └── example_lab
        └── example_script.py

```

### Tests

Many labs will require automated testing. If your lab requires it then install `pytest` or `pytest-watch`.

`pip install pytest` # or pytest-watch

`pip freeze > requirements.txt`

`touch tests/__init__.py `(Note: 2 underscores on both sides.)

`touch tests/test_example.py`

Should result in a file tree like this:

```└── example-lab
    ├── README.md
    ├── requirements.txt
    ├── example_lab
    │   └── example_script.py
    └── tests
        ├── __init__.py
        └── test_example.py
```






