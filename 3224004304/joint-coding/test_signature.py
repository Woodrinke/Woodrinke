from fraction import Fraction
from expression import Expression


def leaf(v):
    return Expression(value_node=v)


def node(left, op, right):
    return Expression(left=left, op=op, right=right)


def test_add_commutative():
    e1 = node(leaf(Fraction(23, 1)), "+", leaf(Fraction(45, 1)))
    e2 = node(leaf(Fraction(45, 1)), "+", leaf(Fraction(23, 1)))
    assert e1.signature() == e2.signature()


def test_mul_commutative():
    e1 = node(leaf(Fraction(6, 1)), "×", leaf(Fraction(8, 1)))
    e2 = node(leaf(Fraction(8, 1)), "×", leaf(Fraction(6, 1)))
    assert e1.signature() == e2.signature()


def test_sub_not_commutative():
    e1 = node(leaf(Fraction(5, 1)), "-", leaf(Fraction(3, 1)))
    e2 = node(leaf(Fraction(3, 1)), "-", leaf(Fraction(5, 1)))
    assert e1.signature() != e2.signature()


def test_div_not_commutative():
    e1 = node(leaf(Fraction(1, 1)), "÷", leaf(Fraction(2, 1)))
    e2 = node(leaf(Fraction(2, 1)), "÷", leaf(Fraction(1, 1)))
    assert e1.signature() != e2.signature()


def test_associative_reorder():
    e1 = node(leaf(Fraction(3, 1)), "+", node(leaf(Fraction(2, 1)), "+", leaf(Fraction(1, 1))))
    e2 = node(node(leaf(Fraction(1, 1)), "+", leaf(Fraction(2, 1))), "+", leaf(Fraction(3, 1)))
    assert e1.signature() == e2.signature()


def test_not_associative_reorder():
    e1 = node(node(leaf(Fraction(1, 1)), "+", leaf(Fraction(2, 1))), "+", leaf(Fraction(3, 1)))
    e2 = node(node(leaf(Fraction(3, 1)), "+", leaf(Fraction(2, 1))), "+", leaf(Fraction(1, 1)))
    assert e1.signature() != e2.signature()