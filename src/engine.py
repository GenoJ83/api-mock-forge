from typing import Optional, Dict, Any
from src.core.types import MockRequest, MockResponse
from src.routing.dispatcher import RouteDispatcher
from src.journal.recorder import RequestJournal
from src.latency.simulator import LatencySimulator

class MockForgeEngine:
    def __init__(self, default_latency_ms: float = 0.0):
        self.dispatcher = RouteDispatcher()
        self.journal = RequestJournal()
        self.latency_sim = LatencySimulator(mode="fixed", base_ms=default_latency_ms)
        
    def mock(self, method: str, path: str, status_code: int = 200, body: Any = None, headers: Optional[Dict[str, str]] = None):
        headers = headers or {"Content-Type": "application/json"}
        resp = MockResponse(status_code=status_code, body=body, headers=headers)
        return self.dispatcher.register(method, path, resp)
        
    def handle_request(self, req: MockRequest) -> MockResponse:
        self.journal.record(req)
        match = self.dispatcher.dispatch(req)
        if not match:
            return MockResponse(status_code=404, headers={"Content-Type": "application/json"}, body={"error": "Not Found"})
        base_resp, params = match
        delay = self.latency_sim.compute_delay_ms()
        return MockResponse(status_code=base_resp.status_code, headers=base_resp.headers, body=base_resp.body, latency_ms=delay)
