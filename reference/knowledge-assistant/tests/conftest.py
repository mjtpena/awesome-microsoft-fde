import sys
from pathlib import Path

import pytest

from harbourline import LocalRetriever, load_passages

# Let tests import evals/run_evals.py as a module.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "evals"))


@pytest.fixture(scope="session")
def retriever():
    return LocalRetriever(load_passages()[0])
