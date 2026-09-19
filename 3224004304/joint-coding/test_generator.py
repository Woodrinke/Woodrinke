from generator import generate_problems, write_files
from fraction import Fraction


def test_generate_count():
    problems = generate_problems(10, 10)
    assert len(problems) == 10


def test_no_duplicate_signature():
    problems = generate_problems(50, 10)
    sigs = [p.signature() for p in problems]
    assert len(sigs) == len(set(sigs))

def test_write_files(tmp_path):
    problems = generate_problems(5, 10)
    ex_path = tmp_path / "Exercises.txt"
    ans_path = tmp_path / "Answers.txt"
    write_files(problems, str(ex_path), str(ans_path))

    ex_lines = ex_path.read_text(encoding="utf-8").splitlines()
    ans_lines = ans_path.read_text(encoding="utf-8").splitlines()

    assert len(ex_lines) == 5
    assert len(ans_lines) == 5

    for i, line in enumerate(ex_lines, start=1):
        assert line.startswith(f"{i}. ")
        assert line.endswith(" = ")

    for i, (expr, ans) in enumerate(zip(problems, ans_lines), start=1):
        assert ans.startswith(f"{i}. ")
        assert ans == f"{i}. {expr.value()}"