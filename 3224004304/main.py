import hashlib
import sys
import re
import jieba

# 简易中文停用词表
STOP_WORDS = {"的", "了", "是", "我", "在", "和", "就", "都", "而", "及", "与", "之", "也"}


def clean_text(raw_text: str) -> str:
    """文本清洗：只保留中文字符，去除数字、英文、标点、空白"""
    # 正则只匹配中文汉字
    chinese_only = re.sub(r"[^\u4e00-\u9fff]", "", raw_text)
    return chinese_only.strip()

def stable_hash(word: str) -> int:
    """
    稳定的字符串哈希函数。
    用 md5 代替内置 hash()，保证跨进程、跨机器结果一致。
    """
    return int(hashlib.md5(word.encode("utf-8")).hexdigest(), 16)

def get_simhash(cleaned_text: str) -> int:
    """生成64位simhash指纹，输入清洗后的中文文本，返回64位整数指纹"""
    if not cleaned_text:
        return 0

    words = jieba.lcut(cleaned_text)
    # 过滤停用词
    words = [w for w in words if w not in STOP_WORDS]

    # 初始化64位权重数组
    v = [0] * 64
    for word in words:
        h = stable_hash(word)
        for i in range(64):
            bit = (h >> i) & 1
            if bit == 1:
                v[i] += 1
            else:
                v[i] -= 1

    fingerprint = 0
    for i in range(64):
        if v[i] > 0:
            fingerprint |= (1 << i)
    return fingerprint


def hamming_distance(hash1: int, hash2: int) -> int:
    """计算两个64位指纹的海明距离，返回不同bit数量 0~64"""
    xor = hash1 ^ hash2
    return bin(xor).count("1")


def calculate_similarity(text1: str, text2: str) -> float:
    """
    对外统一算法入口
    输入两段原始文本字符串，返回0~1相似度
    """
    c1 = clean_text(text1)
    c2 = clean_text(text2)
    if not c1 or not c2:
        return 0.0

    f1 = get_simhash(c1)
    f2 = get_simhash(c2)
    dist = hamming_distance(f1, f2)
    similarity = (64 - dist) / 64
    return similarity


def read_text_file(path: str) -> str:
    """
    读取指定路径的文本文件，返回文件内容。
    读取失败时打印错误信息并退出程序。
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"错误：文件不存在 {path}")
    except UnicodeDecodeError:
        print(f"错误：文件编码不是utf-8 {path}")
    except PermissionError:
        print(f"错误：无读取权限 {path}")
    sys.exit(1)


def main():
    # 命令行参数校验
    if len(sys.argv) != 4:
        print("用法：python main.py 原文路径 抄袭文本路径 输出文件路径")
        sys.exit(1)

    orig_path, add_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]

    # 读取两个输入文件
    text_orig = read_text_file(orig_path)
    text_add = read_text_file(add_path)

    # 计算相似度
    sim = calculate_similarity(text_orig, text_add)
    result_val = round(sim * 100, 2)

    # 写入输出文件
    try:
        with open(out_path, "w", encoding="utf-8") as f_out:
            f_out.write(f"{result_val:.2f}")
    except PermissionError:
        print(f"错误：无写入权限 {out_path}")
        sys.exit(1)


if __name__ == "__main__":
    main()