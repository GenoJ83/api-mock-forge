from typing import Dict, Any, List
from src.schema.generator import SchemaGenerator

class NestedSchemaGenerator(SchemaGenerator):
    """Extends schema synthesizer with nested objects and array repeating."""
    
    def generate_complex(self, spec: Dict[str, Any]) -> Dict[str, Any]:
        out = {}
        for k, v in spec.items():
            if isinstance(v, dict):
                out[k] = self.generate_complex(v)
            elif isinstance(v, list) and len(v) == 2 and isinstance(v[1], int):
                item_type = v[0]
                count = v[1]
                if isinstance(item_type, dict):
                    out[k] = [self.generate_complex(item_type) for _ in range(count)]
                else:
                    out[k] = [self.generate_field(item_type) for _ in range(count)]
            else:
                out[k] = self.generate_field(str(v))
        return out
