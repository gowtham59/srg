a1=int(input())
a2r=list(map(int,input().split()))
sum=0
for x in range(1,a1):
    for y in range(x):
        if a2r[x]>a2r[y]:
            sum+=a2r[y]
print(sum)
