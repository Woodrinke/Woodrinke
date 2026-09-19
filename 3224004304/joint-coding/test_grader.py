import random
from generator import generate_problems, write_files
from grader import grade


def test_grade_with_wrong_answers(tmp_path):
    problems = generate_problems(5, 10)

    ex_path = tmp_path / "Exercises.txt"
    ans_path = tmp_path / "Answers.txt"
    write_files(problems, str(ex_path), str(ans_path))

    # 读标准答案，把第 2、4 题改错
    std_ans = ans_path.read_text(encoding="utf-8").splitlines()
    student_ans = []
    for i, line in enumerate(std_ans, start=1):
        if i in (2, 4):
            # 故意改成一个明显不同的答案
            student_ans.append(f"{i}. 999")
        else:
            student_ans.append(line)

    student_path = tmp_path / "StudentAnswers.txt"
    student_path.write_text("\n".join(student_ans) + "\n", encoding="utf-8")

    grade_path = tmp_path / "Grade.txt"
    grade(str(ex_path), str(student_path), str(grade_path))

    content = grade_path.read_text(encoding="utf-8")
    assert "Correct: 3 (1, 3, 5)" in content
    assert "Wrong: 2 (2, 4)" in content


def test_grade_all_correct(tmp_path):
    problems = generate_problems(5, 10)

    ex_path = tmp_path / "Exercises.txt"
    ans_path = tmp_path / "Answers.txt"
    write_files(problems, str(ex_path), str(ans_path))

    grade_path = tmp_path / "Grade.txt"
    grade(str(ex_path), str(ans_path), str(grade_path))

    content = grade_path.read_text(encoding="utf-8")
    assert "Correct: 5 (1, 2, 3, 4, 5)" in content
    assert "Wrong: 0 ()" in content