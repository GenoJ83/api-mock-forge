from src.journal.recorder import RequestJournal
from src.core.types import MockRequest

def test_journal_record_and_filter():
    j = RequestJournal(capacity=5)
    j.record(MockRequest("GET", "/users"))
    j.record(MockRequest("POST", "/users", body={"name": "Alice"}))
    j.record(MockRequest("GET", "/orders"))
    
    assert j.count() == 3
    assert j.count(method="GET") == 2
    assert j.count(method="POST", path="/users") == 1
    assert len(j.filter(path="/users")) == 2
