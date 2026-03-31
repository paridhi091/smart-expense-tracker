import streamlit as st
import pandas as pd
import os
from sklearn.linear_model import LinearRegression
import numpy as np 

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

if os.path.exists(FILE_NAME):
    df = pd.read_csv(FILE_NAME)

    st.subheader(" Your Expenses")
    st.dataframe(df)

    # Total spending
    total = df["Amount"].sum()
    st.metric("Total Spending", f"₹ {total}")

    # 📊 Smart Insights
if os.path.exists(FILE_NAME):
    df = pd.read_csv(FILE_NAME)

    st.subheader(" Smart Insights")

    # 1. Highest spending category
    top_category = df.groupby("Category")["Amount"].sum().idxmax()
    top_amount = df.groupby("Category")["Amount"].sum().max()
    st.write(f" You spend the most on **{top_category}** (₹{top_amount})")

    # 2. Average expense
    avg = df["Amount"].mean()
    st.write(f" Your average expense is ₹{avg:.2f}")

    # 3. Simple warning
    if avg > 1000:
        st.warning(" Your average spending is high!")
    else:
        st.success(" Your spending is under control")


    if len(df) > 1:
        df["Day"] = range(1, len(df) + 1)

        X = df[["Day"]]
        y = df["Amount"]

        model = LinearRegression()
        model.fit(X, y)

        future_day = np.array([[len(df) + 1]])
        prediction = model.predict(future_day)

        st.subheader(" Predicted Next Expense")
        st.write(f"₹ {prediction[0]:.2f}")
    else:
        st.info("Add at least 2 expenses for prediction")
        
        
else:
    st.warning("No expenses yet!")