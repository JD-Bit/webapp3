from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain
import streamlit.components.v1 as components
import time

THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"

def run_snow_animation():
    rain(emoji= "❤️", font_size=20, falling_speed=5, animation_length="infinite")

st.set_page_config(page_title="V-day?", page_icon="❣️")

run_snow_animation()

with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; color: white;'>Will you be my valentine?😍</h1>", unsafe_allow_html=True)
st.image("dusty.jpg")

st.markdown(
    """
<style>
button {
    height: auto;
    padding-top: 15px !important;
    padding-bottom: 15px !important;
}
</style>
""",
    unsafe_allow_html=True,
)

col1, col2, col3, col4 = st.columns([1,1,1,1])
with col2:
    happy = st.button("YESS")
with col3:
    sad = st.button("HELL NOO")

if happy:
    st.markdown('# 😍 YAY!! See you at bugis MRT on 13/02/2024!! 😍')
elif sad:
    for i in range (20):
        st.markdown('pretty ' * i + "please!🥹")
        time.sleep(1)