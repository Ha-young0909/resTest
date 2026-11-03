from pathlib import Path

GAME_HTML_PATH = Path(__file__).with_name("dino_game.html")


def load_game_html() -> str:
    return GAME_HTML_PATH.read_text(encoding="utf-8")


def render_dino_game(height: int = 230) -> None:
    import streamlit as st

    if hasattr(st, "iframe"):
        st.iframe(GAME_HTML_PATH, height=height)
    else:  # st.iframe이 없는 구버전 Streamlit
        import streamlit.components.v1 as components

        components.html(load_game_html(), height=height)
