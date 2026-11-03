import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from dino import load_game_html


def test_game_html_is_self_contained_canvas_game():
    html = load_game_html()
    assert "<canvas" in html
    assert "requestAnimationFrame" in html
    # 외부 리소스를 불러오지 않아야 한다.
    assert "http://" not in html and "https://" not in html


def test_game_html_uses_observed_constants():
    html = load_game_html()
    for token in ("GRAVITY: 0.6", "MAX_SPEED: 13", "CACTUS_SMALL", "CACTUS_LARGE", "PTERODACTYL"):
        assert token in html
