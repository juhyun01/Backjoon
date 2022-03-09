N,M = map(int, input().split())
list = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if list[i]+list[j]+list[k] > M:
                continue
            else:
                result = max(result,list[i]+list[j]+list[k])
print(result)