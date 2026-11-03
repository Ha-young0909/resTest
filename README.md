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

## 테마

`dino game` 페이지 아래의 버튼으로 `기본`과 `빅라이트` 테마를 고를 수 있습니다. 빅라이트는 공룡 머리와 장애물을 `assets/dino-face.jpg`, `assets/obstacle-face.jpg` 사진으로 그리며, 사진은 `src/dino_game.html`에 data URI로 내장되어 있습니다(사진을 바꾸면 HTML의 data URI도 다시 만들어야 합니다).

## 일일 리더보드 (Supabase)

`dino game` 페이지는 Supabase로 하루(한국 시간 기준) 단위 TOP 10을 보여줍니다. 플레이어당 그날의 최고 점수 1건만 저장됩니다.

1. `supabase/migrations/20261103000000_dino_daily_leaderboard.sql`을 프로젝트에 적용합니다 (`supabase db push` 또는 SQL Editor).
2. `.streamlit/secrets.toml.example`을 `.streamlit/secrets.toml`로 복사해 `SUPABASE_URL`, `SUPABASE_ANON_KEY`를 채웁니다 (환경변수로도 가능). service_role 키는 넣지 마세요.

설정이 없으면 리더보드 없이 게임만 동작합니다. 테이블은 RLS로 잠겨 있고 `submit_dino_score` / `get_dino_daily_leaderboard` 함수로만 접근합니다.

## 테스트

```bash
pip install pytest
pytest
```

## 구조

```
.github/workflows/  CI 설정
supabase/           DB 마이그레이션
src/                소스 코드 (main.py: 채팅, pages/dino_game.py + dino_game.html: 공룡 게임)
tests/              테스트
docs/               문서 (architecture.md)
assets/             이미지 및 정적 리소스
```

## 라이선스

MIT. 자세한 내용은 [LICENSE](LICENSE)를 보세요.
