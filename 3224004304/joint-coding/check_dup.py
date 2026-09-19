# check_dup.py
from parser import parse_expression_string
from grader import extract_expression

with open("Exercises.txt", encoding="utf-8") as f:
    lines = [l for l in f.read().splitlines() if l.strip()]

seen = set()
for i, line in enumerate(lines, start=1):
    expr_str = extract_expression(line)
    expr = parse_expression_string(expr_str)
    sig = expr.signature()
    if sig in seen:
        print(f"重复: 第 {i} 题 {expr_str}")
    seen.add(sig)

print(f"总题数: {len(lines)}, 唯一签名数: {len(seen)}")
