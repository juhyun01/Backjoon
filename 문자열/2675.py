t = int(input())
for _ in range(t):
    num, s = input().split()
    for i in s:
        print(i*int(num),end='')
    print()