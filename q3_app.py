import streamlit as st
import numpy as np
import pandas as pd
import pickle

### use: streamlit run q3_app.py

### load the prediction model

model_filename = 'models/best_model.pkl' 
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

st.title('Failure Prediction Model')

### input data

st.header('Enter each input features:')
air_temp = st.number_input('Air temperature [K]', value=298.1)
process_temp = st.number_input('Process temperature [K]', value=308.6)
rot_speed = st.number_input('Rotational speed [rpm]', value=1551)
torque = st.number_input('Torque [Nm]', value=42.8)
tool_wear = st.number_input('Tool wear [min]', value=0.0)

twf = st.selectbox('TWF (Tool Wear Failure)', [0, 1])
hdf = st.selectbox('HDF (Heat Dissipation Failure)', [0, 1])
pwf = st.selectbox('PWF (Power Failure)', [0, 1])
osf = st.selectbox('OSF (Overstrain Failure)', [0, 1])


if st.button('Predict'):

    input_data = np.array([[air_temp, process_temp, rot_speed, torque, tool_wear, twf, hdf, pwf, osf]])
    prediction = model.predict(input_data)
    st.write(f'The predicted output is: {prediction[0]}')

### Batch Job via file upload

st.header('Use the Prediction Model')

up_file = st.file_uploader('Upload Test csv File', type=["csv"])

if up_file is not None:
    # Convert uploaded file to dataframe
    df = pd.read_csv(up_file)
#   df = pd.read_csv(up_file, header=None)

    st.write("### Preview of Data")
    st.dataframe(df)  

st.write("### Prediction Result")

# preprocessing

df = df.drop(["UDI", "Product ID"], axis=1)
df = pd.get_dummies(df, "Type")
X = df.drop(columns=['Machine failure', 'RNF', 'Type_H', 'Type_L', 'Type_M'])


prediction = model.predict(X)
# st.write(f'The predicted output is: {prediction}')
# df['pred']= prediction
st.write(prediction)
