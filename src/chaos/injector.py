import random
from typing import Optional
from src.core.types import MockResponse

class ChaosInjector:
    def __init__(self, error_rate: float = 0.0, seed: int = 42):
        self.error_rate = error_rate
        self.rng = random.Random(seed)
        
    def maybe_inject(self, normal_response: MockResponse) -> MockResponse:
        if self.error_rate > 0.0 and self.rng.random() < self.error_rate:
            fault_code = self.rng.choice([500, 503, 504])
            return MockResponse(status_code=fault_code, body={"chaos": "Fault injected", "status": fault_code})
        return normal_response
