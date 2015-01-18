from perlin import ease
import pytest
import sys


@pytest.mark.randomize(a=int, b=int, ncalls=50)
def test_ease_produces_normalised_output(a, b):
    start = min(a, b) / (sys.maxint * 2.0)
    stop = max(a, b) / (sys.maxint * 2.0)
    result = ease(start, stop)
    assert result >= 0
    assert result <= 1


@pytest.mark.randomize(a=int, b=int, ncalls=50)
def test_ease_emphasizes_edges(a, b):
    start = min(a, b) / (sys.maxint * 2.0)
    stop = max(a, b) / (sys.maxint * 2.0)
    result = ease(start, stop)
    gap = stop - start
    if gap > 0 and gap < 0.5:
        assert result > 0
        assert result < gap
    elif gap > 0.5 and gap < 1:
        assert result < 1
        assert result > gap
    else:
        assert result == gap
