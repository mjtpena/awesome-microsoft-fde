"""The index sync removes superseded passages and fails loudly on errors.

Runs against fake Azure clients, so it needs the [azure] extra installed but
never calls Azure.
"""

from types import SimpleNamespace

import pytest

pytest.importorskip("azure.search.documents")

from harbourline import indexer


class FakeSearchClient:
    def __init__(self, existing_ids, fail_keys=()):
        self.existing_ids = existing_ids
        self.fail_keys = set(fail_keys)
        self.deleted = []

    def _results(self, documents):
        return [
            SimpleNamespace(key=d["id"], succeeded=d["id"] not in self.fail_keys, error_message="boom")
            for d in documents
        ]

    def upload_documents(self, documents):
        return self._results(documents)

    def delete_documents(self, documents):
        self.deleted.extend(d["id"] for d in documents)
        return self._results(documents)

    def search(self, search_text, select):
        return [{"id": i} for i in self.existing_ids]


def run(monkeypatch, client):
    import azure.search.documents as sd
    import azure.search.documents.indexes as sdi

    monkeypatch.setattr(sd, "SearchClient", lambda *a, **k: client)
    monkeypatch.setattr(sdi, "SearchIndexClient", lambda *a, **k: SimpleNamespace(create_or_update_index=lambda i: None))
    return indexer.build_index("https://example.search.windows.net", "policies", credential=object())


def test_stale_passages_are_removed(monkeypatch):
    client = FakeSearchClient(existing_ids=["old-superseded-passage"])
    report = run(monkeypatch, client)
    assert client.deleted == ["old-superseded-passage"]
    assert "removed 1 stale passages" in report


def test_failed_upload_fails_the_hook(monkeypatch):
    from harbourline.corpus import load_passages

    first_id = load_passages()[0][0].id
    with pytest.raises(RuntimeError, match="upload failed"):
        run(monkeypatch, FakeSearchClient(existing_ids=[], fail_keys=[first_id]))
