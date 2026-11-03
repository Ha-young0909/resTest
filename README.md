# resTest

Streamlit 기반 AI 채팅 앱입니다.

## 실행

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run src/main.py
```

## 테스트

```bash
pip install pytest
pytest
```

## 구조

```
.github/workflows/  CI 설정
src/                소스 코드
tests/              테스트
docs/               문서 (architecture.md)
assets/             이미지 및 정적 리소스
```

## 라이선스

MIT. 자세한 내용은 [LICENSE](LICENSE)를 보세요.
