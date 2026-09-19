import random
from fraction import Fraction
from expression import Expression, random_expression_tree


def test_leaf():
    e = Expression(value_node=Fraction(3, 1))
    assert e.is_leaf()
    assert e.value() == Fraction(3, 1)
    assert str(e) == "3"


def test_tree_value():
    left = Expression(value_node=Fraction(1, 2))
    right = Expression(value_node=Fraction(1, 3))
    e = Expression(left=left, op="+", right=right)
    assert e.value() == Fraction(5, 6)


def test_tree_str():
    left = Expression(value_node=Fraction(1, 2))
    right = Expression(value_node=Fraction(1, 3))
    e = Expression(left=left, op="+", right=right)
    assert str(e) == "1/2 + 1/3"


def test_random_tree_count():
    for _ in range(50):
        count = random.randint(0, 3)
        e = random_expression_tree(10, count)
        # 统计运算符个数
        def op_count(node):
            if node.is_leaf():
                return 0
            return 1 + op_count(node.left) + op_count(node.right)
        assert op_count(e) == count, f"运算符个数不对: {str(e)}"


def test_random_tree_sub_no_negative():
    for _ in range(100):
        e = random_expression_tree(10, 3)
        # 递归检查每个减法子表达式
        def check(node):
            if node.is_leaf():
                return
            if node.op == "-":
                assert node.left.value() >= node.right.value(), f"减法出负数: {str(node)}"
            check(node.left)
            check(node.right)
        check(e)


def test_random_tree_div_proper():
    for _ in range(100):
        e = random_expression_tree(10, 3)
        def check(node):
            if node.is_leaf():
                return
            if node.op == "÷":
                assert node.right.value() != Fraction(0, 1)
                assert node.value().is_proper(), f"除法结果不是真分数: {str(node)}"
            check(node.left)
            check(node.right)
        check(e)