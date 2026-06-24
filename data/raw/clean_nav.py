import pandas as pd

# load data
df = pd.read_csv("02_nav_history.csv")

# convert date
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# remove duplicates
df = df.drop_duplicates()

# sort
df = df.sort_values(["amfi_code", "date"])

# forward fill NAV
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# remove invalid NAV
df = df[df["nav"] > 0]

# save cleaned file
df.to_csv("02_nav_history_cleaned.csv", index=False)

print(" Cleaned file created")