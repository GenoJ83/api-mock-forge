from src.middleware.auth import BearerAuthValidator
from src.core.types import MockRequest

def test_auth_validator():
    auth = BearerAuthValidator("secret-123")
    r1 = MockRequest("GET", "/secret")
    assert auth.validate(r1).status_code == 401
    
    r2 = MockRequest("GET", "/secret", headers={"Authorization": "Bearer wrong"})
    assert auth.validate(r2).status_code == 403
    
    r3 = MockRequest("GET", "/secret", headers={"Authorization": "Bearer secret-123"})
    assert auth.validate(r3) is None
