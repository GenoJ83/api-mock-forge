from src.dsl.loader import DeclarativeMockLoader
from src.engine import MockForgeEngine
from src.core.types import MockRequest

def test_declarative_loader():
    engine = MockForgeEngine()
    config = {
        "routes": [
            {"method": "GET", "path": "/ping", "status": 200, "body": {"ok": True}},
            {"method": "DELETE", "path": "/items/:id", "status": 204}
        ]
    }
    count = DeclarativeMockLoader.load_from_dict(engine, config)
    assert count == 2
    resp = engine.handle_request(MockRequest("GET", "/ping"))
    assert resp.status_code == 200 and resp.body == {"ok": True}
