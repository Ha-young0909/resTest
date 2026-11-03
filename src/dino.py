import json
import os
from pathlib import Path

GAME_HTML_PATH = Path(__file__).with_name("dino_game.html")


def load_game_html(supabase_url: str = "", supabase_key: str = "") -> str:
    """게임 HTML을 읽고 Supabase 설정을 채운다. 둘 중 하나라도 비면 리더보드 UI는 숨겨진다."""
    html = GAME_HTML_PATH.read_text(encoding="utf-8")
    if supabase_url and supabase_key:
        # json.dumps로 따옴표/백슬래시를 이스케이프해 JS 문자열 리터럴로 안전하게 넣는다.
        html = html.replace('"__SUPABASE_URL__"', json.dumps(supabase_url))
        html = html.replace('"__SUPABASE_KEY__"', json.dumps(supabase_key))
    return html


def get_supabase_config() -> tuple[str, str]:
    """(url, anon/publishable key). 환경변수 우선, 없으면 st.secrets. 없으면 빈 문자열."""
    url = os.environ.get("SUPABASE_URL", "")
    key = os.environ.get("SUPABASE_ANON_KEY", "")
    if not (url and key):
        import streamlit as st

        try:
            url = url or st.secrets.get("SUPABASE_URL", "")
            key = key or st.secrets.get("SUPABASE_ANON_KEY", "")
        except Exception:  # secrets.toml이 없으면 StreamlitSecretNotFoundError
            pass
    return url, key


def render_dino_game(height: int = 560) -> None:
    import streamlit as st

    html = load_game_html(*get_supabase_config())
    if hasattr(st, "iframe"):
        st.iframe(html, height=height)
    else:  # st.iframe이 없는 구버전 Streamlit
        import streamlit.components.v1 as components

        components.html(html, height=height)
