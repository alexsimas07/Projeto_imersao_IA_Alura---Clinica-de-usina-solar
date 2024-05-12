import streamlit as st
import google.generativeai as genai

google_api_key = 'AIzaSyBAyX79eUpFZvBxaN3W5YufoPWyNVKcHPA'

def retorna_resposta_modelo(mensagens,
                            google_api_key,
                            modelo="gemini-1.5-pro-latest"):
    genai.GenerativeModel = google_api_key
    response = genai.GenerativeModel.create(
        model=modelo,
        messages=mensagens
    )
    return response

import streamlit as st

def pagina_principal():
    if 'mensagens' not in st.session_state:
        st.session_state.mensagens = []

    mensagens = st.session_state.mensagens

    st.header("👨‍🚀 Mini Engenheiro Bulbe", divider=True)

    if not mensagens:
        mensagens.append({'role':'user', 'content':'O que são inversores nas usinas solares?'})
        mensagens.append({'role':'assistant', 'content':'Equipamento que faz a conversão da energia solar para energia elétrica'})

    for mensagem in mensagens:
        chat = st.chat_message(mensagem['role'])
        chat.markdown(mensagem['content'])

    prompt = st.chat_input("Qual é a sua dúvida, meu nobre?")
    if prompt:
        nova_mensagem = {'role':'user', 'content': prompt}
        chat = st.chat_message(nova_mensagem['role'])
        chat.markdown(nova_mensagem['content'])
        mensagens.append(nova_mensagem)

        chat = st.chat_message('assistant')
        resposta_completa = ''
        respostas = retorna_resposta_modelo(mensagens,
                                            google_api_key,
                                            stream=True)
        for resposta in respostas:
            resposta_completa += resposta.choices[0].deslta.get('content','')
            chat.markdown(resposta_completa + "▌")
        nova_mensagem = {'role': 'assistant',
                        'content':resposta_completa}
                        
                                            

        st.session_state['mensagens'] = mensagens

pagina_principal() 