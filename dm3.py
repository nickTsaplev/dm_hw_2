def composition(a,b):
    n = len(a)
    
    c = [False] * n
    for i in range(n):
        c[i] = [False] * n
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if(a[i][k] and b[k][j]):
                    c[i][j] = True
    return c
    

def relUnion(a,b):
    n = len(a)
    
    c = [False] * n
    for i in range(n):
        c[i] = [False] * n
    
    for i in range(n):
        for j in range(n):
            c[i][j] = (a[i][j] or b[i][j])
    
    return c

n = int(input())

a = [0] * n
for i in range(n):
    a[i] = list(map(bool,map(int, (input().split()))))

prev = [0] * n
for i in range(n):
    prev[i] = [0] * n

ans = a
nextval = a
while(prev != ans):
    # print(nextval)
    prev = ans
    nextval = composition(nextval,a)  
    ans = relUnion(ans,nextval)
    
for i in range(n):
    for j in range(n):
        if(ans[i][j]):
            print(1, end = ' ')
        else:
            print(0, end = ' ')
    print()
