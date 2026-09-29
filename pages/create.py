import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("Add New Record")

t = st.text_input("Title")
a = st.text_input("Author")
p = st.number_input("Price", min_value=0)
pg = st.number_input("Pages", min_value=0)
l = st.text_input("Language")

btn = st.button("Add")

if btn:
    b = BookListCreateRetrieveUpdateDelete()
    b.create(t, a, p, l, pg)
    st.success("Create Record Successfully")