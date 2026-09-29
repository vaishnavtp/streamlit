import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("Delete Record")

i = st.number_input("Enter Id", min_value=1, step=1)

btn = st.button("Delete")

if btn:
    b = BookListCreateRetrieveUpdateDelete()

    b.delete(i)

    st.success("Record deleted successfully")