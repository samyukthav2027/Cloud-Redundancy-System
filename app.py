import streamlit as st
import sqlite3
from validator import validate_data

st.set_page_config(page_title="Cloud Data Redundancy System")

st.title("☁️ Cloud Data Redundancy System")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Data","View Database"]
)

if menu=="Add Data":

    st.subheader("Add New Record")

    name=st.text_input("Name")

    email=st.text_input("Email")

    phone=st.text_input("Phone")

    if st.button("Submit"):

        result=validate_data(name,email,phone)

        if result=="Unique":

            conn=sqlite3.connect("cloud.db")

            cursor=conn.cursor()

            cursor.execute(
                "INSERT INTO cloud_data(name,email,phone) VALUES(?,?,?)",
                (name,email,phone)
            )

            conn.commit()

            conn.close()

            st.success("Data Added Successfully")

        elif result=="Duplicate":

            st.error("Duplicate Record")

        else:

            st.warning("False Positive Found")



elif menu=="View Database":

    conn=sqlite3.connect("cloud.db")

    cursor=conn.cursor()

    cursor.execute("SELECT * FROM cloud_data")

    rows=cursor.fetchall()

    st.subheader("Database")

    st.table(rows)

    conn.close()