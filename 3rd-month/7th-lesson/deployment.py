import pandas as pd
import streamlit as st
from joblib import load
from sklearn.metrics import accuracy_score

model = load('electricty.joblib')
