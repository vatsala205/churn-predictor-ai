import pandas as pd
from sqlalchemy import create_engine
from config import CLEANED_DATA_PATH, DB_CONFIG

# Load cleaned data
df = pd.read_csv(CLEANED_DATA_PATH)

# Build connection string
url = f"mysql+mysqlconnector://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"
engine = create_engine(url)

# Dump to MySQL
df.to_sql('customer_data', con=engine, if_exists='replace', index=False)
print("Data dumped to MySQL table 'customer_data'")
