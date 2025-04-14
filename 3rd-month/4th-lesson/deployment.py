import pandas as pd
import streamlit as st
from joblib import load
from sklearn.metrics import accuracy_score

model = load('song_popularity.joblib')

try:
  x_test=pd.read_csv('song_x_test.csv')
  y_test=pd.read_csv('song_y_test.csv')
  y_test=y_test.squeeze()
  show_accuracy=True
except:
  show_accuracy=False

st.set_page_config(page_title='Song popularity prediction model', layout='centered')
st.title('Song popularity')
st.markdown('Enter charactersitcs of the song and see how is the popularity of that song using our model.')

song_name = st.text_input('Song name')
song_duration_ms = st.number_input('Song duration', min_value=0.0, max_value=1000.0, value=300.0)
acousticness = st.number_input('Acousticness level', min_value=0.0, max_value=100.0)
danceability = st.number_input('Danceability level', min_value=0.0, max_value=100.0)
energy = st.number_input('Energy level', min_value=0.0, max_value=100.0)
instrumentalness = st.number_input('Instrumentalness level', min_value=0.0, max_value=100.0)
liveness = st.number_input('Liveness level', min_value=0.0, max_value=100.0)
loudness = st.number_input('Loudness level', min_value=00.0, max_value=60.0)
speechiness = st.number_input('Speechiness level', min_value=0.0, max_value=100.0)
tempo = st.number_input('Tempo level', min_value=50.0, max_value=200.0)
audio_valence = st.number_input('Audio_valence level', min_value=0.0, max_value=100.0)

if st.button('Predict the popularity of the song :)'):
  input_date=pd.DataFrame([{
    'song_name': song_name,
    'song_duration_ms': song_duration_ms,
    'acousticness': acousticness,
    'danceability': danceability,
    'energy': energy,
    'instrumentalness': instrumentalness,
    'liveness': liveness,
    'loudness': loudness,
    'speechiness': speechiness,
    'tempo': tempo,
    'audio_valence': audio_valence,
  }])

  
  prediction = model.predict(input_data)[0]
  st.success(f"Predicted song popularity score: {prediction: .2}")

if show_accuracy:
        from sklearn.metrics import mean_squared_error, r2_score

        y_pred = model.predict(x_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        st.metric('Test R² score:', f"{r2:.2f}")
        st.metric('Test MSE:', f"{mse:.2f}")
else:
        st.info('Test data not available to evaluate the model.')