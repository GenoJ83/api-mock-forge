from typing import Optional, Callable
from src.core.types import MockRequest, MockResponse

class PassthroughProxy:
    def __init__(self, upstream_handler: Optional[Callable[[MockRequest], MockResponse]] = None):
        self.upstream_handler = upstream_handler
        
    def forward(self, req: MockRequest) -> MockResponse:
        if self.upstream_handler:
            return self.upstream_handler(req)
        return MockResponse(status_code=502, body={"error": "No upstream proxy configured"})
