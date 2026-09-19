# expression.py
from fraction import Fraction, random_fraction
import random


class Expression:
    def __init__(self, left=None, op=None, right=None, value_node=None):
        self.left = left
        self.op = op
        self.right = right
        self.value_node = value_node

    def is_leaf(self):
        return self.value_node is not None

    def value(self):
        if self.is_leaf():
            return self.value_node
        if self.op == "+":
            return self.left.value() + self.right.value()
        if self.op == "-":
            return self.left.value() - self.right.value()
        if self.op == "×":
            return self.left.value() * self.right.value()
        if self.op == "÷":
            return self.left.value() / self.right.value()
        raise ValueError(f"未知运算符: {self.op}")

    def __str__(self):
        return self._to_string()

    def _to_string(self, parent_op=None, is_right=False):
        if self.is_leaf():
            return str(self.value_node)

        my_op = self.op
        left_str = self.left._to_string(my_op, False)
        right_str = self.right._to_string(my_op, True)

        s = f"{left_str} {my_op} {right_str}"

        if parent_op is not None and self._need_parens(parent_op, is_right):
            s = f"({s})"

        return s

    def _need_parens(self, parent_op, is_right):
        my_op = self.op
        my_pri = priority(my_op)
        parent_pri = priority(parent_op)

        if my_pri < parent_pri:
            return True

        if my_pri == parent_pri and is_right:
            if parent_op == "-" and my_op in ("+", "-"):
                return True
            if parent_op == "÷" and my_op in ("×", "÷"):
                return True

        return False

    def signature(self):
        if self.is_leaf():
            return f"V{self.value_node}"

        left_sig = self.left.signature()
        right_sig = self.right.signature()

        if self.op in ("+", "×"):
            if left_sig > right_sig:
                left_sig, right_sig = right_sig, left_sig
            return f"{self.op}({left_sig},{right_sig})"

        return f"{self.op}({left_sig},{right_sig})"


def priority(op):
    if op in ("+", "-"):
        return 1
    if op in ("×", "÷"):
        return 2
    return 0


def random_expression_tree(r, count):
    if count == 0:
        return Expression(value_node=random_fraction(r))

    op = random.choice(["+", "-", "×", "÷"])

    left_count = random.randint(0, count - 1)
    right_count = count - 1 - left_count

    for _ in range(20):
        left = random_expression_tree(r, left_count)
        right = random_expression_tree(r, right_count)

        if op == "+" or op == "×":
            return Expression(left=left, op=op, right=right)

        if op == "-":
            if left.value() >= right.value():
                return Expression(left=left, op=op, right=right)
            else:
                return Expression(left=right, op=op, right=left)

        if op == "÷":
            if right.value() == Fraction(0, 1):
                continue
            result = left.value() / right.value()
            if result.is_proper():
                return Expression(left=left, op=op, right=right)
            if left.value() != Fraction(0, 1):
                result2 = right.value() / left.value()
                if result2.is_proper():
                    return Expression(left=right, op=op, right=left)

    return Expression(value_node=random_fraction(r))