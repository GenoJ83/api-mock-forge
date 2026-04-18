from src.journal.recorder import RequestJournal

class JournalAssertions:
    @staticmethod
    def assert_called(journal: RequestJournal, method: str, path: str, times: int = 1) -> None:
        c = journal.count(method=method, path=path)
        if c != times:
            raise AssertionError(f"Expected {method} {path} to be called {times} times, but was called {c} times.")
            
    @staticmethod
    def assert_not_called(journal: RequestJournal, method: str, path: str) -> None:
        JournalAssertions.assert_called(journal, method, path, times=0)
