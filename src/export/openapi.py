import json
from typing import Dict, Any
from src.routing.dispatcher import RouteDispatcher

class OpenApiExporter:
    @staticmethod
    def export(dispatcher: RouteDispatcher, title: str = "Mock API") -> Dict[str, Any]:
        paths: Dict[str, Any] = {}
        for route in dispatcher.routes:
            p = route.raw_path
            m = route.method.lower()
            if p not in paths:
                paths[p] = {}
            paths[p][m] = {
                "responses": {
                    str(route.response.status_code): {
                        "description": f"Status {route.response.status_code} response"
                    }
                }
            }
        return {"openapi": "3.0.0", "info": {"title": title, "version": "1.0.0"}, "paths": paths}
