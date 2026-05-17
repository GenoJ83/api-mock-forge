from src.metrics.collector import MetricsCollector

def test_metrics_collector():
    m = MetricsCollector()
    m.observe(200)
    m.observe(200)
    m.observe(404)
    summ = m.get_summary()
    assert summ["total_requests"] == 3
    assert summ["by_status"][200] == 2
    assert summ["by_status"][404] == 1
