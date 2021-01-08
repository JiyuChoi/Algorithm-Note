# Merge Sort

## 📌 병합정렬 
[(그림 출처)](https://ko.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/overview-of-merge-sort)<br>
![screenshot_20171221-151714](https://cdn.kastatic.org/ka-perseus-images/ace963383bea8d154f6abd1322a06a73b56b4628.png)<br>
* 정렬할 데이터를 하나로 잘게 쪼갠 후(divide) 두 개의 값을 비교하여 정렬(conquer)하고 합치는(Merge) 알고리즘<br>
* 분할정복을 사용한 대표적인 알고리즘
* O(nlogn)

## 📌 병합정렬 알고리즘 구현 소스코드
[(소스코드 출처)](https://ordo.tistory.com/87)
```py
# 리스트 분리
def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2

    left = list[:mid]
    right = list[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


# 리스트 정렬하면서 병합
def merge(left, right):
    lt = 0
    rt = 0
    result = []
    
    while lt < len(left) and rt < len(right):
        if left[lt] < right[rt]:
            result.append(left[lt])
            lt += 1
        else:
            result.append(right[rt])
            rt += 1
                
     # 한 곳의 병합이 끝나면 나머지 남은 곳의 데이터 넣기
     while lt < len(left):
        result.append(left[lt])
        lt += 1
            
     while rt < len(right):
        result.append(right[rt])
        rt += 1
            
    return result

'''
list = [14, 7, 3, 12, 9, 11, 6, 2]
print(merge_sort(list))
'''
```
