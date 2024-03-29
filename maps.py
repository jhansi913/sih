import streamlit as st

# Define JavaScript to handle map clicks
js_code = """
<script>
document.addEventListener("DOMContentLoaded", function(event) {
    const map = document.querySelector(".stDeckGlMap div:first-child");

    map.addEventListener("click", function(event) {
        if (window.Streamlit) {
            const lat = event.latlng.lat;
            const lon = event.latlng.lng;
            
            // Set session state with latitude and longitude
            Streamlit.setComponentValue({latitude: lat, longitude: lon});
        }
    });
});
</script>
"""

# Inject JavaScript into Streamlit app
st.components.v1.html(js_code)

# Placeholder to display captured latitude and longitude
if st.session_state.get("latitude") is not None:
    st.write("Latitude:", st.session_state.latitude)
    st.write("Longitude:", st.session_state.longitude)


