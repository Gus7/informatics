A = input().split()
nomer, element = map(int, input().split())
print(*A[0:nomer], element, *A[nomer:len(A)])