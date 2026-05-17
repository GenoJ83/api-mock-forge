from typing import Dict, Any

class MetricsCollector:
    def __init__(self):
        self.status_counters: Dict[int, int] = {}
        self.total_requests = 0
        
    def observe(self, status_code: int) -> None:
        self.total_requests += 1
        self.status_counters[status_code] = self.status_counters.get(status_code, 0) + 1
        
    def get_summary(self) -> Dict[str, Any]:
        return {
            "total_requests": self.total_requests,
            "by_status": dict(self.status_counters)
        }
