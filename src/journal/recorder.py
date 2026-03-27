from typing import List, Optional
from src.core.types import MockRequest

class RequestJournal:
    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.history: List[MockRequest] = []
        
    def record(self, request: MockRequest) -> None:
        if len(self.history) >= self.capacity:
            self.history.pop(0)
        self.history.append(request)
        
    def count(self, method: Optional[str] = None, path: Optional[str] = None) -> int:
        return len(self.filter(method=method, path=path))
        
    def filter(self, method: Optional[str] = None, path: Optional[str] = None) -> List[MockRequest]:
        res = self.history
        if method:
            res = [r for r in res if r.method.upper() == method.upper()]
        if path:
            res = [r for r in res if r.path == path]
        return res
        
    def clear(self) -> None:
        self.history.clear()
