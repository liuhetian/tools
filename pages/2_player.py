import streamlit as st
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

folder_path = Path('static/music/mp3/')
for item in folder_path.iterdir():
    if item.is_file():
        st.write(item.name)
        st.audio(str(item))