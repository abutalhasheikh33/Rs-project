from flask import Flask
from flask_cors import CORS
import pandas as pd

app = Flask( __name__ )
CORS(app)  # This will enable CORS for all routes
def recommend_budget(df):
    filteredDF = df[(df['Category'] == 'Shopping') | (df['Category'] == 'Gas & Fuel') | (df['Category'] == 'Paycheck') | (df['Category'] == 'Internet') | (df['Category'] == 'Fastfood') | (df['Category'] == 'Mortgage & Rent') | (df['Category'] == 'Groceries') | (df['Category'] == 'Mortgage & Rent') | (df['Category'] == 'Fast Food')]
    print(filteredDF)
    avg_spending = filteredDF.groupby('Category')['Amount'].mean()
    expected_budget_plan = {}
    for category, avg_amount in avg_spending.items():
        expected_budget_plan[category] = avg_amount * 0.8
    return expected_budget_plan


@app.route('/')
def budget_plan():
    df = pd.read_csv('personal_transactions.csv')
    budget_recommendation = recommend_budget(df)
    return budget_recommendation


if __name__=="__main__":
    app.run(debug=True,port=5000)
