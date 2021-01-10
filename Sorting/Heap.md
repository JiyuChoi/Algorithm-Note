# 힙 (Heap)

- 완전 이진 트리를 기본으로한 자료 구조이며, 부모 노드와 자식 노드간의 대소관계가 성립하기 때문에 삽입 삭제 후 노드를 다시 정렬해주는 기능이 필요
- 트리 내의 최대 값이나 최소 값을 쉽게 찾고자하는 자료구조이므로 힙의 루트 노트는 힙 내의 데이터들 중 가장 큰 값이거나 가장 작은 값

## 📌 완전 이진 트리(Complete Binary Tree)

- 이진 트리의 노드를 생성할 때 트리의 왼쪽부터 차곡차곡 채워나가는 트리
- 마지막 레벨을 제외한 모든 레벨에는 노드가 꽉 차 있어야함

## 📌 완전 이진 트리와 힙의 차이

힙은 완전 이진트리를 기초로 하기 때문에 기본적인 노드의 삽입 및 삭제 알고리즘은 일반적인 완전 이진 트리와 동일

- 노드의 삽입은 반드시 배열의 끝에만 가능, 노드를 삭제하고 나면 빈 공간이 남지 않도록 노드를 당겨 빈공간을 채워줘야한다는 공통점 존재
- 그러나 힙은 부모와 자식 간의 대소관계가 성립되어야 한다는 조건이 있기 때문에, 삽입 삭제 후 노드를 다시 정렬해주어야 함

[설명출처](https://evan-moon.github.io/2019/10/12/introduction-data-structure-heap/)
<br/>
<br/>
# 파이썬 라이브러리 heapq

다익스트라 최단경로를 포함해 다양한 알고리즘에서 <b>'우선순위 큐'</b> 기능을 구현하고자 할때 사용

- 파이썬의 힙은 최소힙으로 구성
- 단순히 원소를 집어넣고 빼는 것만으로도 시간 복잡도 O(nlogn)의 오름차순 정렬
- 최소힙 자료구조의 최 상단 원소는 항상 '가장 작은' 원소

## 📌 힙 정렬(Heap sort) 구현 소스코드

파이썬 라이브러리에선 최대힙을 제공하지 않으므로 다음 주석과 같은 방법으로 <b>'내림차순 힙'</b> 정렬을 구현함

```python
# 최소 힙(Min Heap)
import heapq as hq

def heapsort(iterable):
	h = []
	result = []
	# 모든 원소를 차례대로 힙에 삽입	
	for value in iterable:
		hq.heappush(h, value)   # 최대힙의 경우 hq.heappush(h, -value)
	# 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
	for i in range(len(h)):
		result.append(hq.heappop(h))  # 최대힙의 경우 result.append(-hq.heappush(h))
	return result
```

### ✔️ 우선순위 큐를 이용하는 문제

- BOJ [카드 정렬하기](https://www.acmicpc.net/problem/1715)
- 프로그래머스 [더 맵게](https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3)
