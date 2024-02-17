import streamlit as st
import requests
import json

# Инициализация сессионных переменных, если они еще не были установлены
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = ''
if 'role' not in st.session_state:
    st.session_state['role'] = ''

# Форма авторизации, если пользователь не аутентифицирован
if not st.session_state['authenticated']:
    st.title('Авторизация пользователя')

    with st.form("auth_form"):
        username = st.text_input("Имя пользователя")
        password = st.text_input("Пароль", type="password")
        submit_button = st.form_submit_button("Авторизоваться")

    if submit_button:
        response = requests.post("http://localhost:8000/test/v1/auth/", data={
            "username": username,
            "password": password
        })
        if response.status_code == 200:
            user_data = response.json()
            st.session_state['authenticated'] = True
            st.session_state['username'] = user_data['username']
            st.session_state['role'] = user_data.get('role', 'Пользователь')  # Предполагаем, что ответ содержит роль
            st.experimental_rerun()
        else:
            st.error("Ошибка авторизации. Проверьте введенные данные.")

# Главная страница, если пользователь аутентифицирован
if st.session_state['authenticated']:
    st.title(f"Добро пожаловать, {st.session_state['username']}!")
    st.subheader(f"Ваша роль: {st.session_state['role']}")
    # Здесь может быть дополнительный контент главной страницы

