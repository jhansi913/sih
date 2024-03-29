import streamlit as st

def main():
    st.title("Click on the Map to Get Latitude and Longitude")

    # Display the map
    map_data = st.map()

    # Function to handle map click events
    def handle_click(lat, lon):
        st.write(f"Latitude: {lat}, Longitude: {lon}")

    # Register the click event handler
    map_data.on_click(handle_click)

if __name__ == "__main__":
    main()


