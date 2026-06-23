# etl/extract.py

import pandas as pd

def extract_data():

    customers = pd.read_csv("data/raw/customers.csv")
    products = pd.read_csv("data/raw/products.csv")
    orders = pd.read_csv("data/raw/orders.csv")
    payments = pd.read_csv("data/raw/payments.csv")

    return {
        "customers": customers,
        "products": products,
        "orders": orders,
        "payments": payments
    }