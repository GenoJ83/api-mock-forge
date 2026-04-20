import pytest
from src.assertions.journal_assert import JournalAssertions
from src.journal.recorder import RequestJournal
from src.core.types import MockRequest

def test_journal_assertions():
    j = RequestJournal()
    j.record(MockRequest("GET", "/v1/status"))
    JournalAssertions.assert_called(j, "GET", "/v1/status", 1)
    JournalAssertions.assert_not_called(j, "POST", "/v1/status")
    with pytest.raises(AssertionError):
        JournalAssertions.assert_called(j, "GET", "/v1/status", 2)
