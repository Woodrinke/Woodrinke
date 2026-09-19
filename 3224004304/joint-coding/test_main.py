import subprocess
import sys
from pathlib import Path



def run_main(args, cwd=None):
    return subprocess.run(
        [sys.executable, "main.py"] + args,
        capture_output=True,
        text=True,
        cwd=cwd,
    )

def test_missing_r():
    result = run_main(["-n", "5"])
    assert result.returncode != 0
    output = (result.stdout + result.stderr).lower()
    assert "usage" in output

def test_generate_basic(tmp_path):
    # 把项目文件复制到 tmp_path 才能跑，或者直接在项目目录跑
    result = run_main(["-n", "5", "-r", "10"])
    assert result.returncode == 0

    ex = Path("Exercises.txt")
    ans = Path("Answers.txt")
    assert ex.exists()
    assert ans.exists()

    ex_lines = ex.read_text(encoding="utf-8").splitlines()
    ans_lines = ans.read_text(encoding="utf-8").splitlines()
    assert len(ex_lines) == 5
    assert len(ans_lines) == 5


def test_invalid_r():
    result = run_main(["-n", "5", "-r", "0"])
    assert result.returncode != 0