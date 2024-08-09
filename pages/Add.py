import streamlit as st
import pandas as pd



def load_data(file_path):
    df = pd.read_excel(file_path)
    return df

# Save the updated DataFrame back to the Excel file
def save_data(df, file_path):
    df.to_excel(file_path, index=False)

file_path = "C:/PythonScripting/MyCode/demo/NewDesktopand.xlsx"

data = load_data(file_path)


def centered_text(text, font_size=None, color=None):
    style = "text-align: center;"
    if font_size:
        style += f" font-size: {font_size};"
    if color:
        style += f" color: {color};"
    return f"<div style='{style}'>{text}</div>"

st.markdown(centered_text("<h1 style='color : #37D2DC'>ADD NEW ASSET</h1>"), unsafe_allow_html=True)

st.divider()
st.subheader("FILL THE ASSET DETAILS BELOW :")
st.divider()
#st.markdown("<h3 style='color : cyan'>USER DETAILS :</h3>", unsafe_allow_html=True)
ex = st.text_input("Enter the User ID receiving the asset :")
if ex not in data['UID'].values and len(ex)>1:
    st.error("User ID not found.")
if ex in data['UID'].values:
    usd = data[data["UID"] == ex]
    emp = usd['Employee Name'].values[0]
    depart = usd['Department'].values[0]
    ao = usd['Asset Owner'].values[0]
    locat = usd['Location'].values[0]
    st.subheader("User Details:")
    st.write(f"Name: {emp}")
    st.write(f"Department: {depart}")
    st.write(f"Owner: {ao}")
    st.write(f"Location: {locat}")
#col1, col2, col3 = st.columns(3)
#with col1:

 #   u_id = st.text_input("USER ID :")
  #  dept = st.text_input("DEPARTMENT :")

#with col2:

 #   emp_name = st.text_input("EMPLOYEE NAME :")

  #  status = st.text_input("STATUS :")

#with col3:

 #   location = st.text_input("LOCATION :")


#st.divider()
#with col1:
 #   st.divider()
  #  st.write("  ")
  #  st.write("Enter UID to use Autofill")
  #  submittt=  st.button("Autofill", type = "primary")

  #  user_dept = st.session_state.get('user_dept', 'YOLO')  # Default to 'YOLO' if no department info is found

   # if submittt:
    #    user_data = data[data["UID"] == u_id]
     #   if not user_data.empty:
      #      emp_name = user_data['Employee Name'].values[0]
       #     status = user_data['Status'].values[0]
        #    dept = user_data['Department'].values[0]
         #   location = user_data['Location'].values[0]
          #  st.write(f"Name: {emp_name}")
           # st.write(f"Department: {dept}")
            #st.write(f"Status: {status}")
            #st.write(f"Location: {location}")

st.markdown("<h3 style='color : cyan'>ASSET DETAILS :</h3>", unsafe_allow_html=True)




col4, col5, col6 = st.columns(3)
with col4:
    Asset_type = st.text_input("ASSET TYPE :")
    comp_name = st.text_input("COMPUTER NUMBER:")
    comp_model = st.text_input("DEVICE MODEL: ")

    purchase_no = st.text_input("PURCHASE NUMBER :")
    vendor_name = st.text_input("VENDOR :")


with col5:
    brand = st.text_input("BRAND NAME :")
    serial = st.text_input("SERIAL NO. :")
    invoice_no = st.text_input("INVOICE NUMBER :")
    warranty_date = st.date_input("WARRANTY END DATE :")
    year_month = warranty_date.year

    pa_desc = st.text_input("PA DESC:")
with col6:
    stat = st.text_input("STATUS : ")

    mac_add = st.text_input("MAC ADDRESS :")
    invoice_date = st.date_input("INVOICE DATE :")

    asset_cost = st.number_input("ASSET COST :")
    Asset_assetOwner = st.text_input("Asset_assetOwner :")
st.divider()
with col5:
    submitt = st.button("ADD ASSET", type="primary", use_container_width=True)

    user_dept = st.session_state.get('user_dept', 'YOLO')  # Default to 'YOLO' if no department info is found

    if submitt:
        new_row = pd.DataFrame(
                {'Status': [stat], 'UID': [ex], 'Employee name': [emp], 'Employee Name': [emp],
                 'PA Desc': [pa_desc], 'Asset Owner': [ao], 'Asset_assetOwner': [Asset_assetOwner],
                 'Asset Type': [Asset_type], 'Computer Name ': [comp_name], 'Brand ': [brand],
                 'Current Model': [comp_model], 'Serial ': [serial], 'Location': [locat],
                 'Purchase Number': [purchase_no], 'Invoice Number': [invoice_no], 'Invoice Date': [invoice_date],
                 'Warranty end': [warranty_date], 'year_Month': [year_month], 'Vendor name': [vendor_name],
                 'ASSET COST': [asset_cost], 'MAC address-wireless': [mac_add], 'Department': [depart]})
        if depart == user_dept or user_dept == 'YOLO':

                # Append the new row to the DataFrame
            data = pd.concat([data, new_row], ignore_index=True)

                # Save the updated DataFrame back to the Excel file
            save_data(data, file_path)

            st.success("Row added successfully!")

        else:
            st.error("Not Authorized for this Department")
