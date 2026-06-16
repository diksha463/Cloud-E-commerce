import pandas as pd

# Load datasets
customers = pd.read_csv('data/olist_customers_dataset.csv')
orders = pd.read_csv('data/olist_orders_dataset.csv')
print("Customers Shape:", customers.shape)
print("Orders Shape:", orders.shape)

print("\nCustomers Missing Values:")
print(customers.isnull().sum())

print("\nOrders Missing Values:")
print(orders.isnull().sum())
# Remove duplicates
orders.drop_duplicates(inplace=True)

# Convert date columns
date_columns = [
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_carrier_date',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col])

# Create Year and Month columns
orders['year'] = orders['order_purchase_timestamp'].dt.year
orders['month'] = orders['order_purchase_timestamp'].dt.month

print("\nCleaning Completed")
print(orders.head())
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Diksha%402003@localhost:5432/ecommerce"
)

print("PostgreSQL Connected Successfully")
orders.to_sql(
    'orders',
    engine,
    if_exists='replace',
    index=False
)

print("Orders table loaded successfully")