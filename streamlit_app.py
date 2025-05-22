import streamlit as st

st.title("blackiebooandcimot")
st.write(
    "hii welcome to wekidii, need help?"
)
st.image("haloo.jpg")

st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)
if (angka % 2) == 0:
    st.write(f"{angka}adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
