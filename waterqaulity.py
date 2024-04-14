import streamlit as st
import pandas as pd
import pickle
import gzip
from joblib import load

 
  

def predict_portability1(model, ph,hardness,solids,cholarmine,sulfate,cond,carbon,turb,trihalome):
    input_features = [[ph,hardness,solids,cholarmine,sulfate,cond,carbon,turb,trihalome]]
    portability = model.predict(input_features)[0]
    return portability
def predict_portability2(model,Latitude,Longitude):
    input_features = [[Latitude,Longitude]]
    portability = model.predict(input_features)[0]
    return portability

def main():
 navigation_options = ['Welcome', 'water_quality', 'water_depth']

    # Create sidebar with navigation options
 page = st.sidebar.radio('Navigation', navigation_options)
 
  
 if page=='Welcome':
  st.title("welcome machine learning world ")
  st.image("machine.jpg")
  
 elif page=='water_quality':
  st.title("Water Quality prediction")
  st.subheader("Samples")
  df = pd.read_csv('water_potability.csv')
  for column in df.columns:
    if df[column].dtype in [int, float]:  # Only fill numeric columns
        mean_value = df[column].mean()  # Calculate mean of the column
        df[column].fillna(mean_value, inplace=True)
  top_3 = df.head(3)
  bottom_3 = df.tail(3)
 
  combined_df = pd.concat([top_3, bottom_3])

 
  st.dataframe(combined_df)
  
   
  ph = st.number_input("Enter ph:")
  hardness = st.number_input("Enter hardness:", min_value=0.0, step=0.1)
  solids = st.number_input("Enter solids:", min_value=0.0, step=0.1)
  cholarmine = st.number_input("Enter cholarmine:", min_value=0.0, step=0.1)
  sulfate = st.number_input("Enter sulfate:", min_value=0.0, step=0.1)
  cond= st.number_input("Enter conductivity:", min_value=0.0, step=0.1)
  carbon = st.number_input("Enter carbon:", min_value=0.0, step=0.1)
  turb = st.number_input("Enter turb:", min_value=0.0, step=0.1)
  trihalome = st.number_input("Enter trihalome:", min_value=0.0, step=0.1)
  model = load('random_forest_model881.joblib.gz')
  if st.button("predicit"):
   portability = predict_portability1(model, ph,hardness,solids,cholarmine,sulfate,cond,carbon,turb,trihalome)
   st.success(f"Predicted portability: {portability}")
   
  
  if portability==0:
    st.write("Be cautious: The water quality may be compromised. Consuming unsafe water can pose serious health risks.")
  elif portability==1:
    st.write("Stay hydrated with confidence: The water quality meets the necessary standards and is safe for consumption.")
    


         
 elif page=='water_depth':
  st.title("Embedding HTML in Streamlit")
  with open("home.html", "r", encoding="utf-8") as file1:
   html_content1 = file1.read()
  st.components.v1.html(html_content1, height=600, scrolling=True)
    
     
 
  st.title("Water Depth prediction")
  
  Latitude = st.number_input("Enter latitude:")
  Longitude= st.number_input("Enter longitude:")
  model = load('random_forest_model880.joblib.gz')
  if st.button("predicit"):
   portability = predict_portability2(model,Latitude,Longitude)
   st.success(f"Predicted Depth: {portability}")
        # Predict power
         
 

if __name__ == "__main__":
    main()
