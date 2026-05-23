from src.engine import MockForgeEngine
from src.core.types import MockRequest
from src.chaos.injector import ChaosInjector

def test_full_pipeline_flow():
    engine = MockForgeEngine(default_latency_ms=5.0)
    engine.mock("GET", "/status", 200, {"uptime": 9999})
    req = MockRequest("GET", "/status")
    resp = engine.handle_request(req)
    assert resp.status_code == 200
    assert resp.body["uptime"] == 9999
    assert engine.journal.count() == 1
