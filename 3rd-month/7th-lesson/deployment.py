import pandas as pd
import streamlit as st
from joblib import load
from sklearn.metrics import accuracy_score

model = load('electricty.joblib')

try:
  x_test=pd.read_csv('4th-lesson/song_x_test.csv')
  y_test=pd.read_csv('4th-lesson/song_y_test.csv')
  y_test=y_test.squeeze()
  show_accuracy=True
except:
  show_accuracy=False

st.set_page_config(page_title='Fault detection in electricity', layout='centered')
st.title('Electrity fault detection')
st.markdown('Enter inputs of the electricty experience and get the result on whether there is a problem with the electricity using our model.')

Ia = st.number_input('Current in Phase A (Ia)', min_value=0.0, max_value=220.0)
Ib = st.number_input('Current in Phase B (Ib)', min_value=0.0, max_value=220.0)
Ic = st.number_input('Current in Phase C (Ic)', min_value=0.0, max_value=220.0)
Va = st.number_input('Voltage in Phase A (Va)', min_value=0.0, max_value=220.0)
Vb = st.number_input('Voltage in Phase B (Vb)', min_value=0.0, max_value=220.0)
Vc = st.number_input('Voltage in Phase C (Vc)', min_value=0.0, max_value=220.0)

if st.button('Detect the fault'):
  input_data = pd.DataFrame([{
    'Current in Phase A (Ia)': Ia,
    'Current in Phase B (Ib)': Ib,
    'Current in Phase C (Ic)': Ic,
    'Voltage in Phase A (Va)': Va,
    'Voltage in Phase B (Va)': Vb,
    'Voltage in Phase C (Vc)': Vc,
  }])

prediction = model.predict(input_data)[0]
st.success(f"Fault detection: {prediction:.2f}")

if show_accuracy:
  from sklearn.metrics import accuracy_score
  y_pred = model.predict(x_test)
  acc_score = accuracy_score(y_test, y_pred)
  st.metric('Accuracy score:', acc_score)
else:
  st.info('Test data not available to evaluate the model.')