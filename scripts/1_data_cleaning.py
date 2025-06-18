import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import RAW_DATA_PATH, CLEANED_DATA_PATH


# Load data
df = pd.read_csv(RAW_DATA_PATH)


# Clean column names
df.columns = df.columns.str.strip().str.replace(' ', '_')

print("Columns in the DataFrame:", df.columns.tolist())

# Convert 'Yes/No' to booleans
df['International_plan'] = df['International_plan'].map({'Yes': True, 'No': False})
df['Voice_mail_plan'] = df['Voice_mail_plan'].map({'Yes': True, 'No': False})
df['Churn'] = df['Churn'].astype(str).str.upper().map({'TRUE': True, 'FALSE': False})

# Save cleaned data
df.to_csv(CLEANED_DATA_PATH, index=False)
print("Data cleaned and saved to:", CLEANED_DATA_PATH)
