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


def test_leaderboard_disabled_without_supabase_config():
    html = load_game_html()
    assert '"__SUPABASE_URL__"' in html  # 치환되지 않으면 JS가 리더보드를 꺼둔다.


def test_supabase_config_is_injected_as_js_string_literals():
    html = load_game_html('https://x.supabase.co', 'key"with\\quote')
    assert '"https://x.supabase.co"' in html
    assert '"key\\"with\\\\quote"' in html
    assert "__SUPABASE_URL__" not in html and "__SUPABASE_KEY__" not in html


def test_leaderboard_renders_names_without_innerhtml():
    # 닉네임은 사용자 입력이므로 innerHTML로 그리면 XSS가 된다.
    assert "innerHTML" not in load_game_html()
