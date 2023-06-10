import pytest
from hypothesis import given, strategies as st


# Example 1: Run this test
# Closure property: States that when we add two natural numbers,
# we always get a natural number. The same is true for whole
# numbers, integers, fractions, and decimals.

@given(
    st.one_of(
      st.lists(st.integers(), min_size=2, max_size=2),
      st.lists(st.floats(allow_nan=False), min_size=2, max_size=2),
      st.lists(st.fractions(), min_size=2, max_size=2)
    )
)
def test_sum_closure_property(list):
    n1 = list[0]
    n2 = list[1]
    cls = type(n1)
    # print(cls)
    assert isinstance(n1, cls)
    assert isinstance(n2, cls)
    assert isinstance(n1 + n2, cls)


# Example 2: Let's write a test for this property together.
# Commutative property: When we add two or more numbers, their sum is
# the same regardless of the order of the addends. We can write
# this property in the form of A + B = B + A.

# Our strategy goes here
def test_sum_commutative_property():
    # Our code goes here
    pytest.skip()


# Example 3: Let's write a test for the associative property.
# Associative property: When we add three or more numbers, the sum
# is the same regardless of the grouping of the addends. It also
# means that when we add three different numbers, the result is
# not affected by the addition pattern followed.

# Your strategy goes here
def test_sum_associative_property():
    # Our code goes here
    pytest.skip()

# Bonus 1: rewrite the test above using the permutations strategy
# (https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.permutations)


# Example 4: Let's write a test for the additive Identity together.
# Additive Identity property: On adding zero to any number, the sum
# remains the original number. Adding 0 to a number does not change
# the value of the number. It is true for natural numbers, whole
# numbers, fractions, integers, and decimals.

# Your strategy goes here
def test_sum_identity_property():
    # Our code goes here
    pytest.skip()


# You don't need to solve this right now.
# We'll come back later today.

# Example 5: Let's write a test for the following property.
# Additive inversive property: Additive inverse of a number x is the number that,
# when added to x, yields zero. So, the additive inverse of a number x is –x.
# Therefore, we can say that the additive inverse of a number is equal but
# opposite in sign to it.
# Caveat: is not valid to do the inverse within the test, let's do it at the
# strategy level
# Tip: you can check how to adapt a strategy (https://hypothesis.readthedocs.io/en/latest/data.html#adapting-strategies)

# Your strategy goes here
def test_sum_additive_inverse_property():
    # Our code goes here
    pytest.skip()