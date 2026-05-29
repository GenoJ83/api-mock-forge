# api-mock-forge

High-throughput declarative HTTP mock and API simulation engine with dynamic schema synthesis, latency emulation, and request verification hooks.

[![CI](https://github.com/GenoJ83/api-mock-forge/actions/workflows/ci.yml/badge.svg)](https://github.com/GenoJ83/api-mock-forge/actions)

## Quick Start
```python
from src.engine import MockForgeEngine
from src.core.types import MockRequest

engine = MockForgeEngine(default_latency_ms=15.0)
engine.mock('GET', '/users/:id', 200, {'name': 'Alice', 'role': 'Admin'})

resp = engine.handle_request(MockRequest('GET', '/users/usr_42'))
print(resp.status_code, resp.body)
```

## Architecture
- **Route Dispatcher**: Parameterized regex path compilation (`/api/:version/{item}`)
- **Schema Synthesizer**: Seeded schema generation with nested arrays and UUIDs
- **Chaos & Fault Injection**: Configurable failure rates and HTTP status overrides
- **Request Journal**: In-memory ring buffer with fluent assertion helpers
