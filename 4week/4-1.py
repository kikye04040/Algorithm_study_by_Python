def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] # 피벗을 배열의 중간 요소로 선택
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_and_sort_arrays(arr1, arr2):
    merged_array = arr1 + arr2 # 두 배열 합치기
    sorted_array = quick_sort(merged_array) # 퀵 정렬을 사용하여 배열을 정렬
    return sorted_array

# 예시 실행
arr1 = [10, 5, 15]
arr2 = [4, 11, 2]
print(merge_and_sort_arrays(arr1, arr2))