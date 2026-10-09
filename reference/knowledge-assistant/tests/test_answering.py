"""The answer contract: cite a retrieved passage, or refuse."""

import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest

from harbourline.answering import REFUSAL, ExtractiveAnswerer, parse_answer


def test_extractive_answer_cites_its_passage(retriever):
    q = "What is the excess for a windscreen replacement?"
    answer = ExtractiveAnswerer().answer(q, retriever.search(q, ["all-staff"]))
    assert not answer.refused
    assert answer.citations == ["motor-excess-policy"]
    assert "£95" in answer.text


def test_extractive_refuses_off_topic_questions(retriever):
    q = "What is the excess on a travel insurance claim?"
    assert ExtractiveAnswerer().answer(q, retriever.search(q, ["all-staff"])).refused


def test_extractive_refuses_with_no_passages():
    assert ExtractiveAnswerer().answer("anything", []).refused


def test_uncited_model_answer_becomes_a_refusal(retriever):
    passages = retriever.search("windscreen excess", ["all-staff"])
    assert parse_answer("The excess is £95.", passages).refused


def test_citation_to_a_passage_we_did_not_retrieve_is_ignored(retriever):
    passages = retriever.search("windscreen excess", ["all-staff"])
    answer = parse_answer("The rate rises 7.5% [pricing-motor-rate-review-draft].", passages)
    assert answer.refused


def test_model_refusal_is_recognised(retriever):
    passages = retriever.search("windscreen excess", ["all-staff"])
    assert parse_answer(REFUSAL, passages).refused


def test_llm_answerer_calls_the_gateway_with_a_bearer_token_and_no_key(retriever):
    """Contract test against a fake gateway: path, auth header and parsing."""
    pytest.importorskip("agent_framework.openai")
    from harbourline.answering import LlmAnswerer

    seen = {}

    class FakeGateway(BaseHTTPRequestHandler):
        def do_POST(self):
            body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            seen.update(path=self.path, auth=self.headers.get("Authorization"), key=self.headers.get("api-key"))
            content = "A windscreen replacement carries an excess of £95 [motor-excess-policy]."
            out = json.dumps({
                "id": "1", "object": "chat.completion", "created": 0, "model": body["model"],
                "choices": [{"index": 0, "finish_reason": "stop", "message": {"role": "assistant", "content": content}}],
                "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2},
            }).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(out)))
            self.end_headers()
            self.wfile.write(out)

        def log_message(self, *args):
            pass

    server = HTTPServer(("127.0.0.1", 0), FakeGateway)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        answerer = LlmAnswerer(f"http://127.0.0.1:{server.server_port}/openai/v1", "chat", credential=lambda: "entra-token")
        q = "What is the excess for a windscreen replacement?"
        answer = answerer.answer(q, retriever.search(q, ["all-staff"]))
    finally:
        server.shutdown()

    assert seen == {"path": "/openai/v1/chat/completions", "auth": "Bearer entra-token", "key": None}
    assert answer.citations == ["motor-excess-policy"]
