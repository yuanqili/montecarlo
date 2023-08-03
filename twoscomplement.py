import streamlit as st


def twos_complement(n, bits):
    if n < 0:
        n = (1 << bits) + n
    return bin(n)[2:].zfill(bits)


st.header('Two\'s complement converter')

bits = st.number_input('Number of bits', value=8, min_value=1, max_value=64, step=1)
number = st.number_input('The number to be converted', value=-42, step=1)
complement = twos_complement(number, bits)

st.caption('Your number in two\'s complement is')
st.success(f'{complement}')
