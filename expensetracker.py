import streamlit as st

st.title("Smart Expense Tracker AI ")

amount = st.number_input("Enter amount")
category = st.text_input("Enter category")

if st.button("Add Expense"):
    st.write(f"Added: ₹{amount} for {category}")