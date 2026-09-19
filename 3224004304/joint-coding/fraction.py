# fraction.py
import math
import random


class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("分母不能为 0")
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        g = math.gcd(abs(numerator), denominator)
        self.numerator = numerator // g
        self.denominator = denominator // g

    def __add__(self, other):
        n = self.numerator * other.denominator + other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(n, d)

    def __sub__(self, other):
        n = self.numerator * other.denominator - other.numerator * self.denominator
        d = self.denominator * other.denominator
        return Fraction(n, d)

    def __mul__(self, other):
        n = self.numerator * other.numerator
        d = self.denominator * other.denominator
        return Fraction(n, d)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("除数不能为 0")
        n = self.numerator * other.denominator
        d = self.denominator * other.numerator
        return Fraction(n, d)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def is_proper(self):
        return 0 <= self.numerator < self.denominator

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        if abs(self.numerator) < self.denominator:
            return f"{self.numerator}/{self.denominator}"
        sign = "-" if self.numerator < 0 else ""
        n = abs(self.numerator)
        integer = n // self.denominator
        remainder = n % self.denominator
        if remainder == 0:
            return f"{sign}{integer}"
        return f"{sign}{integer}’{remainder}/{self.denominator}"

    @classmethod
    def from_string(cls, s):
        s = s.strip()
        if "’" in s:
            integer_part, frac_part = s.split("’")
            n, d = frac_part.split("/")
            integer = int(integer_part)
            sign = -1 if integer < 0 else 1
            integer = abs(integer)
            numerator = sign * (integer * int(d) + int(n))
            return cls(numerator, int(d))
        if "/" in s:
            n, d = s.split("/")
            return cls(int(n), int(d))
        return cls(int(s))

def random_fraction(r):
    if r <= 1:
        return Fraction(0, 1)

    # 随机决定：自然数 还是 真分数
    if random.random() < 0.5:
        # 自然数：0 到 r-1
        n = random.randint(0, r - 1)
        return Fraction(n, 1)
    else:
        # 真分数：分母 2 到 r-1，分子 1 到 分母-1
        if r <= 2:
            # 没有真分数可生成，退回自然数
            n = random.randint(0, r - 1)
            return Fraction(n, 1)
        d = random.randint(2, r - 1)
        n = random.randint(1, d - 1)
        return Fraction(n, d)