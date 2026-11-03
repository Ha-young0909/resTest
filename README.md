# resTest

Streamlit 기반 AI 채팅 앱입니다.

## 실행

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run src/main.py
```

실행하면 왼쪽 사이드바에서 `main`(AI 채팅)과 `dino game`(공룡 게임)을 오갈 수 있습니다.

## 테스트

```bash
pip install pytest
pytest
```

## 구조

```
.github/workflows/  CI 설정
src/                소스 코드 (main.py: 채팅, pages/dino_game.py + dino_game.html: 공룡 게임)
tests/              테스트
docs/               문서 (architecture.md)
assets/             이미지 및 정적 리소스
```

## 라이선스

MIT. 자세한 내용은 [LICENSE](LICENSE)를 보세요.
