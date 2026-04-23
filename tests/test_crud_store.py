from src.state.crud_store import CrudStore

def test_crud_lifecycle():
    store = CrudStore()
    item = store.create({"title": "Fix bug"})
    assert "id" in item
    assert store.get(item["id"])["title"] == "Fix bug"
    store.update(item["id"], {"title": "Updated"})
    assert store.get(item["id"])["title"] == "Updated"
    assert store.delete(item["id"]) is True
    assert store.get(item["id"]) is None
