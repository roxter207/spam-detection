import pickle
import streamlit as st

model = pickle.load(open("spam.pickle", "rb"))
cv =pickle.load(open("vectorizer.pickle", "rb"))

def main():
    st.title("Email Spam Classification Apps")

main()