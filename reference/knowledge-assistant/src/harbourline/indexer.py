"""Push the indexable passages to Azure AI Search. Run by the azd postprovision hook.

The same `load_passages` rule decides what goes in, offline and in Azure, so the
local eval and the cloud index can't disagree about which version is current.
"""

from __future__ import annotations

from pathlib import Path

from .corpus import DEFAULT_DATA_DIR, load_passages


def build_index(endpoint: str, index_name: str, data_dir: Path = DEFAULT_DATA_DIR, credential=None) -> list[str]:
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchableField, SearchFieldDataType, SearchIndex, SimpleField

    credential = credential or DefaultAzureCredential()
    index = SearchIndex(
        name=index_name,
        fields=[
            SimpleField(name="id", type=SearchFieldDataType.STRING, key=True),
            SimpleField(name="doc_id", type=SearchFieldDataType.STRING, filterable=True),
            SearchableField(name="title"),
            SearchableField(name="section"),
            SearchableField(name="content"),
            SimpleField(name="groups", type="Collection(Edm.String)", filterable=True),
        ],
    )
    SearchIndexClient(endpoint, credential).create_or_update_index(index)

    passages, skipped = load_passages(data_dir)
    docs = [
        {"id": p.id, "doc_id": p.doc_id, "title": p.title, "section": p.section, "content": p.content, "groups": list(p.groups)}
        for p in passages
    ]
    SearchClient(endpoint, index_name, credential).upload_documents(documents=docs)
    return [f"indexed {len(docs)} passages into {index_name}"] + [f"skipped {s}" for s in skipped]
