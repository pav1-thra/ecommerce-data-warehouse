# etl/load.py

from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:Pavithra%402004@localhost:5432/ecommerce_dw"

engine = create_engine(DATABASE_URL)

def load_data(data):

    data["customers"].to_sql(
        "customers",
        engine,
        if_exists="replace",
        index=False
    )

    data["products"].to_sql(
        "products",
        engine,
        if_exists="replace",
        index=False
    )

    data["orders"].to_sql(
        "orders",
        engine,
        if_exists="replace",
        index=False
    )

    data["payments"].to_sql(
        "payments",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded successfully.")