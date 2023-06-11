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


# Let's discover how to generate arbitrary data for our own data types.
# We have a `Person` class which holds an id(int) and the person's name (string).
# First let's write this as a dataclass.

# Your dataclass here

# Exercise 5: Write a strategy that lets you generate data of the Person type.
# Write your asserts too.
def test_person_generation():
    # Your assert(s) here
    pytest.skip()


# Sometimes you'd like to write your strategy once and reuse in different tests
# with some tweaks. https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.composite

# Exercise 6: Write a reusable strategy that late used in your test allows you to
# generate id greater than a 1000 and strings that contains at least 5 elements.

# Your reusable strategy here

@st.composite
def person_reusable_st(draw, id = None, name =  None):
    # Your code goes here
    ...

# Now write your strategy using the one above and make it satisfy the two conditions

# Your strategy here
def test_person_with_conditions():
    # Your assert(s) here
    pytest.skip()
