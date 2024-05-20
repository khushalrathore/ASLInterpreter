import streamlit as st
import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def main():
    st.title("Random Password Generator")

    base = ["ascii_letters", "digits", "punctuation"]
    random.shuffle(base)
    x1 = random.choice(base)
    x2 = random.choice(base)
    x3 = random.choice(base)

    st.write("Available character sets:", base)
    st.write(f"Selected sets: {x1}, {x2}, {x3}")

    length1 = st.slider("Select length for the first part of the password:", min_value=4, max_value=32, value=16)
    length2 = st.slider("Select length for the second part of the password:", min_value=4, max_value=32, value=16)
    length3 = st.slider("Select length for the third part of the password:", min_value=4, max_value=32, value=20)

    password = generate_password(length1) + "-" + generate_password(length2) + "-" + generate_password(length3)
    st.write("Generated Key:", password)
