import random
import string
from typing import Dict, Any

class SchemaGenerator:
    """Synthesizes mock JSON structures from light schema specs."""
    
    def __init__(self, seed: int = 42):
        self.rng = random.Random(seed)
        
    def generate_field(self, field_type: str) -> Any:
        if field_type == "string":
            return "".join(self.rng.choices(string.ascii_letters, k=8))
        elif field_type == "integer":
            return self.rng.randint(1, 1000)
        elif field_type == "float":
            return round(self.rng.uniform(10.0, 500.0), 2)
        elif field_type == "boolean":
            return self.rng.choice([True, False])
        elif field_type == "uuid":
            h = "".join(self.rng.choices(string.hexdigits.lower()[:16], k=32))
            return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:]}"
        return None
        
    def generate(self, spec: Dict[str, str]) -> Dict[str, Any]:
        return {k: self.generate_field(v) for k, v in spec.items()}
