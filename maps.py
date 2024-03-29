import streamlit as st

def main():
    st.title("Click on the Map to Get Latitude and Longitude")

    # Display the map
    map_data = st.map()

    # Define the JavaScript code to capture click events
    js_code = """
    <script>
    document.addEventListener("DOMContentLoaded", function(event) {
        const map = document.querySelector(".leaflet-container");
        map.addEventListener("click", function(event) {
            const lat = event.latlng.lat;
            const lon = event.latlng.lng;
            const data = {lat: lat, lon: lon};
            const jsonString = JSON.stringify(data);
            const eventName = "map_click";
            const eventPayload = {event: eventName, value: jsonString};
            parent.postMessage(eventPayload, "*");
        });
    });
    </script>
    """

    # Inject the JavaScript code into the Streamlit app
    st.components.v1.html(js_code)

    # Listen for messages from the JavaScript code
    event = st.session_state.get("map_click")
    if event:
        data = event.get("value")
        if data:
            location = eval(data)  # Convert JSON string to dictionary
            st.write("Latitude:", location["lat"])
            st.write("Longitude:", location["lon"])

if __name__ == "__main__":
    main()
