# generator.py
import random
from expression import random_expression_tree


def generate_problems(n, r):
    seen = set()
    problems = []
    max_attempts = n * 100
    attempts = 0

    while len(problems) < n and attempts < max_attempts:
        attempts += 1
        count = random.randint(0, 3)
        expr = random_expression_tree(r, count)
        sig = expr.signature()
        if sig in seen:
            continue
        seen.add(sig)
        problems.append(expr)

    return problems


def write_files(problems, exercises_path="Exercises.txt", answers_path="Answers.txt"):
    with open(exercises_path, "w", encoding="utf-8") as fe, \
         open(answers_path, "w", encoding="utf-8") as fa:
        for i, expr in enumerate(problems, start=1):
            fe.write(f"{i}. {expr} = \n")
            fa.write(f"{i}. {expr.value()}\n")