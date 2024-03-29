import streamlit as st

def main():
    st.title("Click on the Map to Get Latitude and Longitude")

    # Display the map
    map_data = st.map()

    # Write the JavaScript function to handle click events
    js_code = """
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
    """
    st.components.v1.html(js_code)

    # Display the latitude and longitude of the clicked location
    clicked_location = st.session_state.get("clicked_location")
    if clicked_location:
        st.write("Latitude:", clicked_location["lat"])
        st.write("Longitude:", clicked_location["lon"])

if __name__ == "__main__":
    main()
