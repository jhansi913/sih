import streamlit as st
import pandas as pd
from joblib import load
from streamlit.report_thread import get_report_ctx

class SessionState:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

def get_session_state():
    ctx = get_report_ctx()
    this_session = None
    session_infos = ctx.session_state

    for session_info in session_infos:
        if session_info.session_id == ctx.session_id:
            this_session = session_info

    if this_session is None:
        this_session = SessionState()
        session_infos.append(this_session)

    return this_session

def main():
    navigation_options = ['Welcome', 'water_quality', 'water_depth', 'final']

    # Create sidebar with navigation options
    page = st.sidebar.radio('Navigation', navigation_options)
    session_state = get_session_state()

    if page == 'Welcome':
        st.title("Borewells provide life-sustaining water to millions of people around the world.")
        st.image("borewell.webp")
    
    elif page == 'water_quality':
        st.title("Water Quality prediction")
        portability_list = session_state.get('portability_list', [])
        # Your input fields and prediction logic
        
        if st.button("predict water quality"):
            # Your prediction logic
            portability_list.append(portability)
            session_state.portability_list = portability_list
        
    elif page == 'water_depth':
        st.title("Water Depth Prediction")
        depth_list = session_state.get('depth_list', [])
        # Your input fields and prediction logic
        
        if st.button("predict water depth"):
            # Your prediction logic
            depth_list.append(depth)
            session_state.depth_list = depth_list

if __name__ == "__main__":
    main()
