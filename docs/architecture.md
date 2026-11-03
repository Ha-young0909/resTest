# 아키텍처

Streamlit으로 만든 간단한 AI 채팅 앱입니다.

```
src/main.py   Streamlit UI (대화 기록 표시, 입력 처리)
src/ai.py     get_answer(messages) -> str  (현재는 임시 답변, AI 연동으로 교체 예정)
src/utils.py  공용 헬퍼
tests/        pytest 테스트
```

## 흐름

1. 사용자가 `st.chat_input`으로 메시지를 입력한다.
2. `main.py`가 대화 기록(`st.session_state.messages`)과 함께 `ai.get_answer`를 호출한다.
3. 반환된 답변을 화면에 표시하고 기록에 추가한다.
