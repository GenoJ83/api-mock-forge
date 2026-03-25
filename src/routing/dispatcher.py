from typing import List, Optional, Tuple, Dict, Any
from src.routing.route import Route
from src.core.types import MockRequest, MockResponse
from src.core.exceptions import RouteConflictError

class RouteDispatcher:
    def __init__(self):
        self.routes: List[Route] = []
        
    def register(self, method: str, path: str, response: MockResponse) -> Route:
        for r in self.routes:
            if r.method == method.upper() and r.raw_path == path:
                raise RouteConflictError(f"Route {method} {path} already registered")
        route = Route(method, path, response)
        self.routes.append(route)
        return route
        
    def dispatch(self, req: MockRequest) -> Optional[Tuple[MockResponse, Dict[str, str]]]:
        for route in self.routes:
            params = route.match(req.method, req.path)
            if params is not None:
                return route.response, params
        return None
