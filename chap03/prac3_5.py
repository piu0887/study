from __future__ import annotations
from typing import Any, Type
import hashlib

class Node :
    """해시를 구성하는 노드"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """초기화"""
        self.key = key     # 키
        self.value = value # 값
        self.next = next   # 뒤쪽 노드를 참조
        pass

class ChainedHash:
    """체인법으로 해시 클래스 구현"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity       # 해시 테이블 크기를 지정
        self.table = [None] * self.capacity # 해시테이블(리스트)을 선언
        pass

    def hash_value(self, key: Any) ->int:
        """해시값을 구함"""
        
        if isinstance(key, int):
            return key % self.capacity    # 해시값을 찾음
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16)%self.capacity)