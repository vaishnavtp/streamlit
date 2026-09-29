import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete


st.title("Book Details")

i = st.number_input("Enter Id")

btn = st.button("Retrieve")

if btn:
    b = BookListCreateRetrieveUpdateDelete()

    record = b.retrieve(i)

    if record:
        st.write("Title", record[1])
        st.write("Author", record[2])
        st.write("Price", record[3])
        st.write("Pages", record[4])
        st.write("Language", record[5])
    else:
        st.write("No record found")