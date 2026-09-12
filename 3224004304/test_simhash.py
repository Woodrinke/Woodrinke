import pytest
from main import (
    clean_text,
    get_simhash,
    hamming_distance,
    calculate_similarity,
    read_text_file,
)


# ==================== 1. clean_text ====================

def test_clean_text_normal():
    """正常句子，含标点、数字、英文，应只保留中文"""
    assert clean_text("今天是星期天，天气晴！123abc") == "今天是星期天天气晴"


def test_clean_text_pure_symbol():
    """纯标点符号，清洗后应为空"""
    assert clean_text("!!!$$$   ,,") == ""


def test_clean_text_empty():
    """空字符串，清洗后仍为空"""
    assert clean_text("") == ""


# ==================== 2. get_simhash ====================

def test_get_simhash_same_text():
    """相同文本，指纹必须一致"""
    assert get_simhash("今天是星期天天气晴") == get_simhash("今天是星期天天气晴")


def test_get_simhash_diff_text():
    """不同文本，指纹应该不同"""
    assert get_simhash("今天是星期天天气晴") != get_simhash("苹果香蕉梨子很好吃")


def test_get_simhash_empty():
    """空文本，返回 0"""
    assert get_simhash("") == 0


# ==================== 3. hamming_distance ====================

def test_hamming_same():
    """相同指纹，距离为 0"""
    assert hamming_distance(123, 123) == 0


def test_hamming_opposite():
    """完全相反的 64 位指纹，距离为 64"""
    full_one = (1 << 64) - 1
    assert hamming_distance(0, full_one) == 64


# ==================== 4. calculate_similarity ====================

def test_sim_identical():
    """完全相同文本，相似度为 1.0"""
    t = "今天是星期天，天气晴，今天晚上我要去看电影。"
    assert calculate_similarity(t, t) == 1.0


def test_sim_empty_one_side():
    """一边为空，相似度为 0.0"""
    t = "今天是星期天，天气晴，今天晚上我要去看电影。"
    assert calculate_similarity(t, "") == 0.0


def test_sim_unrelated_less_than_related():
    """无关文本的相似度，应低于相关文本"""
    t1 = "今天是星期天，天气晴朗，我打算晚上和朋友一起去看电影，然后吃顿好的。"
    t2 = "苹果香蕉梨子橘子都是水果，富含维生素，多吃对身体有好处，尤其是夏天。"
    t3 = "今天是周天，天气晴朗，我晚上要和朋友去看电影，然后吃顿好的。"

    res_unrelated = calculate_similarity(t1, t2)
    res_related = calculate_similarity(t1, t3)

    assert res_unrelated < res_related


def test_sim_sample():
    """作业样例：原文与改写句，相似度应在合理范围"""
    t1 = "今天是星期天，天气晴，今天晚上我要去看电影。"
    t2 = "今天是周天，天气晴朗，我晚上要去看电影。"
    res = calculate_similarity(t1, t2)
    assert 0.5 < res < 1.0


# ==================== 5. read_text_file 异常测试 ====================

def test_read_file_not_exist():
    """文件不存在，应退出程序"""
    with pytest.raises(SystemExit):
        read_text_file("这个文件肯定不存在_12345.txt")


def test_read_path_is_dir(tmp_path):
    """传进来是目录，应退出程序"""
    with pytest.raises(SystemExit):
        read_text_file(str(tmp_path))