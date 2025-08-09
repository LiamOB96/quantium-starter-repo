import pandas as pd
from pathlib import Path

# Paths
ROOT = Path(__file__).resolve().parents[1]   # project root
DATA_DIR = ROOT / "data"
OUTPUT = DATA_DIR / "processed_sales.csv"

# Obtain csv files
csv_files = DATA_DIR.glob("*.csv")

data_frames = []

for csv_file in csv_files:
    df = pd.read_csv(csv_file)

    # Obtain rows with pink morsels
    mask = df['product'] == 'pink morsel'

    # Remove dollar signs in price values
    if df.loc[mask, 'price'].dtype == "object":
        df.loc[mask, 'price'] = df.loc[mask, 'price'].str.replace("$", "", regex=False).str.strip()

    # Convert quantity and price columns to numeric
    df.loc[mask, 'quantity'] = pd.to_numeric(df.loc[mask, 'quantity'], errors="coerce")
    df.loc[mask, 'price'] = pd.to_numeric(df.loc[mask, 'price'], errors="coerce")

    # Calculate sales
    df.loc[mask, 'sales'] = df.loc[mask, 'quantity'] * df.loc[mask, 'price']

    # Select only relevant columns from pink morsel rows
    pink_morsel_rows = df.loc[mask, ['sales', 'date', 'region']]

    # Append relevant pink morsel data
    data_frames.append(pink_morsel_rows)

final_df = pd.concat(data_frames, ignore_index=True)

# Save the combined result to a new CSV
output_path = DATA_DIR / "processed_sales.csv"
final_df.to_csv(output_path)

