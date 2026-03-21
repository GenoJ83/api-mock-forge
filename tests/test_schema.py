from src.schema.generator import SchemaGenerator

def test_generate_primitives():
    gen = SchemaGenerator(seed=123)
    res = gen.generate({"name": "string", "age": "integer", "score": "float", "active": "boolean", "id": "uuid"})
    assert isinstance(res["name"], str)
    assert isinstance(res["age"], int)
    assert isinstance(res["score"], float)
    assert isinstance(res["active"], bool)
    assert len(res["id"].split("-")) == 5
