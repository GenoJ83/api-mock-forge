from typing import Optional
from src.core.types import MockRequest, MockResponse

class BearerAuthValidator:
    def __init__(self, expected_token: str):
        self.expected_token = expected_token
        
    def validate(self, req: MockRequest) -> Optional[MockResponse]:
        auth_hdr = req.headers.get("Authorization", "")
        if not auth_hdr.startswith("Bearer "):
            return MockResponse(status_code=401, body={"error": "Missing or invalid bearer token"})
        token = auth_hdr.split("Bearer ", 1)[1].strip()
        if token != self.expected_token:
            return MockResponse(status_code=403, body={"error": "Forbidden"})
        return None
