import streamlit as st
import pandas as pd

import nekt

nekt.data_access_token = st.secrets["DATA_ACCESS_TOKEN"]

try:
    cidades_df = nekt.load_table(layer_name="Raw", table_name="cidades").toPandas()
    st.write(cidades_df)  
    st.write("Dataframe loaded successfully!")
except Exception as e:
    st.error(f"Error loading data: {e}")

########

st.title("🎈 My new app")