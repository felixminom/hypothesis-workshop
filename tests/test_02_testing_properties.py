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



# Our code goes here
def test():
    pass