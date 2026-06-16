import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Diksha%402003@localhost:5432/ecommerce"
)

datasets = {
    "customers": "data/olist_customers_dataset.csv",
    "products": "data/olist_products_dataset.csv",
    "payments": "data/olist_order_payments_dataset.csv",
    "reviews": "data/olist_order_reviews_dataset.csv",
    "order_items": "data/olist_order_items_dataset.csv"
}

for table, file in datasets.items():
    df = pd.read_csv(file)

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{table} loaded successfully")