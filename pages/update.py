import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("Update Record")

i = st.number_input("Enter Id", min_value=1, step=1)

title = st.text_input("Title")
author = st.text_input("Author")
price = st.number_input("Price", min_value=0, step=1)
pages = st.number_input("Pages", min_value=0, step=1)
language = st.text_input("Language")

btn = st.button("Update")

if btn:
    b = BookListCreateRetrieveUpdateDelete()

    b.update(i, title, author, price, pages, language)

    st.success("Record updated successfully")