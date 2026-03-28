import streamlit as st
import pandas as pd
import os

FILE_NAME = "expenses.csv"

# Function to save expense
def save_expense(category, amount):
    new_data = pd.DataFrame({
        "Category": [category],
        "Amount": [amount]
    })

    if os.path.exists(FILE_NAME):
        new_data.to_csv(FILE_NAME, mode='a', header=False, index=False)
    else:
        new_data.to_csv(FILE_NAME, index=False)


st.title("Smart Expense Tracker ")

amount = st.number_input("Enter amount")
category = st.text_input("Enter category")

if st.button("Add Expense"):
    if category and amount > 0:
        save_expense(category, amount)
        st.success(f"Added: ₹{amount} for {category}")
    else:
        st.warning("Please enter valid data")