import streamlit as st 
from openai import OpenAI

modelo = OpenAI(api_key='') #modelo e a chave para acesso da IA

st.write('### ChatBot com IA')

# session_state é um dicionário = memória do streamlit
if not 'lista_mensagens' in st.session_state:
    st.session_state['lista_mensagens'] = []

# #adicionar uma mensagem
# st.session_state['lista_mensagens'].append(mensagem)

#exibir o histórico de mensagem
for mensagem in st.session_state['lista_mensagens']:
    role = mensagem['role']
    content = mensagem['content']
    st.chat_message(role).write(content) #1 argumento é quem enviou a mensagem, e o 2 é o texto da mensagem

mensagem_usuario = st.chat_input('Escreva sua mensagem aqui')

if mensagem_usuario:
    #user -> ser humano
    #assistant -> IA
    st.chat_message('user').write(mensagem_usuario)
    mensagem = {'role' : 'user', 'content' : mensagem_usuario}
    st.session_state['lista_mensagens'].append(mensagem)

    #resposta da IA
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state['lista_mensagens'],
        model='gpt-4o' #modelo de IA a ser usado
    )
    print(resposta_modelo)
    resposta_ia = resposta_modelo.choices[0].message.content #pega o campo mensagem da lista gerada como resposta da IA
    

    #exibir a resposta da IA na tela
    st.chat_message('assistant').write(resposta_ia)
    mensagem_ia = {'role' : 'assistant', 'content' : resposta_ia}
    st.session_state['lista_mensagens'].append(mensagem_ia)

    # print(st.session_state['lista_mensagens'])

#Para executar o streamlit via navegador use - python -m streamlit run main.py
