A = int(input())
for i in range(A):
    Yonsei=0
    Korea=0
    for j in range(9):
        Y,K = map(int, input().split())
        Yonsei+=Y
        Korea+=K
    if Yonsei>Korea:
        print("Yonsei")
    elif Yonsei<Korea:
        print("Korea")
    else:
        print("Draw")