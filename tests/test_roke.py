import hypothesis.strategies as st
from hypothesis import given
from roke.main import gen_identifiers


@given(st.integers(min_value=0, max_value=10000))
def test_count(count):
    pattern = ""
    result = gen_identifiers(pattern, count)
    assert len(result) == count
