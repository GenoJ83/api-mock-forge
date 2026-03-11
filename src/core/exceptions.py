class MockForgeError(Exception):
    """Base exception for api-mock-forge."""

class RouteConflictError(MockForgeError):
    """Raised when conflicting routes are registered."""

class SchemaValidationError(MockForgeError):
    """Raised when generated response fails schema constraints."""
