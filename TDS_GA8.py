import streamlit as st

a = st.number_input(int(input("First Number")))
b = st.number_input(int(input("Second Number")))
c = st.number_input(int(input("Third Number")))


if (a >= b) and (a >= c):
	l = a

elif (b >= a) and (b >= c):
	l = b

elif (c >= a) and (c >= b):
	l = c

st.write("Largest Number", l)