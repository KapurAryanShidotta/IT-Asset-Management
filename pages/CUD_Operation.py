import streamlit as st
from streamlit_navigation_bar import st_navbar


user_dept = st.session_state.get('user_dept', 'YOLO')  # Default to 'YOLO' if no department info is found

def centered_text(text, font_size=None, color=None):
    style = "text-align: center;"
    if font_size:
        style += f" font-size: {font_size};"
    if color:
        style += f" color: {color};"
    return f"<div style='{style}'>{text}</div>"


page = st_navbar(["HOME", "ADD", "READ", "UPDATE", "DELETE"])

if page == "HOME":
    st.switch_page("pages/HOME.py")
if page == "ADD":
    st.switch_page("pages/Add.py")
if page == "READ":
    st.switch_page("pages/Read.py")
if page == "UPDATE":
    st.switch_page("pages/Update.py")
if page == "DELETE":
    st.switch_page("pages/delete.py")



st.markdown(centered_text("<h1 style= 'color : #37D2DC'>C.R.U.D. Operations 💻 </h1>"), unsafe_allow_html=True)
st.divider()

st.markdown(
        centered_text(
            "<p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu.</p>",
            color="darkgrey", font_size="16px"
        ),
        unsafe_allow_html=True
    )
st.divider()
col1, col2, col3, col4 = st.columns(4)


with col1:
    if st.button("ADD ASSET", help="Add", type="primary", use_container_width=True):
        if user_dept == 'YOLO':
            st.switch_page("pages/Add.py")
        else:
            st.error("Not Authorized")
    st.markdown(
        centered_text(
            "<p>Add a new asset info into the dataset.</p>",
            color="darkgrey", font_size="16px"
        ),
        unsafe_allow_html=True
    )



with col2:
    if st.button("READ ASSET", help="Read", type="primary", use_container_width=True):
         st.switch_page("pages/Read.py")

    st.markdown(
        centered_text(
            "<p>Get info of asset(s) from the dataset.</p>",
            color="darkgrey", font_size="16px"
        ),
        unsafe_allow_html=True
    )
with col3:
    if st.button("UPDATE ASSET", help="Update", type="primary", use_container_width=True):
        if user_dept == 'YOLO':
            st.switch_page("pages/Update.py")
        else:
            st.error("Not Authorized")
    st.markdown(
        centered_text(
            "<p>Make changes to details of a specific asset in the dataset.</p>",
            color="darkgrey", font_size="16px"
        ),
        unsafe_allow_html=True
    )
with col4:
    if st.button("DELETE ASSET", help="Delete", type="primary", use_container_width=True):
        st.switch_page("pages/delete.py")
    st.markdown(
        centered_text(
            "<p>Delete an asset from the dataset.</p>",
            color="darkgrey", font_size="16px"
        ),
        unsafe_allow_html=True
    )

#if 'page' not in st.session_state:
#    st.session_state.page = "crud"

#if st.session_state.page == "page1.py":
#    st.switch_page("page1.py")
