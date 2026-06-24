import pandas as pd
from sqlalchemy import create_engine

# load cleaned files
nav = pd.read_csv("02_nav_history_cleaned.csv")
scheme = pd.read_csv("07_scheme_performance_cleaned.csv")
investor = pd.read_csv("08_investor_transactions_cleaned.csv")

# create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# push to database
nav.to_sql("nav_history", engine, if_exists="replace", index=False)
scheme.to_sql("scheme_performance", engine, if_exists="replace", index=False)
investor.to_sql("investor_transactions", engine, if_exists="replace", index=False)

print("DATABASE CREATED bluestock_mf.db")