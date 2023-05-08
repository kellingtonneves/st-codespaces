"""Streamlit Codespaces Template"""

import streamlit as st
from streamlit_extras.switch_page_button import switch_page

def run():
    st.title("App Title")

    st.header("Header")
    st.subheader("Subheader")
    st.write("App Description Here.")
    st.markdown("""
        Text with a <a href="Subpage" target="_self">link</a> to a subpage.
    """, unsafe_allow_html=True)

    if st.button("Button to a subpage"):
        switch_page("Subpage")

    # st.header("What am I into to now?")
    # st.markdown("""
    #     If you're curious about what I've been exploring lately, then check my <a href="Now" target="_self">Now</a> page.
    # """, unsafe_allow_html=True)

    # if st.button("Tell me more!"):
    #     switch_page("Now")
    

# def about():
#     st.title("ABOUT")

if __name__ == "__main__":
    run()