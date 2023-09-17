S = input()
N = len(S)
result = 1
for i in range(N-1):
    if S[i] != S[i+1]:
        result += 1
print(result//2)