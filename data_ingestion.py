import pandas as pd
import os

data_path = "data/raw"

files = os.listdir(data_path)

for file in files:
    if file.endswith(".csv"):
        file_path = os.path.join(data_path, file)

        try:
            df = pd.read_csv(file_path)

            print("\n" + "=" * 60)
            print(f"FILE: {file}")
            print("=" * 60)

            print("\nShape:")
            print(df.shape)

            print("\nData Types:")
            print(df.dtypes)

            print("\nFirst 5 Rows:")
            print(df.head())

        except Exception as e:
            print(f"Error loading {file}: {e}")