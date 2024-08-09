import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Home Page",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed" )





def load_credentials():
    try:
        df = pd.read_csv("password1.csv")
        st.write("Loaded credentials:")
       # st.write(df)  # Log the contents of the CSV file for debugging
        return df
    except Exception as e:
        st.error(f"Error loading credentials: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error


# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'user_dept' not in st.session_state:
    st.session_state.user_dept = None


# Function to authenticate user
def authenticate(username2, password2):
    df = load_credentials()
    if df.empty:
        st.error("Credentials could not be loaded.")
        return

    df['username'] = df['username'].astype(str).str.strip()
    df['password'] = df['password'].astype(str).str.strip()
    df['depts'] = df['depts'].astype(str).str.strip()

    # Convert input values to strings
    username2 = str(username2).strip()
    password2 = str(password2).strip()

    # Filter the DataFrame to find matching username and password
    filtered_df = df[(df['username'] == username2) & (df['password'] == password2)]

    # Check if any rows were returned
    if not filtered_df.empty:
        st.session_state.authenticated = True
        st.session_state.user_dept = filtered_df['depts'].values[0]  # Save the department
        st.success("Successfully authenticated!")
    else:
        st.error("Invalid username or password")


# Login form
if not st.session_state.authenticated:
    st.title("Login")
    username2 = st.text_input("Username")
    password2 = st.text_input("Password", type="password")
    if st.button("Login"):
        authenticate(username2, password2)
        if st.session_state.authenticated == True:
            st.switch_page("pages/HOME.py")

