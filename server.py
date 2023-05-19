import streamlit as st 
import pickle

print('Successfully executed ')

model = pickle.load(open('model.pkl', 'rb'))

def predict(Glucose,Bp,Insulin,BMI):
    prediction=model.predict([[Glucose,Bp,Insulin,BMI]])
    if prediction == 0:
        return 'No Diabetes. Be happy ....'
    else:
        return 'Diabetes. Take Treatements....'
    
def main():
    st.title("Diabetes Prediction")
    html_temp = """
    <div style="background-color:Black;padding:20px">
    <h2 style="color:white;text-align:center;">Streamlit Diabetes Predictor </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Glucose = st.text_input("Glucose","Type Here")
    Bp = st.text_input("Bp","Type Here")
    Insulin = st.text_input("Insulin","Type Here")
    BMI = st.text_input("BMI","Type Here")
    result=""
    if st.button("Predict"):
        result=predict(Glucose,Bp,Insulin,BMI)
        st.success('You Have {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")
        st.text('Created By AJITH')
main()
