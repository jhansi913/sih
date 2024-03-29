import streamlit as st

def main():
    st.title("Click on the Map to Get Latitude and Longitude")

    # Display the map
    map_data = st.map()

    # Input fields for latitude and longitude
    latitude = st.number_input("Latitude", value=0.0)
    longitude = st.number_input("Longitude", value=0.0)

    # Add a button to capture the clicked location
    if st.button("Capture Click"):
        # Get the latitude and longitude from the map click (not supported directly in Streamlit)
        # For demonstration purposes, we'll use the input fields
        st.write("Latitude:", latitude)
        st.write("Longitude:", longitude)

if __name__ == "__main__":
    main()
