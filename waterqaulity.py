import streamlit as st
import pickle
import gzip

def load_model(model_path):
    
    with gzip.open('random_forest_model.pkll.gz', 'rb') as file:
        saved_model = pickle.load(file)
     
    return model

def predict_portability(model, ph,hardness,solids,sulfate,cond,carbon,trihalome):
    input_features = [[ph,hardness,solids,sulfate,cond,carbon,trihalome]]
    portabilty = model.predict(input_features)[0]
    return portability

def main():
    st.title("Power Prediction App")

    # Load machine learning model
    model_path = "waterquality_pred.pkl"
    model = load_model(model_path)

    # User inputs
    ph = st.number_input("Enter ph:", min_value=0.0, step=0.1)
    hardness = st.number_input("Enter hardness:", min_value=0.0, step=0.1)
    solids = st.number_input("Enter solids:", min_value=0.0, step=0.1)
    sulfate = st.number_input("Enter sulfate:", min_value=0.0, step=0.1)
    cond= st.number_input("Enter conductivity:", min_value=0.0, step=0.1)
    carbon = st.number_input("Enter carbon:", min_value=0.0, step=0.1)
    trihalome = st.number_input("Enter trihalome:", min_value=0.0, step=0.1)
    
    
              

    # Button to predict power
    if st.button("Predict Power"):
        # Predict power
        portability = predict_portability(model, ph,hardness,solids,sulfate,cond,carbon,trihalome)
        st.success(f"Predicted portability: {portablity}")

if __name__ == "__main__":
    main()
