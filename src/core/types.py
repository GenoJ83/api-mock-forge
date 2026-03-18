from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass, field
import time

@dataclass
class MockRequest:
    method: str
    path: str
    headers: Dict[str, str] = field(default_factory=dict)
    query_params: Dict[str, str] = field(default_factory=dict)
    body: Optional[Any] = None
    timestamp: float = field(default_factory=time.time)

@dataclass
class MockResponse:
    status_code: int = 200
    headers: Dict[str, str] = field(default_factory=dict)
    body: Optional[Any] = None
    latency_ms: float = 0.0
