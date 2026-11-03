import streamlit as st
from ai import get_answer

st.title("AI 채팅")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:                 # 기존 대화 다시 그리기
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("메시지를 입력하세요"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("생각 중..."):
            answer = get_answer(st.session_state.messages)
        st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
