# Counter
### collections 모듈의 Counter 클래스
```py
from collections import Counter
```
### 파이썬의 기본 자료형인 dictionary를 확장하고 있음
```py
Counter('hello world')
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```
### most_common
* 입력된 값으 요소들 중 빈도수가 높은 순으로 반환
* 리스트 안의 튜플 형태로 반환
```py
Counter('hello world').most_common(2)
# [('l', 3), ('o', 2)]
```

### Counter를 이용한 연산
* 덧셈(+), 뺄셈(-), 교집합(&), 합집합(|) 가능
* 딕셔너리 형태로 반환
```py
a = Counter('aabbccdd')
b = Counter('abbbce')

print(a-b)

# Counter({'d': 2, 'c': 1, 'b': 1, 'a': 1})
```
