from src.schema.nested import NestedSchemaGenerator

def test_nested_generation():
    gen = NestedSchemaGenerator(seed=99)
    spec = {
        "user": {"name": "string", "id": "uuid"},
        "tags": ["string", 3],
        "items": [{"sku": "string", "qty": "integer"}, 2]
    }
    res = gen.generate_complex(spec)
    assert "user" in res and "name" in res["user"]
    assert len(res["tags"]) == 3
    assert len(res["items"]) == 2
    assert "sku" in res["items"][0]
