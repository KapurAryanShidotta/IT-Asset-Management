import streamlit as st
import pandas as pd

def centered_text(text, font_size=None, color=None):
    style = "text-align: center;"
    if font_size:
        style += f" font-size: {font_size};"
    if color:
        style += f" color: {color};"
    return f"<div style='{style}'>{text}</div>"

# Assuming the department info is already saved in session state
user_dept = st.session_state.get('user_dept', 'YOLO')  # Default to 'YOLO' if no department info is found

st.markdown(centered_text("<h1 style='color : #37D2DC'>UPDATE ASSET INFO</h1>"), unsafe_allow_html=True)
file_path = "NewDesktopand.xlsx"
st.divider()
df = pd.read_excel(file_path)

st.subheader("Enter Required Details for Updating :")

user_id = st.text_input("ENTER THE  UID :")

        # Search for the user in the DataFrame
search_result = df[(df['UID'] == user_id) ]
def save_data(df, file_path):
    df.to_excel(file_path, index=False)
x = True
# Check if the user exists and display the result
if not search_result.empty:

        st.success("User found")
        st.write(search_result)
        change_col = st.text_input("What do you want to change ?")
        if change_col in df.columns:
            new_val = st.text_input("Enter the New Value :")
            if len(new_val) >0:
                if user_id in df['UID'].values:
                    df.loc[df['UID'] == user_id, change_col] = new_val

                    save_data(df, file_path)
                    st.success("successfully updated")
                    st.write("Updated Row :")
                    search_result = df[(df['UID'] == user_id)]
                    st.write(search_result)
                    x = False
                else:
                    st.error("not successfull")

#if not x:
#    st.button("More Changes")


#
#new_val = st.text_input("Enter the New Value :")
#if user_id in df['UID'].values:
#    df.loc[df['UID'] == user_id, change_col] = new_val

#    save_data(df, file_path)
 #   st.success("successfully updated")
#else:
 #   st.error("some error")