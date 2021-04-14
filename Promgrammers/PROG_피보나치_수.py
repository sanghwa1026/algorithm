import sys

sys.setrecursionlimit(1000000)
global dp

def fibo(n):
    if n < 1:
        return 0
    elif dp[n] > 0:
        return dp[n]

    dp[n] = (fibo(n - 1) + fibo(n - 2)) % 1234567
    return dp[n]

def solution(n):
    global dp
    answer = 0
    dp = [0] * 100001
    dp[0], dp[1] = 0, 1

    answer = fibo(n)
    return answer