from src.routing.route import Route
from src.core.types import MockResponse

def test_static_route_match():
    r = Route("GET", "/health", MockResponse(status_code=200))
    assert r.match("GET", "/health") == {}
    assert r.match("POST", "/health") is None
    assert r.match("GET", "/other") is None

def test_parameterized_route_match():
    r = Route("GET", "/users/:userId/orders/{orderId}", MockResponse(status_code=200))
    match = r.match("GET", "/users/usr_99/orders/ord_101")
    assert match == {"userId": "usr_99", "orderId": "ord_101"}
