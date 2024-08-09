import streamlit as st
import pandas as pd

def centered_text(text, font_size=None, color=None):
    style = "text-align: center;"
    if font_size:
        style += f" font-size: {font_size};"
    if color:
        style += f" color: {color};"
    return f"<div style='{style}'>{text}</div>"





from streamlit_navigation_bar import st_navbar
#import pages as
page = st_navbar(["HOME", "CRUD", "VIZ"])

if page == "CRUD":
    st.switch_page("CRUD_Operation.py")
if page == "Page 2":
    st.switch_page("demo99.py")


#page = st_navbar(["HOME", "CUD_Operation", "delete", "Update", "Read"])
#st.write(page)



