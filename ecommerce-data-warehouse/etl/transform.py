import pandas as pd

def transform_data(data):

    customers = data["customers"].drop_duplicates()
    products = data["products"].drop_duplicates()
    orders = data["orders"].drop_duplicates()
    payments = data["payments"].drop_duplicates()

    customers = customers.fillna("")
    products = products.fillna("")
    orders = orders.fillna(0)
    payments = payments.fillna(0)

    return {
        "customers": customers,
        "products": products,
        "orders": orders,
        "payments": payments
    }

