import openai
import streamlit as st
import os
from streamlit_chat import message as msg
import streamlit as st

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])
st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],)
    
    
openai.api_key = "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"
    
st.title("Olá, sou a I.A.R.A.S, como posso te ajudar hoje?")
st.subheader("Inteligência Artificial de Respostas Automáticas em Saúde")
st.write("Desenvolvido por alunos do 1º ano do Colégio Militar de Belém")
st.write("***")

if 'hst_conversa' not in st.session_state:
    st.session_state.hst_conversa = []

pergunta = st.text_input("Digite sua dúvida (por exemplo: Como limpar um machucado)")
btn_enviar = st.button("Enviar pergunta")

if btn_enviar:
    st.session_state.hst_conversa.append({"role": "user", "content": pergunta})
    retorno_openai = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.hst_conversa,
        max_tokens=500,
        n=1
    )

    st.session_state.hst_conversa.append(
        {"role": "assistant", "content": retorno_openai['choices'][0]['message']['content']})

if len(st.session_state.hst_conversa) > 0:
    for i in range(len(st.session_state.hst_conversa)):
        if i % 2 == 0:
            msg("Você: " + st.session_state.hst_conversa[i]['content'], is_user=True)
        else:
            msg("I.A.R.A.S: " + st.session_state.hst_conversa[i]['content'])
