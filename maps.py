import streamlit as st

def main():
    st.title("Click on the Map to Get Latitude and Longitude")

    # Initialize variables to store latitude and longitude
    latitude = None
    longitude = None

    # Display the map
    map_data = st.map()

    # Add a button to capture click
    if st.button("Capture Click"):
        # Set a session state flag to indicate we're capturing the click
        latitude, longitude = map_data.select_location()

    # Display the captured latitude and longitude
    if latitude is not None and longitude is not None:
        st.write("Latitude:", latitude)
        st.write("Longitude:", longitude)

if __name__ == "__main__":
    main()
