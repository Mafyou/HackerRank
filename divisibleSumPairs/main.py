def divisibleSumPairs(n, k, ar):
    answer = 0
    for i in range(n):
        for j in range(i, n):
            if i == j: continue
            total = ar[i] + ar[j]
            if total % k == 0:
                answer += 1
    return answer

res = divisibleSumPairs(6, 3, [1,3,2,6,1,2])
print(res)