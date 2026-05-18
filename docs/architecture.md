# Architecture & Internals

`api-mock-forge` coordinates route resolution, chaos testing, in-memory journaling, and deterministic schema generation.

```
Request -> AuthMiddleware -> Dispatcher -> LatencySimulator -> ChaosInjector -> Response
                             |
                             v
                        Journal (Recorded)
```
