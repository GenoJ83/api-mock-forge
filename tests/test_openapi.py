from src.export.openapi import OpenApiExporter
from src.routing.dispatcher import RouteDispatcher
from src.core.types import MockResponse

def test_openapi_export():
    d = RouteDispatcher()
    d.register("GET", "/users", MockResponse(status_code=200))
    d.register("POST", "/users", MockResponse(status_code=201))
    doc = OpenApiExporter.export(d)
    assert doc["openapi"] == "3.0.0"
    assert "/users" in doc["paths"]
    assert "get" in doc["paths"]["/users"]
    assert "post" in doc["paths"]["/users"]
