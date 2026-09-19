# test_random.py
from fraction import Fraction, random_fraction

def test_random_fraction():
    for _ in range(20):
        f = random_fraction(10)
        value = f.numerator / f.denominator
        assert 0 <= value < 10, f"越界: {f}"
        assert f.denominator > 0

    for _ in range(10):
        assert random_fraction(1) == Fraction(0, 1)

    for _ in range(10):
        f = random_fraction(2)
        assert f == Fraction(0, 1) or f == Fraction(1, 1)
