# smart-expense-tracker


##  Overview

Smart Expense Tracker is a beginner-friendly web application built using Python and Streamlit. It helps users record their daily expenses, analyze spending patterns, and get basic predictions using machine learning.

---

##  Features

* Add and store daily expenses
* View all expenses in a table
* Calculate total spending
* Get insights on spending habits
* Predict next expense using AI (Linear Regression)

---

##  Tech Stack

* Python
* Streamlit
* Pandas
* Scikit-learn

---

##  Project Structure

```
expensetracker.py   # Main application file  
expenses.csv        # Stores expense data (auto-created)  
README.md           # Project documentation  
```

---

##  Installation & Setup

### 1. Clone the repository

```
git clone <https://github.com/paridhi091/smart-expense-tracker>
cd <smart-expense-tracker>
```

### 2. Install required libraries

```
pip install streamlit pandas scikit-learn
```

---

##  How to Run

Run the following command in terminal:

```
streamlit run expensetracker.py
```

Then open the link shown 

---

## How to Use

1. Enter the expense amount
2. Enter the category (e.g., Food, Travel)
3. Click **Add Expense**
4. View your expenses in the table
5. Check total spending and prediction

---

##  AI Feature

This project uses a simple **Linear Regression model** to predict the next expense based on previous spending data.

---

##  Problem It Solves

Many people do not track their daily expenses and end up overspending.
This app helps users monitor their spending, understand patterns, and make better financial decisions.

---

##  Future Improvements

* Add charts and graphs
* Monthly expense prediction
* User authentication system
* Database integration
* Improved UI design


---

##  Note

This is a beginner-level project created for learning purposes.
