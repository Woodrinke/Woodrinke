from fraction import Fraction

def test_reduce():
    # 约分测试
    assert Fraction(2, 4) == Fraction(1, 2)
    assert Fraction(0, 5) == Fraction(0, 1)
    assert Fraction(3, -6) == Fraction(-1, 2)

def test_calc():
    # 四则运算
    assert Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)
    assert Fraction(1, 2) - Fraction(1, 3) == Fraction(1, 6)
    assert Fraction(1, 2) * Fraction(1, 3) == Fraction(1, 6)
    assert Fraction(1, 2) / Fraction(1, 3) == Fraction(3, 2)

def test_compare():
    # 比较
    assert Fraction(1, 2) < Fraction(2, 3)
    assert Fraction(3, 2) > Fraction(1, 1)
    assert Fraction(1, 2) == Fraction(2, 4)

def test_proper():
    # 真分数
    assert Fraction(1, 2).is_proper()
    assert not Fraction(3, 2).is_proper()
    assert Fraction(0, 1).is_proper()

def test_str():
    # 字符串转换
    assert str(Fraction(3, 1)) == "3"
    assert str(Fraction(1, 2)) == "1/2"
    assert str(Fraction(3, 2)) == "1’1/2"

def test_from_string():
    # 字符串解析
    assert Fraction.from_string("3") == Fraction(3, 1)
    assert Fraction.from_string("1/2") == Fraction(1, 2)
    assert Fraction.from_string("1’1/2") == Fraction(3, 2)

