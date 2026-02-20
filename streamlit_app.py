import streamlit as st

import nekt
nekt.data_access_token = st.secrets["DATA_ACCESS_TOKEN"]

st.title("Connect your app with Nekt 👩🏼‍💻")

try:
    cidades_df = nekt.load_table(layer_name="Raw", table_name="cidades").select("id", "nome")
    print("Dataframe loaded successfully!")
except Exception as e:
    print(f"Error loading data: {e}")

st.write(f"Total de cidades: {cidades_df.count()}")
st.write(cidades_df.toPandas().head(10))