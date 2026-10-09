"""Permission trimming happens in retrieval, before any model sees the text."""

import pytest

from harbourline.retrieval import AzureSearchRetriever, tokenize

PRICING_Q = "What base rate increase is proposed in the motor rate review?"


def test_pricing_draft_is_trimmed_for_a_non_pricing_user(retriever):
    results = retriever.search(PRICING_Q, ["all-staff"], k=20)
    assert all("pricing" not in p.groups for p in results)
    assert "pricing-motor-rate-review-draft" not in {p.doc_id for p in results}


def test_pricing_user_can_retrieve_the_draft(retriever):
    results = retriever.search(PRICING_Q, ["all-staff", "pricing"], k=5)
    assert results[0].doc_id == "pricing-motor-rate-review-draft"


def test_user_with_no_groups_sees_nothing(retriever):
    assert retriever.search("windscreen excess", [], k=5) == []


def test_superseded_text_is_never_retrieved(retriever):
    results = retriever.search("windscreen replacement excess", ["all-staff"], k=20)
    assert results[0].doc_id == "motor-excess-policy"
    assert not any("£60" in p.content or "£75" in p.content for p in results)


def test_results_are_ranked_and_capped(retriever):
    results = retriever.search("excess", ["all-staff"], k=3)
    assert len(results) == 3
    assert [p.score for p in results] == sorted((p.score for p in results), reverse=True)


def test_rare_unmatched_word_lowers_the_match(retriever):
    on_topic = retriever.search("motor windscreen excess", ["all-staff"])[0]
    off_topic = retriever.search("travel insurance excess", ["all-staff"])[0]
    assert on_topic.match > 0.9
    assert off_topic.match < 0.25


def test_tokenize_folds_plurals_and_drops_stopwords():
    assert tokenize("What are the claims for windscreens?") == ["claim", "windscreen"]


def test_azure_group_filter_and_injection_guard():
    assert AzureSearchRetriever.group_filter(["all-staff", "pricing"]) == (
        "groups/any(g: search.in(g, 'all-staff,pricing', ','))"
    )
    with pytest.raises(ValueError):
        AzureSearchRetriever.group_filter(["all-staff') or true or ('"])
