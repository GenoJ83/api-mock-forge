from typing import List, Dict, Any
from src.engine import MockForgeEngine

class DeclarativeMockLoader:
    @staticmethod
    def load_from_dict(engine: MockForgeEngine, config: Dict[str, Any]) -> int:
        routes = config.get("routes", [])
        count = 0
        for r in routes:
            method = r.get("method", "GET")
            path = r.get("path", "/")
            status = r.get("status", 200)
            body = r.get("body", {})
            headers = r.get("headers", None)
            engine.mock(method, path, status_code=status, body=body, headers=headers)
            count += 1
        return count
