from src.chaos.injector import ChaosInjector
from src.core.types import MockResponse

def test_chaos_fault_injection():
    chaos = ChaosInjector(error_rate=1.0, seed=12)
    res = chaos.maybe_inject(MockResponse(status_code=200, body={"ok": True}))
    assert res.status_code in [500, 503, 504]
    assert "chaos" in res.body
