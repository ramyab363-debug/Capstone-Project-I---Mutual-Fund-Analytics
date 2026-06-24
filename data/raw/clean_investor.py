import pandas as pd

df = pd.read_csv("08_investor_transactions.csv")

# convert date
df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")

# clean text columns
df["transaction_type"] = df["transaction_type"].str.strip().str.title()
df["kyc_status"] = df["kyc_status"].str.strip().str.title()

# valid transaction types
valid_types = ["Sip", "Lumpsum", "Redemption"]
df = df[df["transaction_type"].isin(valid_types)]

# valid KYC values
valid_kyc = ["Verified", "Pending", "Rejected"]
df = df[df["kyc_status"].isin(valid_kyc)]

# amount validation
df["amount_inr"] = pd.to_numeric(df["amount_inr"], errors="coerce")
df = df[df["amount_inr"] > 0]

# remove duplicates
df = df.drop_duplicates()

# save cleaned file
df.to_csv("08_investor_transactions_cleaned.csv", index=False)

print("INVESTOR CLEANING DONE")