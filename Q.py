A = input().split()
index = int(input())
print(*A[0:index], *A[index+1:len(A)])