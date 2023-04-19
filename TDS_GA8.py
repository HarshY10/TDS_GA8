!pip install -q streamlit
import streamlit as st


a = st.number_input("Enter first number ")
b = st.number_input("Enter second number ")
c = st.number_input("Enter third number ")

if (a >= b) and (a >= c):
	l = a

elif (b >= a) and (b >= c):
	l = b

elif (c >= a) and (c >= b):
	l = c

st.write("The largest number is ", l)
