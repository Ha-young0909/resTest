import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ai import get_answer


def test_get_answer_echoes_last_message():
    messages = [{"role": "user", "content": "안녕"}]
    assert "안녕" in get_answer(messages)
