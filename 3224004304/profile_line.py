from line_profiler import LineProfiler
from main import calculate_similarity

t1 = "今天是星期天，天气晴朗，我打算晚上和朋友一起去看电影，然后吃顿好的。" * 50
t2 = "今天是周天，天气晴朗，我晚上要和朋友去看电影，然后吃顿好的。" * 50

lp = LineProfiler()
lp.add_function(calculate_similarity)   # 要分析这个函数
test_func = lp(calculate_similarity)    # 包装
test_func(t1, t2)                       # 执行
lp.print_stats()                        # 打印结果