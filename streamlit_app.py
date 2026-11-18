import streamlit as st
st.set_page_config(page_title="AgendaPro MVP", layout="wide")
st.title("AgendaPro MVP")
st.write("Sistema de Agendamento para Salões")

st.sidebar.title("Menu")
pagina = st.sidebar.selectbox("Escolha", ["Dashboard","Novo Agendamento"])

if pagina == "Dashboard":
    c1,c2,c3 = st.columns(3)
    c1.metric("Agendamentos Hoje", 12)
    c2.metric("Clientes", 85)
    c3.metric("Faturamento", "R$ 1.850")
else:
    st.subheader("Novo Agendamento")
    st.text_input("Nome")
    st.text_input("Telefone")
    st.selectbox("Serviço", ["Corte","Barba","Coloração","Manicure"])
    st.date_input("Data")
    st.selectbox("Horário", ["09:00","10:00","11:00","14:00","15:00"])
    st.button("Confirmar")
