import streamlit as st
from streamlit_navigation_bar import st_navbar


def navigate_to(page):
    st.session_state.page = page


def centered_text(text, font_size=None, color=None):
    style = "text-align: center;"
    if font_size:
        style += f" font-size: {font_size};"
    if color:
        style += f" color: {color};"
    return f"<div style='{style}'>{text}</div>"

page = st_navbar(["Home", "CRUD Ops", "Asset Dashboard"])

if page == "CRUD Ops":
    st.switch_page("pages/CUD_Operation.py")
if page == "Asset Dashboard":
    st.switch_page("pages/demo99.py")
if page == "Home":
    st.switch_page("pages/HOME.py")


st.markdown(centered_text("<h1 style= 'color : #37D2DC'>IT ASSET MANAGEMENT 💻 </h1>"), unsafe_allow_html=True)
st.divider()

st.markdown(centered_text("<h3>Welcome!</h3>"),unsafe_allow_html=True)
st.markdown(
    centered_text(
        "<p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.</p>",
        color="darkgrey", font_size="16px"
        ),
        unsafe_allow_html=True
    )
st.divider()

#st.markdown(centered_text("<h3>What is the purpose of your visit?</h3>"),unsafe_allow_html=True)
#st.markdown('#')
#col1, col2, col3, col4 = st.columns(4)


#with col1:
    # st.button("XXXXX",type= "primary", use_container_width=True)
        #st.switch_page("Read.py")

#with col2:
 ##   if st.button("C.R.U.D. Operations", type= "primary", use_container_width=True):
   #     st.switch_page("pages/CUD_Operation.py")

#with col3:
#    if st.button("POWER BI VIZ",type= "primary", use_container_width=True):
#        st.switch_page("pages/demo99.py")

#with col4:
#   st.button("EMPTY2",type= "primary", use_container_width=True)