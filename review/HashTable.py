# 1. 체이닝

class HashNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def _hash_function(self, key):
        return key % self.size

    def put(self, key, value):
        index = self._hash_function(key)  # 해시 함수로 인덱스 찾기
        if self.table[index] is None:  # 해당 인덱스가 비어 있다면
            self.table[index] = HashNode(key, value)  # 새 노드 삽입
        else:  # 충돌이 발생한 경우 (체이닝 방식)
            node = self.table[index]
            while node.next is not None:  # 마지막 노드까지 이동
                node = node.next
            node.next = HashNode(key, value)  # 연결 리스트로 추가

    def get(self, key):
        index = self._hash_function(key)  # 해시 함수로 인덱스 찾기
        node = self.table[index]
        while node is not None:  # 리스트를 순회하며 키를 찾음
            if node.key == key:
                return node.value
            node = node.next
        return -1  # 키가 없으면 -1 반환

    def remove(self, key):
        index = self._hash_function(key)  # 해시 함수로 인덱스 찾기
        node = self.table[index]
        prev_node = None  # 이전 노드 저장

        while node is not None:
            if node.key == key:  # 찾은 경우
                if prev_node is None:  # 첫 번째 노드라면
                    self.table[index] = node.next  # 다음 노드를 첫 번째로 변경
                else:
                    prev_node.next = node.next  # 이전 노드가 다음 노드를 가리키게 변경
                return
            prev_node = node
            node = node.next

# 2. 오픈 어드레싱

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def _hash_function(self, key):
        return key % self.size

    def put(self, key, value):
        index = self._hash_function(key)

        while self.table[index] is not None:  # 빈 자리 찾을 때까지 이동
            if self.table[index][0] == key:  # 같은 키가 있으면 업데이트
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size  # 선형 탐색 (다음 칸으로 이동)

        self.table[index] = (key, value)  # 빈 자리에 저장

    def get(self, key):
        index = self._hash_function(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size  # 선형 탐색으로 다음 칸 검사

        return -1  # 찾지 못한 경우

    def remove(self, key):
        index = self._hash_function(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None  # 삭제 (None으로 설정)
                return
            index = (index + 1) % self.size  # 선형 탐색으로 다음 칸 검사


# 1. 체이닝

class HashNode2:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class HashTable2:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def _hash_function(self, key):
        return key % self.size

    def put(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = HashNode2(key, value)
        else:
            node = self.table[index]
            while node.next is not None:
                node = node.next
            node.next = HashNode2(key, value)