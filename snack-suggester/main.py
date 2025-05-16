import streamlit as st
from dummy_db import snack_list
from suggester import SuggestionEngine
from user import User


if 'user' not in st.session_state:
    st.session_state.user = User("Guest")

if 'engine' not in st.session_state:
    st.session_state.engine = SuggestionEngine(snack_list)

if 'last_snack' not in st.session_state:
    st.session_state.last_snack = None

if 'current_menu' not in st.session_state:
    st.session_state.current_menu = None


menu = st.sidebar.radio("Choose Option", ["By Mood", "By Time", "Random", "Favorites"])

if st.session_state.current_menu != menu:
    st.session_state.current_menu = menu
    st.session_state.last_snack = None  

st.title("🍿 SnackSuggester - What to Eat Right Now?")
st.subheader("Feeling confused about snacks? Let us help!")


if menu == "By Mood":
    mood = st.text_input("What's your mood? (e.g. happy, sad, lazy, fresh)").lower()
    if st.button("Suggest Snack"):
        snack = st.session_state.engine.suggest_by_mood(mood)
        st.session_state.last_snack = snack

elif menu == "By Time":
    time = st.selectbox("Select time of day", ["morning", "afternoon", "evening", "night"])
    if st.button("Suggest Snack"):
        snack = st.session_state.engine.suggest_by_time(time)
        st.session_state.last_snack = snack

elif menu == "Random":
    if st.button("Give me a random snack"):
        snack = st.session_state.engine.suggest_random()
        st.session_state.last_snack = snack

if menu != "Favorites" and st.session_state.last_snack:
    st.success(f"Try this snack: **{st.session_state.last_snack}**")
    if st.button("Add to Favorites"):
        st.session_state.user.add_favorite(st.session_state.last_snack)
        st.info("Added to favorites!")

elif menu == "Favorites":
    favorites = st.session_state.user.get_favorites()
    st.subheader("Your Favorite Snacks")
    if favorites:
        for snack in favorites:
            st.write(f"🍴 {snack}")
    else:
        st.info("You have no favorite snacks yet.")
