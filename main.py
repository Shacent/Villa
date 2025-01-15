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

engine = create_engine(SUPABASE_DATABASE_URL)

df = pd.read_sql_table(table_name="Villa", con=engine.connect())

df_selected = df[["Silahkan Isi Data Anda !", "Kelas"]]

st.title("Pendaftar Villanations V3 LabTI")
st.dataframe(df_selected,use_container_width=True)
