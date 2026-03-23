from src.latency.simulator import LatencySimulator

def test_fixed_latency():
    sim = LatencySimulator(mode="fixed", base_ms=50.0)
    assert sim.compute_delay_ms() == 50.0

def test_jitter_latency():
    sim = LatencySimulator(mode="jitter", base_ms=100.0, jitter_ms=20.0, seed=7)
    for _ in range(10):
        d = sim.compute_delay_ms()
        assert 80.0 <= d <= 120.0
