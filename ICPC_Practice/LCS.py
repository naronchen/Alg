def LCS(s1,s2):
    w, h = len(s1)+1, len(s2)+1
    dp = [[0 for x in range(h)] for y in range(w)]
    Ans = 0
    for i in range(1, w):
        for j in range(1, h):
            if (s1[i-1] == s2[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
                Ans = max(dp[i][j], Ans)
    return Ans


N = int(input())
strlst = []
for i in range(N):
    strlst.append(input())

Ans = 0
for i in range(len(strlst)):
    for j in strlst[i+1:]:
        Ans = max(LCS(strlst[i],j), Ans)

print(Ans)
