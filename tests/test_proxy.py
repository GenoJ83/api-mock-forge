from src.proxy.passthrough import PassthroughProxy
from src.core.types import MockRequest, MockResponse

def test_proxy_delegation():
    handler = lambda r: MockResponse(status_code=200, body={"proxied": r.path})
    proxy = PassthroughProxy(upstream_handler=handler)
    res = proxy.forward(MockRequest("GET", "/remote/resource"))
    assert res.status_code == 200 and res.body == {"proxied": "/remote/resource"}
