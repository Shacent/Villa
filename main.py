import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Supabase connection URL
SUPABASE_DATABASE_URL = (
    "postgresql://postgres.pjehdrugpzsjqwcmxsmg:yJ17Elq905YI6ij3@aws-0-us-west-1.pooler.supabase.com:5432/postgres"
)

# Create SQLAlchemy engine for connecting to the database
engine = create_engine(SUPABASE_DATABASE_URL)

# Fetch data from the 'Villa' table
query = "SELECT * FROM Villa"
df = pd.read_sql(query, con=engine)

# Ensure the columns you want are correctly selected and available
# Make sure that "Silahkan Isi Data Anda !" and "Kelas" exist in your table
# If the column names are different, update them accordingly
df_selected = df[["Silahkan Isi Data Anda !", "Kelas"]]

# Streamlit application layout
st.title("Pendaftar Villanations V3 LabTI")

# Display the selected dataframe in the Streamlit app
st.dataframe(df_selected, use_container_width=True)

# Optional: Data Visualization Example
st.write("Data Visualization Example:")

# Plot a countplot for 'Kelas'
plt.figure(figsize=(10, 6))
sns.countplot(x='Kelas', data=df_selected)
st.pyplot(plt)
