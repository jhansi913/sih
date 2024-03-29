import streamlit as st

def main():
    st.title("Click on the Map to Get Latitude and Longitude")

    # Display the map
    map_data = st.map()

    # Write the JavaScript function to handle click events
    st.markdown(
        """
        <script>
        const map = document.querySelector(".stDeckGlMap div:first-child");

        map.addEventListener("click", function(event) {
            const lat = event.latlng.lat;
            const lon = event.latlng.lng;
            
            // Send the latitude and longitude to Streamlit
            const data = {lat: lat, lon: lon};
            Streamlit.setComponentValue(data);
        });
        </script>
        """,
        unsafe_allow_html=True
    )

    # Read the latitude and longitude from the JavaScript event
    clicked_location = st.empty()
    if st.session_state.get("clicked_location"):
        st.write("Latitude:", st.session_state.clicked_location["lat"])
        st.write("Longitude:", st.session_state.clicked_location["lon"])

if __name__ == "__main__":
    main()

