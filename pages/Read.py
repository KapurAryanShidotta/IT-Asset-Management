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

st.markdown(centered_text("<h1 style='color : #37D2DC'>VIEW DATASET</h1>"), unsafe_allow_html=True)

def display_excel(file_path, user_dept):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Filter the DataFrame based on department
    if user_dept != "YOLO":
        if 'Department' in df.columns:
            df = df[df['Department'].astype(str).str.strip() == user_dept]


    for i in range(len(filter1)):
        var = filter1[i]
        if 'Asset Owner' in df.columns:
            df = df[df['Asset Owner'].astype(str).str.strip() == var]


    for i in range(len(filter2)):
        var = filter2[i]
        if 'Current Model' in df.columns:
            df = df[df['Current Model'].astype(str).str.strip() == var]


    for i in range(len(filter3)):
        var = filter3[i]
        if 'Vendor name' in df.columns:
            df = df[df['Vendor name'].astype(str).str.strip() == var]


    for i in range(len(filter4)):
        var = filter4[i]
        if 'Location' in df.columns:

            df = df[df['Location'].astype(str).str.strip() == var]


    st.dataframe(df, height=700)
file_path = "NewDesktopand.xlsx"

st.write("YOUR DEPARTMENT :", user_dept.upper())
st.write("SELECT FILTERS :")

col1, col2, col3, col4 = st.columns(4)

with col1:
    filter1 = st.multiselect(
    "Asset Owner :",
    ["SKI", "SKM", "Mandakini", "Tidong"]
    )

with col2:
    filter2 = st.multiselect(
        "Current Model :",
        ["T14s Gen 1", "T14 Gen 2","T14 Gen 3","T14 Gen 4", "T490s Gen 1", "Yoga X1 Gen 5","Yoga X1 Gen 8", "Surface Pro 9", "P16 Gen 1", "P5 workstation", "P51s", "Z6G4"  ]
    )
with col3:
    filter3 = st.multiselect(
        "Vendor :",
        ["PVR system", "EVOKE GLOBAL", "Team Computer", "SHREE IT SOLUTIONS", "TECH4LOGIC PRIVATE LIMITED", "TEAM COMPUTER PVT LTD", "PVR System Pvt Ltd"]
    )
with col4:
    filter4 = st.multiselect(
        "Location :",
        ["Delhi", "Tidong", "Bangalore", "Mandakini", "Rajasthan", "Shimla", "Mumbai", "Chennai", "Oslo", "UK", "Bhopal" ]
    )

# Check if the file path is valid
try:
    display_excel(file_path, user_dept)
except Exception as e:
    st.error(f"Error reading the Excel file: {e}")

