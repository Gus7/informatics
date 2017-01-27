A = input().split()
B = A[1::2]
A[1::2] = A[: int((len(A)+1)/2 - 0.5)*2 - 1 :2]
A[: int((len(A)+1)/2 - 0.5)*2 - 1 :2] = B
print(*A)