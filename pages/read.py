import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("Read Record")

b = BookListCreateRetrieveUpdateDelete()

records = b.list()

if records:
    st.table(records)
else:
    st.write("No records")
