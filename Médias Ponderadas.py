n=int(input())
for i in range(n):
    a,b,c=list(map(float,input().split()))
    total=(a*2+b*3+c*5)/10
    print("%0.1f"%total)


for _ in range(int(input())):
    x,b,c=map(float,input().split())
    d=((x/5.0)+((b*3.0)/10.0)+(c/2.0))
    print("%.1f"%d)