# parser.py
from fraction import Fraction
from expression import Expression


def tokenize(s):
    tokens = []
    i = 0
    n = len(s)
    while i < n:
        c = s[i]
        if c.isspace():
            i += 1
            continue
        if c in "+-×÷()":
            tokens.append(c)
            i += 1
            continue
        # 数字、分数、带分数
        start = i
        while i < n and (s[i].isdigit() or s[i] in "/’"):
            i += 1
        tokens.append(s[start:i])
    return tokens


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def next(self):
        tok = self.peek()
        self.pos += 1
        return tok

    def parse(self):
        expr = self.parse_expression()
        if self.pos != len(self.tokens):
            raise ValueError(f"解析未完成，剩余 token: {self.tokens[self.pos:]}")
        return expr

    def parse_expression(self):
        left = self.parse_term()
        while self.peek() in ("+", "-"):
            op = self.next()
            right = self.parse_term()
            left = Expression(left=left, op=op, right=right)
        return left

    def parse_term(self):
        left = self.parse_factor()
        while self.peek() in ("×", "÷"):
            op = self.next()
            right = self.parse_factor()
            left = Expression(left=left, op=op, right=right)
        return left

    def parse_factor(self):
        tok = self.peek()
        if tok is None:
            raise ValueError("表达式意外结束")
        if tok == "(":
            self.next()
            expr = self.parse_expression()
            if self.peek() != ")":
                raise ValueError("缺少右括号")
            self.next()
            return expr
        # 数字、分数、带分数
        self.next()
        return Expression(value_node=Fraction.from_string(tok))


def parse_expression_string(s):
    tokens = tokenize(s)
    return Parser(tokens).parse()