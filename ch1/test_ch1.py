def test_simple_equality():
    assert 2 == 2


def test_is():
    assert 2 is 2  # small ints are preallocated


def test_in():
    assert 4 in range(5)


def test_not_in():
    assert 40 not in range(5)


def test_gt():
    assert 40 > 5


def test_lt():
    assert -40 < 5


def test_str_contains():
    assert "th" in "python"
