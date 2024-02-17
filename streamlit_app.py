import streamlit as st
import requests

st.title('Регистрация пользователя')

username = st.text_input("Имя пользователя")
password = st.text_input("Пароль", type="password")
role = st.selectbox("Роль", ["Пользователь", "Администратор"])

if st.button('Регистрация'):
    response = requests.post("http://localhost:8000/test/v1/reg/", data={
        "username": username,
        "password": password,
        "role": role
    })
    if response.status_code == 200:
        st.success("Пользователь успешно зарегистрирован!")
    else:
        st.error("Ошибка при регистрации пользователя.")
