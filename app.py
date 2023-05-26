import pandas as pd
import pickle
import streamlit as st

# Load the trained model
model = pickle.load(open('model.sav', "rb"))

df_1 = pd.read_csv('first_telc.csv')

def main():
    st.title('Customer Churn Prediction')
    st.markdown('Enter the customer details:')
    
    # Create a form to input customer details
    input_query = {}
    input_query['SeniorCitizen'] = st.selectbox('Senior Citizen:', ['No', 'Yes'])
    input_query['MonthlyCharges'] = st.number_input('Monthly Charges:')
    input_query['TotalCharges'] = st.number_input('Total Charges:')
    input_query['gender'] = st.selectbox('Gender:', ['Female', 'Male'])
    input_query['Partner'] = st.selectbox('Partner:', ['No', 'Yes'])
    input_query['Dependents'] = st.selectbox('Dependents:', ['No', 'Yes'])
    input_query['PhoneService'] = st.selectbox('Phone Service:', ['No', 'Yes'])
    input_query['MultipleLines'] = st.selectbox('Multiple Lines:', ['No', 'Yes', 'No phone service'])
    input_query['InternetService'] = st.selectbox('Internet Service:', ['No', 'DSL', 'Fiber optic'])
    input_query['OnlineSecurity'] = st.selectbox('Online Security:', ['No', 'Yes', 'No internet service'])
    input_query['OnlineBackup'] = st.selectbox('Online Backup:', ['No', 'Yes', 'No internet service'])
    input_query['DeviceProtection'] = st.selectbox('Device Protection:', ['No', 'Yes', 'No internet service'])
    input_query['TechSupport'] = st.selectbox('Tech Support:', ['No', 'Yes', 'No internet service'])
    input_query['StreamingTV'] = st.selectbox('Streaming TV:', ['No', 'Yes', 'No internet service'])
    input_query['StreamingMovies'] = st.selectbox('Streaming Movies:', ['No', 'Yes', 'No internet service'])
    input_query['Contract'] = st.selectbox('Contract:', ['Month-to-month', 'One year', 'Two year'])
    input_query['PaperlessBilling'] = st.selectbox('Paperless Billing:', ['No', 'Yes'])
    input_query['PaymentMethod'] = st.selectbox('Payment Method:', ['Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check'])
    input_query['tenure'] = st.number_input('Tenure (months):')
    
    if st.button('Predict Churn'):
        # Create a DataFrame with the input values
        new_df = pd.DataFrame([input_query])
        
        # Concatenate the new_df with the original DataFrame
        df_2 = pd.concat([df_1, new_df], ignore_index=True)
        
        # Perform data preprocessing steps
        labels = ["{0} - {1}".format(i, i + 11) for i in range(1, 72, 12)]
        df_2['tenure_group'] = pd.cut(df_2['tenure'].astype(int), range(1, 80, 12), right=False, labels=labels)
        
        # Perform one-hot encoding
        new_df_dummies = pd.get_dummies(df_2[['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService',
                                               'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                                               'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
                                               'Contract', 'PaperlessBilling', 'PaymentMethod', 'tenure_group']])
        
        # Predict using the trained model
        prediction = model.predict(new_df_dummies.tail(1))
        probability = model.predict_proba(new_df_dummies.tail(1))[:, 1]
        
        if prediction == 1:
            output1 = "This customer is likely to be churned!"
        else:
            output1 = "This customer is likely to continue!"
        
        output2 = "Confidence: {}%".format(probability * 100)
        
        # Display the prediction result
        st.markdown('**Churn Prediction Result:**')
        st.write(output1)
        st.write(output2)

if __name__ == "__main__":
    main()
