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
LOTTIE_ANIMATION1 = ASSETS/ "monthsary.json"
LOTTIE_ANIMATION2 = ASSETS/ "hearts.json"

def run_snow_animation():
    rain(emoji= "😘", font_size=20, falling_speed=5, animation_length="infinite")

def load_lottie_animation(file_path):
    with open(file_path,"r") as f:
        return json.load(f)

st.set_page_config(page_title="05/06/2024", page_icon="❣️")

run_snow_animation()

with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🥰Happy THREE MONTHS BABYY🥰")
lottie_animation1 = load_lottie_animation(LOTTIE_ANIMATION1)
st.lottie(lottie_animation1, key ="lottie-monthsary", height= 300)


st.markdown("I want take the moment to remind you of how incredible you are to me. Your presence in my life has brought me so much joy and happiness that I never knew was possible. With you, I've found a love that is genuine and pure. Thank you for giving me the chance to hopefully bring you as much joy and happiness that you brought me, and I am eternally grateful to call you my girlfriend. I will always be by your side regardless of how tough and complicated things may get because you are worth it and I want you to know that. I can't wait for the day where we are walking by the beach while the sun is setting with our golden retriever and of course with our son, dusty. Heres to a lifetime of laughter, love and unforgettable memories!")
st.markdown("'There's nothing, like doing nothing. With you~'")
st.markdown("")
st.markdown("")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        lottie_animation2 = load_lottie_animation(LOTTIE_ANIMATION2)
        st.lottie(lottie_animation2, key ='lottie-hearts', height =200 )
    with right_column:
        st.markdown("")
        st.write("")
        st.markdown("Lets have fun and enjoy ourselves today, better hold my hand while we are going on all them rollercoaster rides!")
        st.markdown("Hopefully we get to take some pics together today:)")

#st.markdown("<h1 style='text-align: center; color: white;'>Will you be my valentine?😍</h1>", unsafe_allow_html=True)

#st.markdown(
#    """
#<style>
#button {
#    height: auto;
#    padding-top: 15px !important;
#    padding-bottom: 15px !important;
#}
#</style>
#""",
#    unsafe_allow_html=True,
#)

#col1, col2, col3, col4 = st.columns([1,1,1,1])
#with col2:
#    happy = st.button("YESS")
#with col3:
#    sad = st.button("HELL NOO")

#if happy:
#    st.markdown('# 😍 YAY!! See you at bugis MRT on 13/02/2024!! 😍')
#elif sad:
#    for i in range (20):
#        st.markdown('pretty ' * i + "please!🥹")
#        time.sleep(1)