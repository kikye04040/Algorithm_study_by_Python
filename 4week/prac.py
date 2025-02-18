# 버블 정렬

def bubblesort(lst):
    # 최댓값을 구하는 알고리즘을 len(lst) - 1 만큼 반복한다.
    iters = len(lst) - 1
    for iter in range(iters):
        # 이미 구한 최댓값은 범위에서 제외한다.
        wall = iters - iter
        for cur in range(wall):
            if lst[cur] > lst[cur + 1]:
                lst[cur], lst[cur + 1] = lst[cur + 1], lst[cur]
    return lst


# 선택 정렬

def selectionsort(lst):
    iters = len(lst) - 1
    for iter in range(iters):
        minimun = iter
        for cur in range(iter + 1, len(lst)):
            if lst[cur] < lst[minimun]:
                minimun = cur

        if minimun != iter:
            lst[minimun], lst[iter] = lst[iter], lst[minimun]

    return lst


# 삽입 정렬

def insertionsort(lst):
    # 0번째 요소는 이미 정렬되어있으니, 1번째 ~ lst(len)-1 번째를 정렬하면 된다.
    for cur in range(1, len(lst)):
        # 비교지점이 cur-1 ~ 0(=cur-cur)까지 내려간다.
        for delta in range(1, cur + 1):
            cmp = cur - delta
            if lst[cmp] > lst[cmp + 1]:
                lst[cmp], lst[cmp + 1] = lst[cmp + 1], lst[cmp]
            else:
                break
    return lst


# 퀵 정렬

def quicksort(lst, start, end):
    def partition(part, ps, pe):
        pivot = part[pe]
        i = ps - 1
        for j in range(ps, pe):
            if part[j] <= pivot:
                i += 1
                part[i], part[j] = part[j], part[i]

        part[i + 1], part[pe] = part[pe], part[i + 1]
        return i + 1

    if start >= end:
        return None

    p = partition(lst, start, end)
    quicksort(lst, start, p - 1)
    quicksort(lst, p + 1, end)
    return lst


# 합병 정렬

def merge(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result

def mergesort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    L = lst[:mid]
    R = lst[mid:]
    return merge(mergesort(L), mergesort(R))


# 힙 정렬

class BinaryMinHeap:
    def __init__(self):
        # 계산 편의를 위해 0이 아닌 1번째 인덱스부터 사용한다.
        self.items = [None]

    def __len__(self):
        # len() 연산을 가능하게 하는 매직 메서드 덮어쓰기(Override).
        return len(self.items) - 1

    def _percolate_up(self):
        # percolate: 스며들다.
        cur = len(self)
        # left 라면 2*cur, right 라면 2*cur + 1 이므로 parent 는 항상 cur // 2
        parent = cur // 2

        while parent > 0:
            if self.items[cur] < self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        smallest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != cur:
            self.items[cur], self.items[smallest] = self.items[smallest], self.items[cur]
            self._percolate_down(smallest)

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root


def heapsort(lst):
    minheap = BinaryMinHeap()
    for elem in lst:
        minheap.insert(elem)

    return [minheap.extract() for _ in range(len(lst))]