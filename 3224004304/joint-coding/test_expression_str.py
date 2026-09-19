from fraction import Fraction
from expression import Expression


def leaf(v):
    return Expression(value_node=v)


def node(left, op, right):
    return Expression(left=left, op=op, right=right)


def test_no_extra_parens():
    e = node(leaf(Fraction(1, 2)), "+", leaf(Fraction(1, 3)))
    assert str(e) == "1/2 + 1/3"


def test_mul_add_parens():
    # (1/2 + 1/3) × 2
    e = node(node(leaf(Fraction(1, 2)), "+", leaf(Fraction(1, 3))), "×", leaf(Fraction(2, 1)))
    assert str(e) == "(1/2 + 1/3) × 2"


def test_add_mul_no_parens():
    # 1/2 + 1/3 × 2
    e = node(leaf(Fraction(1, 2)), "+", node(leaf(Fraction(1, 3)), "×", leaf(Fraction(2, 1))))
    assert str(e) == "1/2 + 1/3 × 2"


def test_sub_right_sub_parens():
    # 5 - (3 - 1)
    e = node(leaf(Fraction(5, 1)), "-", node(leaf(Fraction(3, 1)), "-", leaf(Fraction(1, 1))))
    assert str(e) == "5 - (3 - 1)"


def test_div_right_mul_parens():
    # 1 ÷ (2 × 3)
    e = node(leaf(Fraction(1, 1)), "÷", node(leaf(Fraction(2, 1)), "×", leaf(Fraction(3, 1))))
    assert str(e) == "1 ÷ (2 × 3)"


def test_div_right_div_parens():
    # 1 ÷ (2 ÷ 3)
    e = node(leaf(Fraction(1, 1)), "÷", node(leaf(Fraction(2, 1)), "÷", leaf(Fraction(3, 1))))
    assert str(e) == "1 ÷ (2 ÷ 3)"


def test_sub_right_add_parens():
    # 5 - (3 + 1)
    e = node(leaf(Fraction(5, 1)), "-", node(leaf(Fraction(3, 1)), "+", leaf(Fraction(1, 1))))
    assert str(e) == "5 - (3 + 1)"


def test_left_sub_no_parens():
    # (5 - 3) + 1，左边同优先级不用加括号
    e = node(node(leaf(Fraction(5, 1)), "-", leaf(Fraction(3, 1))), "+", leaf(Fraction(1, 1)))
    assert str(e) == "5 - 3 + 1"