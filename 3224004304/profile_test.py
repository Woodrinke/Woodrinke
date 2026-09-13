import cProfile
import pstats
from main import calculate_similarity

t1 = "今天是星期天，天气晴朗，我打算晚上和朋友一起去看电影，然后吃顿好的。" * 50
t2 = "今天是周天，天气晴朗，我晚上要和朋友去看电影，然后吃顿好的。" * 50

cProfile.run("calculate_similarity(t1, t2)", "profile_result")

p = pstats.Stats("profile_result")
p.sort_stats("cumulative").print_stats(10)