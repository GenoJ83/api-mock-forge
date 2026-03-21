import random
from typing import Optional

class LatencySimulator:
    """Calculates artificial latency based on configured distribution."""
    
    def __init__(self, mode: str = "fixed", base_ms: float = 0.0, jitter_ms: float = 0.0, seed: int = 42):
        self.mode = mode
        self.base_ms = base_ms
        self.jitter_ms = jitter_ms
        self.rng = random.Random(seed)
        
    def compute_delay_ms(self) -> float:
        if self.mode == "fixed":
            return max(0.0, self.base_ms)
        elif self.mode == "jitter":
            delta = self.rng.uniform(-self.jitter_ms, self.jitter_ms)
            return max(0.0, round(self.base_ms + delta, 2))
        elif self.mode == "normal":
            val = self.rng.gauss(self.base_ms, self.jitter_ms / 2.0 if self.jitter_ms > 0 else 1.0)
            return max(0.0, round(val, 2))
        return 0.0
