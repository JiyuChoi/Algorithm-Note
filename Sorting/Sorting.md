# Sorting

## 📌 Selection sort
* '매번 가장 작은 것'을 선택한다<br>
* O(n^2)
```py
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  min_index = i  # 가장 작은 원소의 인덱스 
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[min_index], array[i] = array[i], array[min_index] # 스와프
```

## 📌 Insertion sort
* 특정한 데이터를 적절한 위치에 '삽입'한다<br>
* 데이터가 거의 정렬되어 있을 때 효율적<br>
* 선택 정렬에 비해 실행 시간 측면에서 더 효율적<br>
* O(n^2)
```py
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
  for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복함
    if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
      array[j], array[j-1] = array[j-1], array[j]
    else: # 자기보다 작은 값을 만나면 그 위치에서 멈춤
      break
```

## 📌 Quick sort
* '기준(피벗)'을 정하고 큰 수와 작은 수를 교환한 다음 반으로 나눈다.<br>
* 앞의 두 정렬보다 시간 측면에서 효울적<br>
* 재귀 함수 형태로 구현<br>
* O(nlogn)
```py
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
  # 리스트가 하나 이하의 원소만을 담고 있다면 종료
  if len(array) <= 1:
      return
  
  pivot = array[0]
  tail = array[1:]
  
  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]
  
  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)
```

## 📌 Count sort
* '별도의 리스트를 선언'하고 그 안에 정렬에 대한 정보를 담는다.<br>
* 데이터의 크기가 한정되어 있고, 값이 많이 중복되어 있을 때만 사용가능<br>
* O(N+K)

```py
array = [7,5,9,0,3,1,6,2,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0]*(max(array)+1)

for i in range(len(array)):
  count[array[i]] += 1
  
for i in range(len(count)):
  for j in range(count[i]):
      print(i, end=" ")
```

```
