import streamlit as st, pandas as pd
from database.connection import conectar
st.title("📊 Dashboard")
conn=conectar()
try:
 a=pd.read_sql('select * from agendamentos',conn)
 st.metric('Agendamentos',len(a))
except: st.write('Sem dados')
