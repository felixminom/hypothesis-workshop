"""
    Let's take a step further and explore how we can adapt data to
    meet our requirements. Also we'll see how to generate arbirtrary
    data for custom data types. You can read the documentation here
    https://hypothesis.readthedocs.io/en/latest/data.html#adapting-strategies
"""

import pytest
from hypothesis import given, strategies as st

# Exercise 1: Write a strategy that generates strings of length 3 every time.
# You can use the min_size param but you CAN'T use the max_size one.

# Your strategy here
def test_length():
    # Your assert(s) here
    pytest.skip()


# Exercise 2: Write a strategy that generates a ordered list of floats.

# Your strategy here
def test_ordered_list_of_floats():
    # Your assert(s) her
    pytest.skip()

# Exercise 3: Write a strategy that generates a tuple of ints.

# Your strategy here
def test_basic_tuple():
    # Your assert(s) here
    pytest.skip()


# Exercise 4: Write a tuple of ints where the second element is always
# greater than the first one.

# Your strategy here
def test_tuple_snd_is_greater():
    # Your assert(s) here
    pytest.skip()
