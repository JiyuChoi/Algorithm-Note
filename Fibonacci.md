## 피보나치 수열을 해결하는 방법 3가지 [Link](https://shoark7.github.io/programming/algorithm/피보나치-알고리즘을-해결하는-5가지-방법)

#### 1) 재귀함수을 이용한 풀이: O(2^n)
```py
def fibo(n):
    return fibo(n-1) + fibo(n-2) if n >= 2 else n
```

####  2) 반복문을 이용한 풀이: O(n)
```py
def fibo(n):
    if n < 2:
        return n

    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b

    return b
```

####  3) 동적 계획법을 이용한 풀이(반복문): O(n)
```py
def fibo(n):
    if n < 2:
        return n

    f = [0 for _ in range(n+1)]
    f[1] = 1

    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]

    return f[n]
```
