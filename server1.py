import streamlit as st
import pickle

print('Successfully executed ')

model = pickle.load(open('model.pkl', 'rb'))

def predict(gender, senior_citizen, partner, dependents, tenure_months, phone_service,multiple_lines, 
            online_security, online_backup, device_protection,tech_support, streaming_tv, streaming_movies, 
            paperless_billing, monthly_charges, total_charges, payment_method_credit_card,
            payment_method_electronic_check, payment_method_mailed_check,contract_one_year, 
            contract_two_year, internet_services_dsl, internet_service_fibre):
    #step 5: make the predictions based on passed data
    prediction=model.predict([[gender, senior_citizen, partner, dependents, tenure_months, phone_service,
                               multiple_lines,online_security, online_backup, device_protection,
                               tech_support, streaming_tv, streaming_movies, paperless_billing, 
                               monthly_charges, total_charges, payment_method_credit_card,
                               payment_method_electronic_check, payment_method_mailed_check,contract_one_year, 
                               contract_two_year, internet_services_dsl, internet_service_fibre]])
    if prediction == 0:
        return 'Customer will NOT Churn'
    else:
        return 'CUSTOMER WILL CHURN. TAKE... '
    
def main():
    st.title("Telecom Churn Prediction")
    html_temp = """
    <div style="background-color:Black;padding:20px">
    <h2 style="color:white;text-align:center;">Streamlit Telecom Churn Predictor </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.sidebar.title("Customer's Data")
    # Categorical and binary variables
    var_gender = ("Male", "Female")
    var_bool = ("Yes", "No")
    #var_multiple = ("Yes", "Not", "No phone service")
    var_internet = ("DSL", "Fiber optic", "No")
    var_contract = ("Month-to-month", "One year", "Two year")
    var_payment_m = ("Credit card (automatic)", "Bank transfer (automatic)", "Electronic check", "Mailed check")

    #step 1: we read all the data here
    gender = st.sidebar.selectbox("Customer's Gender", var_gender)
    senior_citizen = st.sidebar.selectbox("Are you a Senior Citizen?", var_bool)
    partner = st.sidebar.selectbox("Partner", var_bool)
    dependents = st.sidebar.selectbox("Does the customer live with any dependents(children, parents, etc.)?", var_bool)
    phone_service = st.sidebar.selectbox("Does the customer have a phone service?", var_bool)
    multiple_lines = st.sidebar.selectbox("Does the customer have multiple telephone line services?", var_bool)
    internet_services = st.sidebar.selectbox("Does the customer have multiple Internet line services?", var_internet)
    online_security = st.sidebar.selectbox("Does the customer have online security service?", var_bool)
    online_backup = st.sidebar.selectbox("Does the customer have online backup service?", var_bool)
    device_protection = st.sidebar.selectbox("Does the customer have device protection service?", var_bool)
    tech_support = st.sidebar.selectbox("Does the customer have tech support service?", var_bool)
    streaming_tv = st.sidebar.selectbox("Does the customer have streaming tv service?", var_bool)
    streaming_movies = st.sidebar.selectbox("Does the customer have streaming movies service?", var_bool)
    contract = st.sidebar.selectbox("Which customer's current contract type?", var_contract)
    paperless_billing = st.sidebar.selectbox("Paperless billing", var_bool)
    payment_method = st.sidebar.selectbox("Payment method", var_payment_m)

    # Numerical variables
    tenure_months = st.sidebar.number_input("Tenure Months", min_value = 0, max_value = 200)
    total_charges = st.sidebar.number_input("Total Charges")
    monthly_charges = st.sidebar.number_input("Monthly Charges")
    #cltv = st.sidebar.number_input("Customer Lifetime Value(CLTV)")
    
    #step3: functions to change the category as per requirements of the model
    # Binary variables
    def create_binary(content):
        if content == "Male":
            content = 1
        elif content == "Female":
            content = 0
        elif content == "Yes":
            content = 1
        elif content == "No":
            content = 0
        return content

    # Covert Multiple Lines, Online Security, Online Backup, Device Protection, Tech Support, Streaming TV and Streaming Movies
    # def convert_muliples_var(content):
    #     if content == "No phone service":
    #         content = 1
    #     elif content == "Not":
    #         content = 0
    #     elif content == "Yes":
    #         content = 2
    #     return content

    def convert_internet_ser(content):
        if content == "Fiber optic":
            internet_service_fibre = 1
            internet_services_dsl = 0
        elif content == "DSL":
            internet_service_fibre = 0
            internet_services_dsl = 1
        elif content == "No":
            internet_service_fibre = 0
            internet_services_dsl = 0
        return internet_service_fibre, internet_services_dsl

    def convert_contract(content):
        if content == "One year":
            contract_one_year = 1
            contract_two_year = 0
        elif content == "Month-to-month":
            contract_one_year = 0
            contract_two_year = 0
        elif content == "Two year":
            contract_one_year = 0
            contract_two_year = 1
        return contract_one_year, contract_two_year

    def convert_payment_method(content):
        payment_method_credit_card = 0
        payment_method_electronic_check = 0
        payment_method_mailed_check = 0
        if content == "Credit card":
            payment_method_credit_card = 1
            payment_method_electronic_check = 0
            payment_method_mailed_check = 0
        elif content == "Bank transfer":
            payment_method_credit_card = 0
            payment_method_electronic_check = 0
            payment_method_mailed_check = 0
        elif content == "Electronic check":
            payment_method_credit_card = 0
            payment_method_electronic_check = 1
            payment_method_mailed_check = 0
        elif content == "Mailed check":
            payment_method_credit_card = 0
            payment_method_electronic_check = 0
            payment_method_mailed_check = 1
        return payment_method_credit_card, payment_method_electronic_check, payment_method_mailed_check
    
    #step2: convert the data into the required format of the model. ie convert category to binary
    gender = create_binary(gender)
    senior_citizen = create_binary(senior_citizen)
    partner = create_binary(partner)
    dependents = create_binary(dependents)
    tenure_months=tenure_months
    phone_service=create_binary(phone_service)
    multiple_lines = create_binary(multiple_lines)
    internet_service_fibre, internet_services_dsl = convert_internet_ser(internet_services)
    online_security = create_binary(online_security)
    online_backup = create_binary(online_backup)
    device_protection = create_binary(device_protection)
    tech_support = create_binary(tech_support)
    streaming_tv= create_binary(streaming_tv)
    streaming_movies = create_binary(streaming_movies)
    contract_one_year, contract_two_year = convert_contract(contract)
    paperless_billing = create_binary(paperless_billing)
    payment_method_credit_card, payment_method_electronic_check, payment_method_mailed_check = convert_payment_method(payment_method)
    monthly_charges=monthly_charges
    total_charges=total_charges

    result=""
    #step4: pass the created the data to the model.
    if st.button("Predict"):
        result=predict(gender, senior_citizen, partner, dependents, tenure_months, phone_service, 
                       multiple_lines, online_security, online_backup, device_protection, 
                       tech_support, streaming_tv, streaming_movies, paperless_billing, 
                       monthly_charges, total_charges, 
                       payment_method_credit_card,payment_method_electronic_check, payment_method_mailed_check,
                       contract_one_year, contract_two_year, internet_services_dsl, internet_service_fibre)
        st.success('You Have {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")
        st.text('Created By MEEEEE')
main()