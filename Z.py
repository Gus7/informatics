A = input().split()
shift = int(input())
print(*A[len(A)-shift:len(A)], *A[0:shift-1])