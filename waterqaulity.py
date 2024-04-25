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
  st.title("Borewells provide life-sustaining water to millions of people around the world.")
  st.image("borewell.webp")
  
 elif page=='water_quality':
  st.title("Water Quality prediction")
  st.image("water_chemicals.png")
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
  st.title("Water Depth prediction")
  with open("home.html", "r", encoding="utf-8") as file1:
   html_content1 = file1.read()
  st.components.v1.html(html_content1, height=600, scrolling=True)
    
     
 
   
  
  Latitude = st.number_input("Enter latitude:",format="%.5f")
  Longitude= st.number_input("Enter longitude:",format="%.5f")
  model = load('random_forest_model880.joblib.gz')
  if st.button("predicit"):
   portability = predict_portability2(model,Latitude,Longitude)
   st.success(f"Predicted Depth: {portability}")

        # Predict power
portability_list = []
depth_list = []         
if len(portability_list) >= 10 and len(depth_list) >= 10:
    data = pd.DataFrame({'Portability': portability_list[:10], 'Depth': depth_list[:10]})
    st.write("Stored Data for 10 Records:")
    st.write(data)

if __name__ == "__main__":
    main()
