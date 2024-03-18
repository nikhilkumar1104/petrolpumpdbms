import streamlit as st
from database import *
from database import view_only_Owner_id, add_Petrolpump_data
import pandas as pd

########################################################################################


def create_for_Petrolpump():
    try:
        # Fetching Owner_id values from the Owners table
        owner_ids = view_only_Owner_id()
    except Exception as e:
        logging.error("Error fetching Owner_id values: %s", e)
        owner_ids = []

    with st.container():
        Registration_No = st.text_input("Registration_No:")
        
        # Adding scroll option for selecting Owner_id
        selected_owner_id = st.selectbox("Owner_id", owner_ids)
        Petrolpump_Name = st.text_input("Petrolpump_Name:")
        Company_Name = st.text_input("Company_Name:")
        Opening_Year = st.number_input("Opening_Year:", step=1)
        State = st.text_input("State:")
        City = st.text_input("City:")
    
    if st.button("Add Petrolpump Details"):
        try:
            # Adding the selected Owner_id to the Petrolpump form
            add_Petrolpump_data(Registration_No, selected_owner_id, Petrolpump_Name, Company_Name,  Opening_Year, State, City)
            st.success("Successfully added Petrolpump details: {}".format(Registration_No))
        except Exception as e:
            logging.error("Error adding Petrolpump details: %s", e)
            st.error("Error adding Petrolpump details. Please try again.")

###############################################################################

def create_for_Owners():
    with st.container():
        Owner_id = st.text_input("Owner_id")
        Owner_Name = st.text_input("Owner_Name:")
        Contact_NO = st.text_input("Contact_NO:")
        DOB = st.date_input("DOB:")
        Gender = st.text_input("Gender:")
        Address = st.text_input("Enter Address")
       
        
    if st.button("Add Owners Details"):
        add_Owners_data(Owner_id,Owner_Name, Contact_NO, DOB, Gender, Address)
        st.success("Successfully added Owners details: {}".format(Owner_Name))
        
        
#################################################################################################

def create_for_Employee():
    with st.container():
        Employee_ID = st.text_input("Employee_ID")
        Emp_Name = st.text_input("Emp_Name:")
        Emp_Gender = st.text_input("Emp_Gender:")
        Designation = st.text_input("Designation:")
        DOB = st.date_input("DOB:")
        Salary = st.number_input("Salary:", step=1)
        Emp_Address = st.text_input("Emp_Address:")
        Email_ID = st.text_input("Email_ID:")
        epp_no = st.text_input("epp_no:")
        Manager_ID = st.text_input("Manager_ID (optional):")

    if st.button("Add Employee Details"):
        # Check if the petrol pump number exists
        if is_valid_petrolpump(epp_no):
            # Check if the manager exists and belongs to the same petrol pump
            if (not Manager_ID or (Manager_ID and is_valid_employee(Manager_ID) and get_employee_epp_no(Manager_ID) == epp_no)):
                # Check if manager's salary is higher than or equal to the employee's salary
                if not Manager_ID or (Manager_ID and get_employee_salary(Manager_ID) >= Salary):
                    # Add Employee data
                    add_Employee_data(Employee_ID, Emp_Name, Emp_Gender, Designation, DOB, Salary, Emp_Address, Email_ID, epp_no, Manager_ID)
                    st.success("Successfully added Employee details: {}".format(Employee_ID))
                else:
                    st.error("Employee's salary cannot be higher than manager's salary.")
            else:
                st.error("Manager with ID '{}' either does not exist or does not belong to the same petrol pump.".format(Manager_ID))
        else:
            st.error("Petrol pump number '{}' does not exist.".format(epp_no))




#######################################################################################################

def create_for_Customer():
    with st.container():
        Customer_Code = st.text_input("Customer_Code")
        C_Name = st.text_input("C_Name:")
        Phone_No = st.text_input("Phone_No:")
        Email_ID=st.text_input("Email_ID")
        Gender = st.text_input("Gender:")
        City = st.text_input("City:")
        Age = st.number_input("Age",step=1)
    
    if st.button("Add Customer Details"):
        add_Customer_data(Customer_Code , C_Name , Phone_No  , Email_ID , Gender,  City , Age)
        st.success("Successfully added Customer details: {}".format(Customer_Code))


########################################################################################################

def create_for_Invoice(): 
    with st.container():
        Invoice_No = st.text_input("Invoice_No:")
        Date = st.date_input("Date:")
        Payment_Type = st.text_input("Payment_Type:")
        Fuel_in_liters = st.number_input("Fuel_in_Liters:")
        Fuel_Type = st.text_input("Fuel_Type:")
        Discount = st.number_input("Discount (%):")
        Total_Price = st.number_input("Total_Amount:")
        Customer_Code = st.text_input("Customer_Code:")
        ipp_no = st.text_input("ipp_no:")
        
    if st.button("Add Invoice Details"):
        discounted_price = apply_discount(Total_Price, Discount)
        add_Invoice_data(Invoice_No, Date, Payment_Type, Fuel_in_liters, Fuel_Type, Discount, discounted_price, Customer_Code, ipp_no)
        st.success("Successfully added Invoice details: {}".format(Invoice_No))
        
        # Display discounted total price in a separate table
        discounted_total_table = pd.DataFrame({"Discounted Total Price": [discounted_price]})
        st.table(discounted_total_table)


##############################################################################################################


def create_for_Tanker():
    with st.container():
        Tanker_ID = st.text_input("Tanker_ID:")
        Capacity = st.number_input("Capacity:")
        pressure = st.number_input("pressure:")
        Fuel_ID = st.text_input("Fuel_ID")
        Fuel_Amount = st.number_input("Fuel_Amount")
        Fuel_Name = st.text_input("Fuel_Name:")
        Fuel_Price = st.number_input("Fuel_Price:")
        tpp_no = st.text_input("tpp_no:")
        
    if st.button("Add Tanker Details"):
        # Check if the petrol pump number exists
        if is_valid_petrolpump(tpp_no):
            # Add Tanker data
            add_Tanker_data(Tanker_ID, Capacity, pressure, Fuel_ID, Fuel_Amount, Fuel_Name, Fuel_Price, tpp_no)
            st.success("Successfully added Tanker details: {}".format(Tanker_ID))
        else:
            st.error("Petrol pump number '{}' does not exist.".format(tpp_no))



