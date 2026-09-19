# grader.py
from parser import parse_expression_string
from fraction import Fraction


def extract_expression(line):
    # 去掉 "1. " 前缀和 " = " 后缀
    line = line.strip()
    if ". " in line:
        line = line.split(". ", 1)[1]
    if line.endswith("="):
        line = line[:-1]
    return line.strip()


def extract_answer(line):
    line = line.strip()
    if ". " in line:
        line = line.split(". ", 1)[1]
    return line.strip()


def grade(exercises_path, answers_path, output_path="Grade.txt"):
    with open(exercises_path, "r", encoding="utf-8") as f:
        ex_lines = [l for l in f.read().splitlines() if l.strip()]
    with open(answers_path, "r", encoding="utf-8") as f:
        ans_lines = [l for l in f.read().splitlines() if l.strip()]

    correct = []
    wrong = []

    for i, (ex_line, ans_line) in enumerate(zip(ex_lines, ans_lines), start=1):
        expr_str = extract_expression(ex_line)
        user_ans_str = extract_answer(ans_line)

        try:
            expr = parse_expression_string(expr_str)
            std = expr.value()
        except Exception as e:
            wrong.append(i)
            continue

        try:
            user = Fraction.from_string(user_ans_str)
        except Exception:
            wrong.append(i)
            continue

        if std == user:
            correct.append(i)
        else:
            wrong.append(i)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"Correct: {len(correct)} ({', '.join(map(str, correct))})\n")
        f.write(f"Wrong: {len(wrong)} ({', '.join(map(str, wrong))})\n")