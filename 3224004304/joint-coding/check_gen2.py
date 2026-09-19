from generator import generate_problems

problems = generate_problems(10000, 10)
sigs = [p.signature() for p in problems]
print("题目数:", len(problems))
print("唯一签名数:", len(set(sigs)))

seen = {}
count = 0
for i, p in enumerate(problems, start=1):
    sig = p.signature()
    if sig in seen:
        count += 1
        if count <= 20:
            print(f"重复: 第 {i} 题 {p} 和 第 {seen[sig]} 题")
    else:
        seen[sig] = i

print("重复数:", count)