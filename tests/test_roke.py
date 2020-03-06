from pathlib import Path

import hypothesis.strategies as st
from hypothesis import given
from roke.main import gen_identifiers, get_dict_list


@given(st.integers(min_value=0, max_value=10000))
def test_count(count):
    pattern = ""
    result = gen_identifiers(pattern, count)
    assert len(result) == count


def test_get_dict_list(monkeypatch):
    monkeypatch.setattr(Path, "is_dir", lambda *a: True)
    monkeypatch.setattr(Path, "glob", lambda p, _: [p / "1.txt", p / "2.txt"])
    result = get_dict_list()
    # Results are 2 things per place, there are 3 places
    assert len(result) == 6
    # Results are all distinct
    assert len(set(result)) == 6
