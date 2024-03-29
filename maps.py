import streamlit as st

def main():
    st.title("Click on the Map to Get Latitude and Longitude")

    # Display the map
    map_data = st.map()

    # Add a button to capture coordinates
    if st.button("Get Coordinates"):
        # Get the current coordinates from the map
        current_coordinates = map_data._coordinates
        if current_coordinates:
            st.write("Latitude:", current_coordinates[0], "Longitude:", current_coordinates[1])
        else:
            st.write("Click on the map to get coordinates.")

if __name__ == "__main__":
    main()
