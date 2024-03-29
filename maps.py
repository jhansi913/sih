import streamlit as st
import folium

def main():
    st.title("Click on the Map to Get Latitude and Longitude")

    # Create a map centered around a specific location
    m = folium.Map(location=[0, 0], zoom_start=2)

    # Add a click handler to the map
    def handle_click(event):
        st.write("Latitude:", event.latlng[0])
        st.write("Longitude:", event.latlng[1])

    m.add_click_handler(handle_click)

    # Display the map
    folium_static(m)

if __name__ == "__main__":
    main()
