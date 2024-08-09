import streamlit as st
import pandas as pd

def centered_text(text, font_size=None, color=None):
    style = "text-align: center;"
    if font_size:
        style += f" font-size: {font_size};"
    if color:
        style += f" color: {color};"
    return f"<div style='{style}'>{text}</div>"



file_path = "C:/PythonScripting/MyCode/demo/NewDesktopand.xlsx"
df = pd.read_excel(file_path)
def save_data(df, file_path):
    df.to_excel(file_path, index=False)
# Assuming the department info is already saved in session state
user_dept = st.session_state.get('user_dept', 'YOLO')  # Default to 'YOLO' if no department info is found

st.markdown(centered_text("<h1 style='color : #37D2DC'>DELETE AN ASSET</h1>"), unsafe_allow_html=True)

st.subheader("Enter Required Details for Deletion :")

user_id = st.text_input("ENTER THE  UID :")

# Search for the user in the DataFrame
search_result = df[(df['UID'] == user_id) ]

if user_id not in df['UID'].values and len(user_id)>1:
    st.error("User ID not found")
if not search_result.empty:

        st.success("User found")
        st.write(search_result)
        st.write("Are you sure you want to delete this record?")
        del1 = st.button("Confirm Delete", type="primary")
        if del1:
            df = df[df['UID'] != user_id]

            save_data(df, file_path)
            st.success("Successfully Deleted !")



