from src.engine import MockForgeEngine
from src.core.types import MockRequest

def test_engine_mock_lifecycle():
    engine = MockForgeEngine(default_latency_ms=10.0)
    engine.mock("GET", "/api/v1/ping", status_code=200, body={"ping": "pong"})
    
    res = engine.handle_request(MockRequest("GET", "/api/v1/ping"))
    assert res.status_code == 200
    assert res.body == {"ping": "pong"}
    assert res.latency_ms == 10.0
    assert engine.journal.count(path="/api/v1/ping") == 1
    
    res_404 = engine.handle_request(MockRequest("POST", "/missing"))
    assert res_404.status_code == 404
