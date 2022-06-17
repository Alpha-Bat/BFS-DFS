N = int(input())
M = int(input())
A = []
B = []
while M > 0 :
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)
    M = M-1

stack = [1]    
check = []
ans1 = []
for i in range(N):
    check.append(0)
while len(stack) > 0 :
    now = stack.pop(0)
    if check[now-1] == 0 :
        ans1.append(now)
        check[now-1] = 1
    add = []
    for idx, a in enumerate(A):
        if a == now and check[B[idx]-1] == 0:
            add.append(B[idx])
            if B[idx] in stack:
                stack.remove(B[idx])
    for idx, b in enumerate(B):
        if b == now and check[A[idx]-1] == 0:
            add.append(A[idx])
            if A[idx] in stack:
                stack.remove(A[idx])
    add.sort()
    stack = add + stack
    
print(len(ans1)-1)
