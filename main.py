import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from supabase import create_client, Client
from sqlalchemy import create_engine

# Import Data from Supabase
SUPABASE_DATABASE_URL = (
    "postgresql://postgres.pjehdrugpzsjqwcmxsmg:yJ17Elq905YI6ij3@aws-0-us-west-1.pooler.supabase.com:5432/postgres"
)

# Create SQLAlchemy engine for connecting to the database
engine = create_engine(SUPABASE_DATABASE_URL)

# Use a SQL query to fetch the data from the 'Villa' table
# Ensure the column names match the actual database column names
query = "SELECT * FROM Villa"
df = pd.read_sql(query, con=engine.connect())

# Ensure column names are clean and accessible
df_selected = df[["Silahkan Isi Data Anda !", "Kelas"]]

# Streamlit application layout
st.title("Pendaftar Villanations V3 LabTI")

# Display the selected dataframe in the Streamlit app
st.dataframe(df_selected, use_container_width=True)

# Optional: Visualize some data with Seaborn or Matplotlib (just an example)
# st.write("Data Visualization Example:")
# sns.countplot(x='Kelas', data=df_selected)
# st.pyplot(plt)
