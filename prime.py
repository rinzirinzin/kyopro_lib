import math

#リストの最大公約数
def gcdl(list_g):
    ans = 0
    for i in range(len(list_g)):
        ans = math.gcd(ans,list_g[i])
    return ans

#素数判定
def prime_judge(N):
    for i in range(2, N + 1):
        if i * i > N:
            break
        if N % i == 0:
            return False
    return N != 1

#素数列挙
def erastos(N):
    prime = [True for i in range(N+1)]
    prime[0] = False #0 is not prime
    prime[1] = False #1 is not prime
    sqrt_n = math.ceil(math.sqrt(N)) #ceil ex 7.09 -> 8
    for i in range(2,sqrt_n):
        if prime[i]:
            for j in range(2*i,N+1,i):
                prime[j] = False
    return prime

#素因数分解
def prime_factorize(N):
    a = []
    while N % 2 == 0:
        a.append(2)
        N //= 2
    f = 3
    while f * f <= N:
        if N % f == 0:
            a.append(f)
            N //= f
        else:
            f += 2
    if N != 1:
        a.append(N)
    return a
