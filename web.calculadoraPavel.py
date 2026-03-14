import streamlit as st 


st.title("🚀 Mi Progreso: Calculadora de Pavel")
st.subheader("Proyecto #1 - Estudiante de Ingeniería")


col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Escribe el primer número:", value=0.0)

with col2:
    num2 = st.number_input("Escribe el segundo número:", value=0.0)

st.write("---") 

st.write("### Selecciona la operación:")
col_a, col_b, col_c, col_d = st.columns(4)

if col_a.button("Sumar ➕"):
    st.success(f"Resultado: {num1 + num2}")

if col_b.button("Restar ➖"):
    st.success(f"Resultado: {num1 - num2}")

if col_c.button("Multiplicar ✖️"):
    st.success(f"Resultado: {num1 * num2}")

if col_d.button("Dividir ➗"):
    if num2 != 0:
        st.success(f"Resultado: {num1 / num2}")
    else:
        st.error("No se puede dividir entre 0, jit")

st.write("---")
st.info("Hecho con Python y Streamlit por Pavel 🐍")