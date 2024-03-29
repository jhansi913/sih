import streamlit as st

def main():
    st.title("Click on the Map to Get Attributes")

    # Display the map
    map_data = st.map()

    # Add a place to display the attributes of the clicked location
    st.write("Latitude:")
    st.write("Longitude:")
    st.write("Attributes:")

    # Write the JavaScript function to handle click events
    st.markdown(
        """
        <script>
        const map = document.querySelector(".stDeckGlMap div:first-child");
        map.onclick = function(event) {
            const lat = event.latlng.lat;
            const lng = event.latlng.lng;
            
            // Send the latitude, longitude, and other attributes to Streamlit
            const latOutput = document.getElementById("lat-output");
            const lngOutput = document.getElementById("lng-output");
            const attrsOutput = document.getElementById("attrs-output");
            
            latOutput.textContent = lat;
            lngOutput.textContent = lng;
            attrsOutput.textContent = "Other attributes: ..."; // You can add more attributes here
        };
        </script>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()


