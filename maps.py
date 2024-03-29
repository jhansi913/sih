import streamlit as st

def main():
    st.title("Click on the Map to Get Latitude and Longitude")

    # Display the map
    map_data = st.map()

    # Add a button to capture coordinates
    if st.button("Get Coordinates"):
        # Get the current coordinates from the map using locator widget
        location = st.locator("Click on the map")
        if location:
            st.write("Latitude:", location["lat"], "Longitude:", location["lon"])
        else:
            st.write("No coordinates selected.")

if __name__ == "__main__":
    main()

