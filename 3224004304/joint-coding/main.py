import argparse
import sys

from generator import generate_problems, write_files
from grader import grade


def build_parser():
    parser = argparse.ArgumentParser(
        description="小学四则运算题目生成与批改程序",
        add_help=True,
    )
    parser.add_argument("-n", type=int, default=10, help="生成题目的个数")
    parser.add_argument("-r", type=int, default=None, help="题目中数值的范围")
    parser.add_argument("-e", type=str, default=None, help="题目文件路径")
    parser.add_argument("-a", type=str, default=None, help="答案文件路径")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    # 批改模式
    if args.e is not None or args.a is not None:
        if args.e is None or args.a is None:
            parser.print_help()
            sys.exit(1)
        grade(args.e, args.a)
        print("批改完成，结果写入 Grade.txt")
        return

    # 生成模式
    if args.r is None:
        parser.print_help()
        sys.exit(1)

    if args.r < 1:
        print("错误：-r 必须是自然数")
        sys.exit(1)

    if args.n < 1:
        print("错误：-n 必须是自然数")
        sys.exit(1)

    problems = generate_problems(args.n, args.r)
    if len(problems) < args.n:
        print(f"警告：只生成了 {len(problems)} 道不重复题目")
    write_files(problems)
    print(f"已生成 {len(problems)} 道题目")


if __name__ == "__main__":
    main()