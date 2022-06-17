N = int(input())
M = int(input())
A = []
B = []
while M > 0 :
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)
    M = M-1

queue = [1]
check = []
ans2 = []
for i in range(N):
    check.append(0)
while len(queue) > 0 :   
    now = queue.pop(0)
    if check[now-1] == 0 :
        ans2.append(now)
        check[now-1] = 1
    add = []
    for idx, a in enumerate(A):
        if a == now and check[B[idx]-1] == 0 and B[idx] not in queue:
            add.append(B[idx])
    for idx, b in enumerate(B):
        if b == now and check[A[idx]-1] == 0 and A[idx] not in queue:
            add.append(A[idx])
    add.sort()
    queue = queue+add
    
print(len(ans2)-1)
