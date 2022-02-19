a = set()

for _ in range(10):
    i = int(input())
    a.add(i%42)
print(len(a))