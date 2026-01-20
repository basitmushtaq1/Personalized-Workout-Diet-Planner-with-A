import streamlit as st

def render_sidebar():
    st.header("👤 Your Profile")
    age = st.number_input("Age", 10, 100, 22)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    weight = st.number_input("Weight (kg)", 30, 200, 70)
    height = st.number_input("Height (cm)", 100, 250, 170)
    
    st.header("🎯 Goals")
    goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Maintenance"])
    diet = st.selectbox("Diet Preference", ["Vegetarian", "Non-Vegetarian", "Vegan", "Eggitarian"])
    budget = st.slider("Daily Budget (₹/$)", 10, 500, 100)
    
    # Save to session
    st.session_state.user_data = {
        "age": age, "gender": gender, "weight": weight, "height": height,
        "fitness_goal": goal, "dietary_preference": diet, "budget": budget,
        "activity_level": "Moderate", "equipment": "Home/Gym", "location": "Home", "time_available": "45 mins"
    }